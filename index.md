---
layout: custom
---

# What and How of Machine Learning Transparency #
{:.no_toc}
### Building Bespoke Explainability Tools with Interoperable Algorithmic Components ###
{:.no_toc}

<!--
https://www.timeanddate.com/worldclock/fixedtime.html?msg=FAT%20Forensics%20Hands-on%20Tutorial&iso=20200918T14&p1=1246&ah=4
-->

<table>
  <thead>
    <tr>
      <th style="text-align: left" colspan="2">An online hands-on tutorial at <a href="https://ecmlpkdd2020.net/">ECML-PKDD 2020</a></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Where:</td>
      <td style="text-align: left"><b>Virtual</b>, through the ECML-PKDD 2020 conference, Ghent, Belgium.</td>
    </tr>
    <tr>
      <td style="text-align: left">When:</td>
      <td style="text-align: left">Friday, September 18<sup>th</sup>, 2020.</td>
    </tr>
    <tr>
      <td style="text-align: left">Tutorial access:</td>
      <td style="text-align: left"><b>Recordings</b> will be made available soon.</td>
    </tr>
  </tbody>
</table>

> **We strongly suggest participants prepare for the hands-on exercises
  beforehand.
  Please have a look at the slides corresponding to the "hands-on
  session preparation" section of
  [Part 2](#part-2-getting-to-know-fat-forensics) of the tutorial and the
  [notebooks page]({{ site.notebooks }}).
  They explain different ways to participate:**
  * **installing the Python package and downloading the Jupyter Notebooks on
    your own machine;**
  * **executing the notebooks online via Google Colab (a Google account is
    required); and**
  * **running the notebooks via My Binder directly in the browser.**

## Table of Contents ##
{:.no_toc}

* TOC
{:toc}

## About the Tutorial ##
In this hands-on tutorial we:
* introduce popular interpretability, explainability and transparency
  techniques for tabular data;
* discuss their strengths and weaknesses;
* illustrate how to identify their interoperable *algorithmic components*;
* show how to decompose them into these atomic functional blocks; and
* demonstrate how to use these components to (re)build robust explainers with
  well-known failure points.

In particular, we focus on popular surrogate explainers such as
*Local Interpretable Model-agnostic Explanations* (LIME[^1]).
They are *model-agnostic*, *post-hoc* and compatible with a diverse
*range of data types* -- image, text and tabular -- making them a popular
choice for explaining black-box predictions.
We embrace this ubiquity and teach participants how to improve upon such
off-the-shelf solutions by taking advantage of the aforementioned modularity.
In particular, we demonstrate how to harness it to compose a suite of bespoke
transparency forensic tools for black-box models and their predictions.

&nbsp;&nbsp;&nbsp;Our effort to build custom explainers from
interoperable algorithmic modules is grounded with a theoretical introduction
followed by interactive coding exercises.
This structure supports two distinct goals: **research & development** as well
as **deployment** of such tools.
The hands-on part of the tutorial, therefore, walks the attendees through
*building* and *validating* their own, tailor-made, *transparency techniques*
in the context of surrogate explainers designated for tabular data.
For example, it demonstrates how choosing their three core modules[^3] --
interpretable data representation, data sampling and explanation generation --
influences the type and quality of the resulting explanations of black-box
predictions.
These programming exercises are delivered using
[`FAT Forensics`](https://fat-forensics.org/)[^2][^4] -- a Python toolbox
open-sourced under the BSD 3-Clause license and designed for inspecting
Fairness, Accountability and Transparency (FAT) aspects of data, models and
predictions.

## Citation ##
To reference this tutorial please use:
```bibtex
@misc{sokol2020what,
  author       = {Sokol, Kacper and
                  Hepburn, Alexander and
                  Santos-Rodriguez, Raul and
                  Flach, Peter},
  title        = {{ "{{" }}W}hat and How of Machine Learning Transparency:
                  {B}uilding Bespoke Explainability Tools with
                  Interoperable Algorithmic Components},
  month        = sep,
  year         = 2020,
  publisher    = {Zenodo},
  version      = {2020ecmlpkdd},
  doi          = {10.5281/zenodo.4035128},
  url          = {https://doi.org/10.5281/zenodo.4035128}
}
```

## Motivation ##
Many public-domain implementations of transparency, interpretability and
explainability (TIE) algorithms are a result of academic research projects.
As such, the development of these tools usually starts with a particular
research goal in mind, e.g., demonstrating the capabilities of a proposed
method.
In practice, this often means that the software is engineered without an
elaborate design, which tends to be detrimental for its reusability and
modularity.
Moreover, such tools are usually aimed at a general audience -- making them
easy to use for non-experts -- which requires hiding all of their complexity
away from the user.
For example, this can be achieved by providing a TIE functionality as an
end-to-end "product" and only allowing its customisation through designated
parameters exposed via an accessible Application Programming Interface (API).
However, more advanced users such as researchers and developers -- who want to
build on top of these implementations or deploy them in a custom system --
may need to resort to tinkering with the source code, which can be frustrating
and time consuming.
While creating strictly modular TIE tools may be desirable, this approach comes
at the expense of a more complex design and an API that is not necessarily
suitable for a lay audience, thus limiting the reach and appeal of such
a software.

&nbsp;&nbsp;&nbsp;In this tutorial, we address the challenges highlighted
above and provide participants with knowledge and hands-on skills to help them:
* identify core building blocks of popular TIE approaches;
* understand the transparency requirements of their use cases; and
* fulfil these desiderata by building bespoke explainers that improve upon
  off-the-shelf solutions.

To this end, we demonstrate how a modular software design -- bundling all of
the reusable TIE algorithmic components in a single package under a
standardised API -- combines the best of both worlds and caters to technical
and casual users alike.
By offering access to a low-level API of TIE building blocks, we supply a
collection of algorithms that can be used by technical users -- researchers and
developers -- to compose their own bespoke explainers.
Additionally, we use these components to build popular and easy to use TIE
algorithms as part of the API targeted at a lay audience.
This modular software design is embodied in an open source Python package --
[`FAT Forensics`](https://fat-forensics.org/) -- which we released to improve
and advance reproducibility of TIE algorithms and provide native access to
their vital components.

&nbsp;&nbsp;&nbsp;By participating in this tutorial, academics can gain
insights into experimenting with the algorithmic design and building blocks of
state-of-the-art explainers -- a perspective that is uncommon among other
educational resources in this space, which simply show how to apply such tools.
Attendees from industry, on the other hand, can learn to build and tune
bespoke explainers of black-box machine learning models and their predictions
to meet their business needs, e.g., improve transparency of deployed predictive
models or extract important insights for relevant stakeholders.
The tutorial also briefly discusses best practices of software engineering
for machine learning research and highlights benefits of modular design, both
of which contribute to sustainable and reproducible research in the field.
Our hands-on approach provides participants with first-hand experience,
leading to a better understanding of how TIE algorithms operate and how to
avoid possible pitfalls of using off-the-shelf solutions.

## FAT Forensics (Software) ##
To support the goals of our hands-on tutorial, we employ
[`FAT Forensics`](https://fat-forensics.org/) -- an open source Python package
that can inspect selected fairness, accountability and **transparency** aspects
of data (and their features), *models* and *predictions*.
The toolbox spans all of the FAT domains because many of them share underlying
algorithmic components that can be reused in multiple different
implementations, often across the FAT borders.
This *interoperability* allows, for example, a counterfactual data point
generator to be used as a post-hoc explainer of black-box predictions on
one hand, and as an individual fairness (disparate treatment) inspection tool
on the other.
The *modular* architecture[^2][^4] enables
[`FAT Forensics`](https://fat-forensics.org/) to deliver robust and tested
low-level FAT building blocks as well as a collection of FAT tools built on top
of them.
Users can choose from these ready-made tools or, alternatively, combine the
available building blocks to create their own bespoke algorithms without the
need of modifying the code base.

&nbsp;&nbsp;&nbsp;The modular design of the toolbox also decouples an FAT tool
from its presentation medium, thus enabling two distinct "modes of operation".
In the *research mode* (data in -- visualisations out), the tool can be loaded
into an interactive Python session, e.g., a Jupyter Notebook, supporting rapid
prototyping and exploratory analysis.
This mode is intended for FAT researchers who can use it to propose new
fairness metrics, compare them with the existing ones or use them to inspect a
new system or data set.
The *deployment mode* (data in -- data out), on the other hand, can be used to
incorporate FAT functionality into a data processing pipeline to provide a
(numerical) analytics or become the foundation of any kind of automated
reporting and dashboarding.
This mode is intended for machine learning engineers and data scientists who
may use it to monitor or evaluate a predictive system during its development
and deployment.

&nbsp;&nbsp;&nbsp;[`FAT Forensics`](https://fat-forensics.org/) is published
under the BSD 3-Clause open source licence, which permits *commercial*
applications.
The toolbox has been built with the best software engineering practices in
mind to ensure its longevity, sustainability, extensibility and streamlined
maintenance.
The development workflow established around the package allows for its
adoption into new and existing projects, and provides an easy way for the
community to contribute novel FAT algorithms.
Finally, the documentation[^2] is carefully crafted to cater a wide range of
users and applications, and consists of:
* introductory [tutorials](https://fat-forensics.org/tutorials/index.html),
  which are narrative-driven and designed for new users who can benefit from
  step-by-step guidance;
* [how-to guides](https://fat-forensics.org/how_to/index.html) discussing
  specific use cases and applications; and
* [API documentation](https://fat-forensics.org/api.html) supported by minimal
  [code examples](https://fat-forensics.org/sphinx_gallery_auto/index.html),
  which can either be executed locally on a personal machine or remotely via
  [Binder](https://mybinder.org/v2/gh/fat-forensics/fat-forensics-doc/master?filepath=notebooks/sphinx_gallery_auto)
  (recommended) or
  [Google Colab](https://colab.research.google.com/github/fat-forensics/fat-forensics-doc/blob/master/)
  (the notebook browser is not very intuitive and an extra cell with the
  `!pip install fat-forensics[all]` command needs to be inserted at the top).

## Schedule and Resources ##
The tutorial lasts for 4 hours, including a 30-minute break.
The first part -- 1 hour and 15 minutes -- introduces popular transparency,
explainability and interpretability approaches.
It focuses on surrogate explainers of tabular data, discussing their pros, cons
and modularisation.
The next part -- 30 minutes in session and a 30-minute break -- presents
the software underpinning the tutorial.
It begins with a 15-minute introduction to
[`FAT Forensics`](https://fat-forensics.org/), which covers its algorithmic
design and available implementations.
The following 15 minutes are used to show participants how to set up the
package in preparation for the hands-on session.
It involves installing any dependencies as well as downloading required data
sets and Jupyter Notebooks for attendees who could not complete these tasks
beforehand.
Next, we take a 30-minute break during which we help participants to resolve
any technical difficulties and setup issues.
The final part -- 1 hour and 45 minutes -- is devoted to hands-on exercises:
* investigating predictions of black-box models by building bespoke surrogate
  explainers for tabular data;
* using surrogate-based feature importance and attribution methods; and
* achieving counterfactual transparency with tree-based surrogates.

*A more detailed outline of the tutorial is presented below.*

> **Tutorial slides, hands-on resources and a link to a Slack workspace via
  which we will provide help during the hands-on exercises will be listed in
  the itemised schedule below in early September.
  A link to the tutorial recording will be posted here in early October.**

### Part 1: Identifying Modules of Black-box Explainers ###
Introduction to *modular* machine learning transparency, explainability and
interpretability through a lens of surrogate explainers for tabular data -- 1
hour and 15 minutes in total.

| Duration | Activities | Instructor | Resources |
|:---------|:-----------|:-----------|:---------:|
| 2.00pm CEST<br>(15&nbsp;minutes) | *Background and motivation* of research on modular explainers. | Peter&nbsp;Flach | [**slides**]({{ "1.1-intro.pdf" | prepend: site.slides }}) |
| 2.15pm CEST<br>(60&nbsp;minutes) | *What and how of modular interpretability*: a case study of bespoke surrogate explainers for tabular data. | Kacper&nbsp;Sokol | [**slides**]({{ "1.2-surrogates.pdf" | prepend: site.slides }}) |

### Part 2: Getting to Know FAT Forensics ###
Introduction to hands-on machine learning interpretability with
[`FAT Forensics`](https://fat-forensics.org/) in preparation for the hands-on
exercises -- 30 minutes in session and a 30-minutes break.

<table>
  <thead>
    <tr>
      <th style="text-align: left">Duration</th>
      <th style="text-align: left">Activities</th>
      <th style="text-align: left">Instructor</th>
      <th style="text-align: center">Resources</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">3.15pm CEST<br>(15&nbsp;minutes)</td>
      <td style="text-align: left"><i>Introduction to open source interpretability tools</i> using the example of <code>FAT Forensics</code> &ndash; promises and perils of modular research software.</td>
      <td style="text-align: left">Alex&nbsp;Hepburn</td>
      <td style="text-align: center"><b><a href="{{ "2.1-software.pdf" | prepend: site.slides }}">slides</a></b></td>
    </tr>
    <tr>
      <td style="text-align: left">3.30pm CEST<br>(15&nbsp;minutes)</td>
      <td style="text-align: left"><i>Hands-on session preparation</i>. Setting up the package on a personal machine and experimenting with it online: My Binder and Google Colab. Overview of <code>FAT Forensics</code>&apos; API documentation, online tutorials and how-to guides.</td>
      <td style="text-align: left">Alex&nbsp;Hepburn</td>
      <td style="text-align: center"><b><a href="{{ site.notebooks }}">setup</a></b><br>&<br><b><a href="{{ "2.2-hands-on.pdf" | prepend: site.slides }}">slides</a></b></td>
    </tr>
    <tr>
      <td style="text-align: left">3.45pm CEST<br>(30&nbsp;minutes)</td>
      <td style="text-align: left"><i>Break</i>. (An opportunity to resolve any individual issues with the software setup encountered by participants.)</td>
      <td style="text-align: left">Kacper&nbsp;Sokol<br>&amp;&nbsp;Alex&nbsp;Hepburn</td>
      <td style="text-align: center"><a href="{{ site.slack }}"><b>Slack</b></a></td>
    </tr>
  </tbody>
</table>

### Part 3: Building Bespoke Surrogate Explainers (Hands-on) ###
Hands-on transparency with bespoke surrogate explainers for tabular data built
from interoperable algorithmic modules -- 1 hour and 45 minutes in total.

| Duration | Activities | Instructor | Resources |
|:---------|:-----------|:-----------|:---------:|
| 4.15pm CEST<br>(15&nbsp;minutes) | *Introduction to the hands-on resources* and overview of the Jupyter Notebooks. | Alex Hepburn | [**slides**]({{ "3.1-notebooks.pdf" | prepend: site.slides }}) |
| 4.30pm CEST<br>(80&nbsp;minutes) | *Active participation* facilitated by the instructors: **bring your own data**. Building bespoke surrogate explainers of black-box predictions for tabular data -- trade-offs associated with choosing particular algorithmic components when building surrogate explainers[^3]. | Kacper Sokol<br>&amp;&nbsp;Alex Hepburn | **[Jupyter<br>Notebooks]({{ site.notebooks }})**<br>&<br>[**Slack**]({{ site.slack }}) |
| 5.50pm CEST<br>(10&nbsp;minutes) | *Summary and farewell*. | Raul Santos-Rodriguez | [**slides**]({{ "3.3-summary.pdf" | prepend: site.slides }}) |

## Instructors ##

### Kacper Sokol ###
Kacper is a final-year PhD student and research associate at the University of
Bristol. His main research focus is transparency -- interpretability and
explainability -- of machine learning systems. In particular, he has done work
on enhancing transparency of logical predictive models (and their ensembles)
with counterfactual explanations. Kacper is the designer and lead developer of
the [`FAT Forensics`](https://fat-forensics.org/) package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: K.Sokol@bristol.ac.uk">K.Sokol@bristol.ac.uk</a></dd>
</dl>

### Alexander Hepburn ###
Alex is a third-year PhD student at the University of Bristol. His research is
based on including user-defined prior information in loss functions to improve
human perceptual systems and cost sensitive learning, mainly applied to deep
learning. Alex is a core developer of the
[`FAT Forensics`](https://fat-forensics.org/) package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: Alex.Hepburn@bristol.ac.uk">Alex.Hepburn@bristol.ac.uk</a></dd>
</dl>

### Raul Santos-Rodriguez ###

Raul is a Senior Lecturer in Data Science and Intelligent Systems in the
Department of Engineering Mathematics at the University of Bristol. His
research interests lie in data science, machine learning, artificial
intelligence and their applications to signal processing, particularly
healthcare, remote sensing and music information retrieval.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: enrsr@bristol.ac.uk">enrsr@bristol.ac.uk</a></dd>
</dl>

### Peter Flach ###
Peter is a Professor of Artificial Intelligence at the University of Bristol.
His research interests include mining highly structured data, the evaluation
and improvement of machine learning models, and human-centred AI. Peter
recently stepped down as Editor-in-Chief of the Machine Learning journal,
is President of the European Association for Data Science, and has
published several books including "Machine
Learning: The Art and Science of Algorithms that Make Sense of Data"
(Cambridge University Press, 2012).

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: Peter.Flach@bristol.ac.uk">Peter.Flach@bristol.ac.uk</a></dd>
</dl>

## References ##

[^1]: Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. 2016. "Why Should
      I Trust You?": Explaining the Predictions of Any Classifier. In
      Proceedings of the 22<sup>nd</sup> ACM SIGKDD International Conference on
      Knowledge Discovery and Data Mining. ACM, 1135–1144.
      <https://dl.acm.org/doi/10.1145/2939672.2939778>

[^2]: Kacper Sokol, Alexander Hepburn, Rafael Poyiadzi, Matthew Clifford,
      Raul Santos-Rodriguez, and Peter Flach. 2020. FAT Forensics: A Python
      Toolbox for Implementing and Deploying Fairness, Accountability and
      Transparency Algorithms in Predictive Systems. Journal of Open Source
      Software, 5(49), p.1904.
      <https://joss.theoj.org/papers/10.21105/joss.01904>

[^3]: Kacper Sokol, Alexander Hepburn, Raul Santos-Rodriguez, and
      Peter Flach. 2019. bLIMEy: Surrogate Prediction Explanations Beyond
      LIME. 2019 Workshop on Human-Centric Machine Learning (HCML 2019) at the
      33<sup>rd</sup> Conference on NeuralInformation Processing Systems
      (NeurIPS 2019), Vancouver, Canada (2019).
      <https://arxiv.org/abs/1910.13016>

[^4]: Kacper Sokol, Raul Santos-Rodriguez, and Peter Flach. 2019. FAT
      Forensics: A Python Toolbox for Algorithmic Fairness, Accountability and
      Transparency. arXiv preprint arXiv:1909.05167.
      <https://arxiv.org/abs/1909.05167>
