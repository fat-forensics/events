# Hands-on Resources (ECML-PKDD 2020) #
The Jupyter Notebooks included in this directory are *hands-on* materials
used for the [ECML-PKDD 2020](https://ecmlpkdd2020.net/) hands-on tutorial:

> **What and How of Machine Learning Transparency:**  
  *Building Bespoke Explainability Tools with Interoperable Algorithmic
  Components*

These resources provide guidance on building bespoke surrogate explainers
of individual black-box predictions for tabular data.
See [events.fat-forensics.org](https://events.fat-forensics.org/) for more
details.

## Help with the Hands-on Exercises ##
During *Part 3.2* of the tutorial you can reach out via the dedicated Slack
workspace to ask questions and get help with any issues or problems.
Registration for the workspace is limited to ECML-PKDD 2020 participants --
the sign-up URL can be found in the Whova app and on the ECML-PKDD 2020
website.

[![Chat via Slack](https://img.shields.io/badge/slack-FAT%20Forensics%20events-yellow.svg?logo=slack)](https://fatforensicsevents.slack.com/)

## Contents ##
This directory holds five Jupyter Notebook, a Python library dedicated for this
tutorial and a file with Python packages required to execute the notebooks.

* [`0-environment-test.ipynb`](0-environment-test.ipynb) -- a test notebook
  used to *validate* environment setup.
* [`1-data-sets.ipynb`](1-data-sets.ipynb) -- a notebook discussing two
  *data sets* that are used throughout the tutorial.
* [`2-interpretable-representations.ipynb`](2-interpretable-representations.ipynb)
  -- a notebook introducing *interpretable representations*.
* [`3-data-sampling.ipynb`](3-data-sampling.ipynb) -- a notebook covering
  various *data sampling* approaches.
* [`4-explanation-generation.ipynb`](4-explanation-generation.ipynb) -- a
  notebook walking through *explanation generation* procedure.

---

* [`fatf_ecml.py`](fatf_ecml.py) -- a Python library with helper functions used
  throughout the notebooks.
* [`requirements.txt`](requirements.txt) -- a list of (two) Python packages
  required to run the notebooks. (See below for more details.)

## Executing the Notebooks ##
There are three distinct ways in which you can run the Jupyter Notebooks.
First, you can install the required dependencies, download the notebooks and
run them on your own machine.
Alternatively, you can execute them online directly in your web browser
(no installation required) using either of the two Jupyter Lab services:
[My Binder](https://mybinder.org/) or
[Google Colab](https://colab.research.google.com/).

### Local Installation ###
First you need to install the required Python packages.
You can either do it manually with:
``` bash
$ pip install fat-forensics[all]
$ pip install jupyterlab
```

or use the [`requirements.txt`](requirements.txt) file:
``` bash
$ pip install -r requirements.txt
```

Then you should run the Jupyter Lab server in the directory that holds
the notebooks with:
``` bash
$ jupyter lab
```

To download the notebooks (contents of this directory) you need to get a copy
of this GitHub repository.
You can download a ZIP archive by licking this
[link](https://github.com/fat-forensics/events/archive/master.zip).
Alternatively, you can clone it with `git` using the following command:
``` bash
$ git clone https://github.com/fat-forensics/events.git
```

### Google Colab ###
To run the notebooks in your browser with Google Colab click the button below
and select the desired notebook from the list (a Google account is required).
**Beware that any changes you make will not be saved unless you click the
`Copy to Drive` button (visible at the top) and open your Google Drive
copy of the notebook in a new tab when prompted.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fat-forensics/events/blob/master/)

### My Binder ###
To run the notebooks in your browser with My Binder click the button below.
Then, you need to navigate to the `resources/2020_ecml-pkdd/notebooks/`
directory.
**Beware that any changes you make will not be saved unless you download
the notebook that you are working on (use the `File -> Download as -> Notebook`
menu option in Binder).**

[![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fat-forensics/events/master)
