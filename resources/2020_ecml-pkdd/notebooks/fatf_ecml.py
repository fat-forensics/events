"""
ECML-PKDD 2020 FAT Forensics Hands-on Tutorial
==============================================

This library implements a collection of helper functions used by the Jupyter
Notebooks designated for the FAT Forensics hands-on tutorial organised
at ECML-PKDD 2020.
Please see <https://events.fat-forensics.org/> for more details.
"""
# Author: Kacper Sokol <k.sokol@bristol.ac.uk>
#         Alex Hepburn <ah13558@bristol.ac.uk>
# License: new BSD

import io
import os
import requests
import scipy
import scipy.stats
import sys
import zipfile

import sklearn.datasets
import sklearn.ensemble
import sklearn.model_selection
import sklearn.preprocessing
import sklearn.svm

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

try:
    import google.colab
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

try:
    import fatf
    FATF_INSTALLED = True
except ImportError:
    FATF_INSTALLED = False


def initialise_colab():
    """
    Installs FAT Forensics with all its auxiliary dependencies when in Colab.
    """
    global FATF_INSTALLED
    if IN_COLAB:
        if not FATF_INSTALLED:
            print('Installing FAT Forensics.')
            stream = os.popen(
                '{} -m pip install fat-forensics[all]'.format(sys.executable))
            output = stream.read()
            print(output)
            FATF_INSTALLED = True
        else:
            print('FAT Forensics is already installed.')
    else:
        print('Not in Colab; nothing to do.')


def generate_2d_moons(random_seed=None):
    """
    Generates a two-dimensional *Two Moons* data set.

    The data set has 1200 training instances and 300 test instances.
    It is generated with 0.25 noise parameter and its features are scaled
    to the [0, 1] range.

    For reproducibility of the data sampling and train/test split,
    you may wish to set the ``random_seed`` parameter.

    Parameters
    ----------
    random_seed : integer, optional (default=None)
        A random seed used to initialise Python's and numpy's ``random``
        modules. If ``None``, the random seeds are not fixed.

    Returns
    -------
    train_X : 2-dimensional numpy array
        A numpy array holding the train data.
    test_X : 2-dimensional numpy array
        A numpy array holding the test data.
    train_y : 1-dimensional numpy array
        A numpy array holding labels of the train data.
    test_y : 1-dimensional numpy array
        A numpy array holding labels of the test data.
    """
    assert random_seed is None or isinstance(random_seed, int), 'Incorrect seed.'
    if random_seed is not None:
        import fatf
        fatf.setup_random_seed(random_seed)

    # Load Moons Dataset
    moons_data, moons_target = sklearn.datasets.make_moons(
        n_samples=1500, noise=0.25)

    # Scale it between 0 and 1
    scaler = sklearn.preprocessing.MinMaxScaler(feature_range=(0, 1))
    moons_data = scaler.fit_transform(moons_data)

    # Split into test and train data
    train_X, test_X, train_y, test_y = sklearn.model_selection.train_test_split(
          moons_data, moons_target, test_size=0.2)

    return train_X, test_X, train_y, test_y


def _download_bikes():
    """
    Downloads the UCI Bike Sharing data set and extracts a subset of its features.

    This function downloads the UCI Bike Sharing data set
    <https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset>
    and removes the following two features:

    * record index, and
    * date.

    Out of the three target variables (casual, registered and cnt),
    it selects *cnt*, which represents the total number of bikes rented
    during a given day.

    Returns
    -------
    bikes_data : 2-dimensional numpy array
        A numpy array holding the data.
    bikes_target : 1-dimensional numpy array
        A numpy array holding the target variable of the data (the number of
        bikes rented on a given day).
    bikes_feature_names : list of strings
        A Python list holding the feature names.
    bikes_target_name : string
        A string with the name of the target variable.
    """
    # Load Bikes
    url=('https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'
         'Bike-Sharing-Dataset.zip')
    request = requests.get(url)
    request_io_stream = io.BytesIO(request.content)

    with zipfile.ZipFile(request_io_stream) as file:
        data = file.read('day.csv').decode('utf-8')

    # Do not read the first two columns (0: index, 1: date); and skip the two
    # penultimate ones (13: casual users count, 14: registered users count)
    # since the last one (15) is the total count.
    column_ids = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15)
    _bikes_data = np.genfromtxt(
        io.StringIO(data),
        delimiter=',',
        skip_header=1,
        usecols=column_ids,
        dtype=np.float32)

    # Separate data from target
    ## Drop the target column
    bikes_data = np.delete(_bikes_data, -1, axis=1)
    ## Target is the total bike rental count
    bikes_target = _bikes_data[:, -1]

    # Get the feature names from the csv header
    _bikes_names = []
    for i, name in enumerate(data.split('\n')[0].split(',')):
        if i in column_ids:
            _bikes_names.append(name.strip())

    # Separate data from target
    bikes_feature_names = _bikes_names[:-1]
    bikes_target_name = _bikes_names[-1]

    return bikes_data, bikes_target, bikes_feature_names, bikes_target_name


def _preprocess_bikes_target(bikes_target):
    """
    Discretises the target variable of the UCI Bike Sharing data set.

    This function bins the regression target variable of the UCI Bike Sharing
    data set (see :func:`_download_bikes`) into three classes, making it a
    classification task:

    * ``0`` is *low*: 0 <= y < 4000;
    * ``1`` is *medium*: 4000 <= y < 6000; and
    * ``2`` is *high*: 6000 <= y < 9000.

    Parameters
    ----------
    bikes_target : 1-dimensional numpy array
        A numpy array holding the target variable of the UCI Bike Sharing data
        set (the number of bikes rented on a given day).

    Returns
    -------
    bikes_binned_target : 1-dimensional numpy array
        A discretised version of the ``bikes_target`` array.
    """
    bins = [0.0, 4000.0, 6000.0, 9000.0]
    # Subtract 1 to start the count from 0
    bikes_binned_target = np.digitize(bikes_target, bins=bins) - 1

    return bikes_binned_target


def generate_bikes(random_seed=None):
    """
    Generates the UCI Bike Sharing data set.

    This function downloads the Bike Sharing data set from the UCI repository
    and removes *record index* and *date* features
    (see :func:`_download_bikes`).
    It also discretises the target variable into three classes: *low* (0),
    *medium* (1) and *high* (2) -- see :func:`_preprocess_bikes_target`.

    For reproducibility of the train/test split, you may wish to set the
    ``random_seed`` parameter.

    Parameters
    ----------
    random_seed : integer, optional (default=None)
        A random seed used to initialise Python's and numpy's ``random``
        modules. If ``None``, the random seeds are not fixed.

    Returns
    -------
    train_X : 2-dimensional numpy array
        A numpy array holding the train data.
    test_X : 2-dimensional numpy array
        A numpy array holding the test data.
    train_y : 1-dimensional numpy array
        A numpy array holding labels of the train data.
    test_y : 1-dimensional numpy array
        A numpy array holding labels of the test data.
    bikes_feature_names : list of strings
        A Python list holding the feature names.
    bikes_target_name : string
        A string with the name of the target variable.
    """
    assert random_seed is None or isinstance(random_seed, int), 'Incorrect seed.'
    if random_seed is not None:
        import fatf
        fatf.setup_random_seed(random_seed)

    # Load Bikes
    bikes_data, bikes_target, bikes_feature_names, bikes_target_name = (
        _download_bikes()
    )

    # Convert the regression target into classification
    bikes_classification_target = _preprocess_bikes_target(bikes_target)

    # Split into test and train data
    train_X, test_X, train_y, test_y = sklearn.model_selection.train_test_split(
        bikes_data, bikes_classification_target,
        test_size=0.2,
        stratify=bikes_classification_target)

    return (train_X, test_X, train_y, test_y,
            bikes_feature_names, bikes_target_name)


def get_boston():
    """
    Generates the Boston Housing data set.

    The target variable is discretised into two classes: *low* (0) and
    *high* (1).
    The discretisation threshold is fixed at 20.

    Returns
    -------
    X : 2-dimensional numpy array
        A numpy array holding the data.
    y_class : 1-dimensional numpy array
        A numpy array holding discretised labels of the data.
    """
    X, y = sklearn.datasets.load_boston(return_X_y=True)
    y_class = np.zeros_like(y, dtype=np.int8)
    y_class[y >= 20] = 1

    return X, y_class


def get_random_forest(data, target, random_seed=None):
    """
    Fits a Random Forest classifier.

    This function fits a Random Forest classifier using the scikit-learn's
    ``sklearn.ensemble.RandomForestClassifier`` class.

    For reproducibility of the model, you may wish to set the
    ``random_seed`` parameter.

    Parameters
    ----------
    data : 2-dimensional numpy array
        Training data of the model.
    target : 1-dimensional numpy array
        Target variable (classification) for the training data of the model.
    random_seed : integer, optional (default=None)
        A random seed used to initialise Python's and numpy's ``random``
        modules as well as scikit-learn's ``random_state`` parameter.
        If ``None``, the random seeds are not fixed.

    Returns
    -------
    clf : sklearn.ensemble.RandomForestClassifier
        A fitted Random Forest classifier.
    """
    assert random_seed is None or isinstance(random_seed, int), 'Incorrect seed.'
    if random_seed is not None:
        import fatf
        fatf.setup_random_seed(random_seed)

    clf = sklearn.ensemble.RandomForestClassifier(
        n_estimators=5, max_depth=7, random_state=random_seed)
    clf.fit(data, target)

    return clf


def get_svc(data, target, random_seed=None):
    """
    Fits a Support Vector Machine classifier.

    This function fits a Support Vector Machine classifier using the
    scikit-learn's ``sklearn.svm.SVC`` class.

    For reproducibility of the model, you may wish to set the
    ``random_seed`` parameter.

    Parameters
    ----------
    data : 2-dimensional numpy array
        Training data of the model.
    target : 1-dimensional numpy array
        Target variable for the training data of the model.
    random_seed : integer, optional (default=None)
        A random seed used to initialise Python's and numpy's ``random``
        modules as well as scikit-learn's ``random_state`` parameter.
        If ``None``, the random seeds are not fixed.

    Returns
    -------
    clf : sklearn.ensemble.RandomForestClassifier
        A fitted Support Vector Machine classifier.
    """
    assert random_seed is None or isinstance(random_seed, int), 'Incorrect seed.'
    if random_seed is not None:
        import fatf
        fatf.setup_random_seed(random_seed)

    clf = sklearn.svm.SVC(probability=False, random_state=random_seed)
    clf.fit(data, target)

    return clf


def gini_index(x):
    """
    Computes a Gini Index of a numpy array.

    Parameters
    ----------
    x : 1-dimensional numpy array
        An array with class predictions or labels.

    Returns
    -------
    gini : float
        Gini Index of the ``x`` array.
    """
    x_ = np.asarray(x)
    _, counts = np.unique(x_, return_counts=True)
    frequencies = counts / x_.shape[0]

    gini_itemwise = frequencies * (1 - frequencies)

    gini = np.sum(gini_itemwise)

    assert 0 <= gini <= 1

    return gini


def entropy(x, base=None):
    """
    Computes entropy of a numpy array.

    Parameters
    ----------
    x : 1-dimensional numpy array
        An array with class predictions or labels.
    base : integer, optional (default=None)
        Base of the logarithm used for computing entropy. By default
        (``None``), the natural logarithm is used.

    Returns
    -------
    entropy_ : float
        Entropy of the ``x`` array.
    """
    assert base is None or isinstance(base, int), 'Wrong type.'

    _, counts = np.unique(x, return_counts=True)
    entropy_ = scipy.stats.entropy(counts, base=base)

    return entropy_


def mse(x):
    """
    Computes Mean Squared Error of a numpy array.

    Parameters
    ----------
    x : 1-dimensional numpy array
        An array with regression or probabilistic predictions.

    Returns
    -------
    mse_ : float
        Mean Squared Error of the ``x`` array.
    """
    # Error
    err = x - np.mean(x)
    # Squared error
    err_sq = np.square(err)
    # Mean Squared Error
    mse_ = np.mean(err_sq)

    return mse_


def get_hyperrectangle_indices(discretised_data, hyperrectangle):
    """
    Extracts row indices of a data array that match the specified sample.

    This function returns row indices of the ``discretised_data`` array that
    are identical to the ``hyperrectangle`` array.
    The data set has to be discretised, i.e., all of its values have to be
    between 0 and 3 inclusive.

    Parameters
    ----------
    discretised_data : 2-dimensional numpy array
        A 2-dimensional array with data.
    hyperrectangle : 1-dimensional numpy array
        A 1-dimensional array that will be matched against each row of the
        ``discretised_data`` array.

    Returns
    -------
    matching_indices : 1-dimensional numpy array
        An array with indices of the matching rows.
    """
    import fatf.utils.array.validation as fatf_v
    hyperrectangle_ = np.asarray(hyperrectangle)

    assert np.all(0 <= discretised_data), 'Data probably not discretised.'
    if not fatf_v.is_1d_array(discretised_data):
        assert (discretised_data.shape[1]
                == hyperrectangle_.shape[0]), 'Size mismatch.'

    matching_rows = (discretised_data == hyperrectangle)
    if not fatf_v.is_1d_array(discretised_data):
        matching_rows = matching_rows.all(axis=1)
    matching_indices = np.where(matching_rows)[0]

    return matching_indices


def weighted_purity(discretised_data, labels, metric):
    """
    Computes weighted purity metric of ``labels`` based on grouping given by
    unique encodings in the ``discretised_data`` array.

    This function identifies unique rows in the ``discretised_data`` array and
    computes user-selected purity metric for the corresponding labels
    (extracted from the ``labels`` array).
    The final result is computed as a weighted average of these individual
    metrics, where the weights are proportions of instances used to compute
    each individual metric.
    (See the Jupyter Notebook for *Interpretable Representation*
    [``1-interpretable-representations.ipynb``]
    -- ECML-PKDD 2020 hands-on tutorial -- for more details.)

    The data set (``discretised_data``) has to be discretised, i.e., all of its
    values have to be between 0 and 3 inclusive.
    The labels (``labels``) are either:

    * *crisp* predictions of a classifier or *class* labels; or
    * *numbers* representing regression values or *probabilistic* predictions
      for a single class (in case of probabilistic classifiers).

    The ``metric`` has to be chosen appropriately to the type of ``labels``:

    * ``'mse'`` (Mean Squared Error) used for **numerical** ``labels``; and
    * ``'gini'`` (Gini Index) used for **crisp** ``labels``.

    Parameters
    ----------
    discretised_data : 2-dimensional numpy array
        A 2-dimensional array with *discretised* data.
    labels : 1-dimensional numpy array
        A 1-dimensional array with labels either holding *numbers* (regression
        values or probabilistic predictions of a single class) or *crisp*
        labels (class predictions or ground truth labels).
    metric : string
        Either ``'mse'`` for Mean Squared Error or ``'gini'`` for Gini Index.

    Returns
    -------
    weighted_purity_ : float
        A weighted purity (``metric``) of the ``labels`` based on the partition
        of the ``discretised_data`` array.
    """
    import fatf.utils.array.validation as fatf_v
    assert np.all(0 <= discretised_data), 'Data probably not discretised.'
    #
    assert (discretised_data.shape[0] == labels.shape[0]), 'Size mismatch.'
    #
    assert metric.lower() in ('mse', 'gini'), (
        'Incorrect metric specifier. Should either be *mse* or *gini*.')

    items_count = discretised_data.shape[0]
    unique_hr = np.unique(discretised_data, axis=0)

    metric_fn = mse if metric.lower() == 'mse' else gini_index

    individual_purity = []
    for encoding in unique_hr:
        matching_rows = (discretised_data == encoding)
        if not fatf_v.is_1d_array(discretised_data):
            matching_rows = matching_rows.all(axis=1)
        matching_indices = np.where(matching_rows)[0]

        hr_metric = metric_fn(labels[matching_indices])
        hr_items_count = matching_indices.shape[0]

        individual_purity.append(hr_metric * hr_items_count)

    weighted_purity_ = np.sum(individual_purity) / items_count

    return weighted_purity_


def one_hot_encode(vector):
    """
    One-hot-encode the ``vector``.

    The order of one-hot-encoding is based on sorted unique values of the
    ``vector``.

    Parameters
    ----------
    vector : 1-dimensional numpy array
        A 1-dimensional array with *discrete* values.

    Returns
    -------
    ohe : 2-dimensional numpy array
        A binary 2-dimensional array with one-hot-encoded ``vector``.
    """
    import fatf.utils.array.validation as fatf_v

    vector = np.asarray(vector)
    assert fatf_v.is_1d_array(vector), 'vector has to be 1-D.'

    unique = np.sort(np.unique(vector))
    unique_count = unique.shape[0]

    ohe = np.zeros((vector.shape[0], unique_count), dtype=np.int8)

    for i, v in enumerate(unique):
        indices = get_hyperrectangle_indices(vector, v)
        ohe[indices, i] = 1

    return ohe


def get_bin_sampling_values(dataset, discretiser):
    """
    Captures the mean and standard deviation of the ``dataset`` for each
    hyper-rectangle encoded by the ``discretiser``.

    Parameters
    ----------
    dataset : 2-dimensional numpy array
        A data set to be analysed.
    discretiser : fat-forensics discretiser object
        A (fitted) discretiser that is compatible with the ``dataset``.

    Returns
    -------
    bin_sampling_values : dictionary of dictionaries holding 4-tuples
        The outer dictionary indicates the feature in the original data
        representation; the inner dictionary signifies a partition (quartile)
        of this feature. Under these two keys, a four-tuple holds the:
        minimum, maximum, mean and standard deviation (in this order)
        values of data points within this partition.
    """
    dataset_discretised = discretiser.discretise(dataset)

    bin_sampling_values = {}
    for index in range(discretiser.features_number):
        bin_sampling_values[index] = {}

        discretised_feature = dataset_discretised[:, index]
        feature = dataset[:, index]

        # The bin IDs need to be sorted as they are retrieved from
        # dictionary keys (hence may come in a random order), therefore
        # interfering with the enumerate procedure.
        bin_ids = sorted(
            list(discretiser.feature_value_names[index].keys()))
        bin_boundaries = discretiser.feature_bin_boundaries[index]
        for bin_i, bin_id in enumerate(bin_ids):
            bin_feature_indices = (discretised_feature == bin_id)
            bin_feature_values = feature[bin_feature_indices]

            # If there is data in the bin, get its empirical mean and
            # standard deviation, otherwise use numpy nan.
            # If there are no data in a bin, the frequency of this bin
            # will be 0, therefore data will never get sampled from this
            # bin, i.e., there will be no attempt to undiscretised them.
            if bin_feature_values.size:
                mean_val = bin_feature_values.mean()
                std_val = bin_feature_values.std()
            else:
                mean_val = np.nan
                std_val = np.nan

            # Use the true bin boundaries (extracted from the discretiser).
            # For the edge bins (with -inf and +inf edges) use the
            # empirical minimum and maximum (if possible) to avoid problems
            # with reverse sampling (see the _undiscretise_data method).
            if bin_i == 0:
                if bin_feature_values.size:
                    min_val = bin_feature_values.min()
                else:
                    min_val = -np.inf  # pragma: nocover
                    assert False, (  # pragma: nocover
                        'Since the upper bin boundary is inclusive in '
                        'the quartile discretiser this can never happen.')
                max_val = bin_boundaries[bin_i]
            # This is bin id count (+1) and not bind boundary count.
            elif bin_i == bin_boundaries.shape[0]:
                min_val = bin_boundaries[bin_i - 1]
                if bin_feature_values.size:
                    max_val = bin_feature_values.max()
                else:
                    max_val = np.inf
            else:
                min_val = bin_boundaries[bin_i - 1]
                max_val = bin_boundaries[bin_i]

            bin_sampling_values[index][bin_id] = (min_val, max_val,
                                                  mean_val, std_val)

    return bin_sampling_values


def undiscretise_data(discretised_data, discretiser, dataset):
    """
    Transforms discretised data back into their original representation.

    This function uses truncated normal sampling fitted into each
    hyper-rectangle.

    Parameters
    ----------
    discretised_data : 2-dimensional numpy array
        A discretised data set (in quartile representation) to be
        undiscretised.
    discretiser : fat-forensics discretiser object
        A (fitted) discretiser that is compatible with the ``dataset``
        (used to extract boundaries of hyper-rectangles).
    dataset : 2-dimensional numpy array
        A data set used to extract mean and standard deviation of each
        hyper-rectangle.

    Returns
    -------
    bin_sampling_values : 2-dimensional numpy array
        Undiscretised ``discretised_data``.
    """
    bin_sampling_values = get_bin_sampling_values(dataset, discretiser)
    dataset_dtype = dataset.dtype

    # Create a placeholder for undiscretised data. We copy the discretised
    # array instead of creating an empty one to preserve the values of
    # sampled categorical features, hence we do not need to copy them
    # later on. We also need to change the type of the array to correspond
    # to the original dataset.
    undiscretised_data = discretised_data.copy().astype(dataset_dtype)

    for index in range(discretised_data.shape[1]):
        discretised_column = discretised_data[:, index]
        undiscretised_column = undiscretised_data[:, index]

        unique_column_values = np.unique(discretised_column)
        for bin_id, bin_values in bin_sampling_values[index].items():
            if bin_id in unique_column_values:
                # Since sampling values must have been found in this bin,
                # there should be an empirical mean (2) and
                # standard deviation (3).

                bin_indices = np.where(discretised_column == bin_id)[0]
                samples_number = bin_indices.shape[0]

                min_, max_, mean_, std_ = bin_values
                if std_:
                    lower_bound = (min_ - mean_) / std_
                    upper_bound = (max_ - mean_) / std_

                    unsampled = scipy.stats.truncnorm.rvs(
                        lower_bound,
                        upper_bound,
                        loc=mean_,
                        scale=std_,
                        size=samples_number)
                else:
                    unsampled = np.array(samples_number * [mean_])

                undiscretised_column[bin_indices] = unsampled
    return undiscretised_data
