---
layout: custom
---

# What and How of Machine Learning Transparency #
### Building Bespoke Explainability Tools with Interoperable Algorithmic Components ###
A hands-on tutorial to be held at the
[ECML-PKDD 2020](https://ecmlpkdd2020.net/) conference in Ghent, Belgium, from
the 14<sup>th</sup> to the 18<sup>th</sup> of September 2020.

## About the Tutorial ##
In this hands-on tutorial we will introduce popular transparency,
interpretability and explainability tools; explain their strengths and
weaknesses; demonstrate how to identify their interoperable
*algorithmic components*; and decompose them into these atomic functional
blocks. We will then teach participants how to improve upon off-the-shelf
solutions by taking advantage of this modularity and building a suite of
bespoke transparency forensic tools for a predictive pipeline: data (both raw
and features), models and predictions. This effort will be grounded with a
theoretical introduction followed by interactive coding exercises, supporting
two distinct goals: research & development, and deployment of such tools. The
major hands-on part of the tutorial will therefore walk the attendees through
*building* and *validating* their own *transparency tools*, for example,
composing a custom surrogate explainer and adjusting a counterfactual data
point generator for black-box predictions. To this end, we will use
[`FAT Forensics`](https://fat-forensics.org/) -- a Python toolbox open-sourced
under the BSD 3-Clause license and designed to inspect fairness, accountability
and transparency (FAT) of all components of a predictive pipeline.

---

**More details and hands-on materials needed to participate in the tutorial
will be posted here closer to the tutorial date.**

## Tutorial Description ##
Many public-domain implementations of transparency, interpretability and
explainability (TIE) algorithms are a result of academic research projects.
Development of such tools usually starts from a particular research goal, such
as demonstrating the capabilities of a proposed method. In practice this often
means that the software is developed without an elaborate design, which affects
its reusability and modularity. The resulting tool may be easy to use for
non-experts, who can customise it with parameters exposed via an accessible
application programming interface (API), which hides all of the complexity from
the user. However, more advanced users such as researchers and developers, who
want to build on top of such implementations or deploy them in a custom system,
may need to resort to tinkering with the source code, which can be frustrating
and time consuming. Designing a strictly modular transparency tool may be
desirable, but comes at the expense of a more complex design and API that may
not be suitable for a lay audience.

In this tutorial we address these challenges and provide participants with
knowledge and hands-on skills to identify base building blocks of popular TIE
approaches, understand the transparency requirements of one's use case and
fulfil them by building a bespoke TIE algorithm that improves upon
off-the-shelf solutions. To this end, we show how a modular software design --
gathering all of the reusable TIE algorithmic components in a single software
package under a standardised API -- combines the best of both worlds and caters
to technical and non-technical users alike. By providing a user-ready API for
algorithmic TIE building blocks we deliver a collection of tools that can be
used by technical users -- researchers and developers -- to create their own
bespoke TIE algorithms. We also use these to provide popular and easy to use
TIE algorithms as part of the API targeted at a lay audience. This modular
design is embodied in an open source Python software package, which we released
to improve and advance reproducibility of TIE algorithms and provide
straightforward access to their vital components.

Attendees from academia will gain experience in experimenting with the design
and building blocks of state-of-the-art explainers -- something which is
uncommon among other educational resources in this space that simply show how
to apply such tools. Attendees from industry will learn to build, tune and
deploy bespoke explainers of black-box machine learning models to meet their
business needs, hence extract important insights for relevant stakeholders. The
tutorial will also briefly cover best practices of software engineering for
machine learning and benefits of modular design, which both contribute to
sustainable research in the field. Our hands-on approach will provide
participants with first-hand experience, leading to a better understanding of
how transparency tools operate and how to avoid possible pitfalls of using
off-the-shelf algorithms.

## Resources ##
To support the goals of our hands-on tutorial, we employ `FAT Forensics` -- an
open source Python package that can inspect selected fairness, accountability
and **transparency** (FAT) aspects of all components of a predictive pipeline:
*data* (and their features), *models* and *predictions*. The toolbox spans all
of the FAT domains because many of them share algorithmic components that can
be reused in multiple different implementations often across the FAT borders.
This *interoperability* allows, for example, a counterfactual data point
generator to be used as a post-hoc interpretability approach for predictions on
one hand, and as an individual fairness (disparate treatment) inspection tool
on the other. The *modular* architecture[^2][^4] enables the toolbox to deliver
robust and tested low-level FAT building blocks, as well as a collection of FAT
tools built on top of this. Users can employ these pre-built tools or
alternatively combine the available building blocks to create their own bespoke
algorithms without the need of modifying the code base.

The modular design of the toolbox decouples an FAT tool from its presentation
medium and enables two distinct "modes of operation". In the *research mode*
(data in -- visualisations out) the tool can be loaded into an interactive
Python session, e.g., a Jupyter Notebook, supporting rapid prototyping and
exploratory analysis. This mode is intended for FAT researchers who can use it
to propose new fairness metrics, compare them with the existing ones or use
them to inspect a new system or a data set. The *deployment mode* (data in --
data out) can be used to incorporate the toolbox into a data processing
pipeline to provide a (numerical) FAT analytics, and supports any kind of
automated reporting or dashboarding. This mode is intended for machine learning
engineers and data scientists who may use it to monitor or evaluate a
predictive system during development and deployment.

`FAT Forensics` is published under the BSD 3-Clause open source licence,
thereby allowing *commercial* applications. The toolbox has been developed with
the best software engineering practices in mind, ensuring its long-term
maintainability, sustainability and extensibility. The software engineering
work-flow established around the toolbox allows for its adoption into new and
existing projects, and provides an easy way for the community to contribute
novel FAT algorithms. The documentation[^2] is carefully crafted to cater a
wide range of users and consists of:

* introductory [tutorials](https://fat-forensics.org/tutorials/index.html),
  which are narrative-driven and designed for new users who need step-by-step
  guidance,
* [how-to guides](https://fat-forensics.org/how_to/index.html) and
* [API documentation](https://fat-forensics.org/api.html) supported by
  [code examples](https://fat-forensics.org/sphinx_gallery_auto/index.html),
  which can either be executed locally on your machine or remotely via
  [Binder](https://mybinder.org/v2/gh/fat-forensics/fat-forensics-doc/master?filepath=notebooks/sphinx_gallery_auto)
  or Google Colab.

---

**More materials geared towards the hands-on sessions of the tutorial will be
published here closer to the tutorial date.**

## Schedule (tentative) ##
The tutorial is 4-hour long, including a 30-minute break.
The first hour will be an introduction to popular transparency, explainability
and interpretability approaches discussing their pros, cons and modularisation.
It will be followed by a 15-minute introduction to `FAT Forensics` discussing
its algorithmic design and available implementations. The following 15 minutes
will be used to show participants how to set up the package in preparation for
the hands-on session; it will involve installing any dependencies and
downloading required data sets for attendees who could not complete that
beforehand. Next, we plan a 30-minute break during which we will help
participants to resolve any setup issues. The following 2 hours will be devoted
to hands-on exercises:

* investigating predictions of black-box models with surrogate explainers,
* achieving counterfactual transparency, and
* using feature importance and attribution methods.

A more detailed outline of the tutorial is presented below.

### Part 1 ###
Introduction to machine learning transparency, explainability and
interpretability for data, models and predictions -- 1 hour in total.

| Duration   | Activities                                      | Instructor   |
|:-----------|:------------------------------------------------|:-------------|
| 10 minutes | Background and motivation of this line of research. | Peter Flach  |
| 10 minutes | Feature attribution and importance metrics for understanding black-box model behaviour, e.g., partial dependence, individual conditional expectation and Shapley values. | Kacper Sokol |
| 10 minutes | Customisable counterfactual explanations of black-box predictions. | Kacper Sokol |
| 30 minutes | Surrogate explanations of black-box predictions for tabular, text and image data. | Alex Hepburn |

### Part 2 ###
Introduction to hands-on ML transparency -- 30 minutes in session and 30
minutes break.

<table>
  <thead>
    <tr>
      <th style="text-align: left">Duration</th>
      <th style="text-align: left">Activities</th>
      <th style="text-align: left">Instructor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">15 minutes</td>
      <td style="text-align: left">Introduction to open source transparency tools, focusing on <code>FAT Forensics</code>.<br>
                                  <ul>
                                    <li>Promises and perils of modular research software; an overview of modular algorithmic transparency implementations.</li>
                                    <li>The origin of <code>FAT Forensics</code>: challenges and opportunities.</li>
                                    <li><code>FAT Forensics</code>&apos; breadth, scope and two modes of operation: research and deployment. The first mode will be discussed in detail during the hands-on part of the tutorial and the latter will only be introduced using an example of a dashboard built with the toolbox.</li>
                                    <li>Current state and the future of the toolbox.</li>
                                    <li>Extra learning resources &ndash; <code>FAT Forensics</code>&apos; documentation.</li>
                                  </ul></td>
      <td style="text-align: left">Kacper Sokol</td>
    </tr>
    <tr>
      <td style="text-align: left">15 minutes</td>
      <td style="text-align: left">Hands-on session preparation.<br>
                                   <ul>
                                     <li>Setting up the package on a personal machine.</li>
                                     <li>Experimenting with the package online: My Binder and Google Colab.</li>
                                     <li>Testing the installation and executing an example notebook.</li>
                                     <li>Introduction to <code>FAT Forensics</code>&apos; API documentation, online tutorials and how-to guides.</li>
                                   </ul></td>
      <td style="text-align: left">Alex Hepburn</td>
    </tr>
    <tr>
      <td style="text-align: left">30 minutes</td>
      <td style="text-align: left">Break. We will use this time to help resolve any individual issues with the software setup.</td>
      <td style="text-align: left">Kacper Sokol and Alex Hepburn</td>
    </tr>
  </tbody>
</table>

### Part 3 ###
Hands-on algorithmic transparency for ML -- 2 hours in total.

| Duration   | Activities                                      | Instructor   |
|:-----------|:------------------------------------------------|:-------------|
| 60 minutes | Building bespoke black-box prediction explainers with surrogates. This part will teach participants about trade-offs associated with choices of particular algorithmic components when building surrogate explainers[^1] for image, text and tabular data[^3]. | Alex Hepburn |
| 30 minutes | Interactive prediction transparency with counterfactual explanations validated via a density score. This part will teach participants how to generate counterfactual explanations tailored to an end user by imposing restrictions and requirements on the counterfactual search. It will also convey the importance of data density when assessing the feasibility of a counterfactual explanation and show participants how to achieve that in practice. | Kacper Sokol |
| 30 minutes | Generating and validating feature importance and attribution measures to assess transparency and accountability of black-box models and their predictions. This part will teach participants how to generate, interpret and tune partial dependence, individual conditional expectation and Shapley values to achieve robust transparency measures of a predictive black-box model. | Kacper Sokol |

## Instructors ##

### Kacper Sokol ###
Kacper is a final-year PhD student and research associate at the University of
Bristol. His main research focus is transparency -- interpretability and
explainability -- of machine learning systems. In particular he has done work
on enhancing transparency of logical predictive models (and their ensembles)
with counterfactual explanations. Kacper is the designer and lead developer of
the `FAT Forensics` package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: K.Sokol@bristol.ac.uk">K.Sokol@bristol.ac.uk</a></dd>
</dl>

### Alexander Hepburn ###
Alex is a third-year PhD student at the University of Bristol. His research is
based on including user-defined prior information in loss functions to improve
human perceptual systems and cost sensitive learning, mainly applied to deep
learning. Alex is a core developer of the `FAT Forensics` package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: Alex.Hepburn@bristol.ac.uk">Alex.Hepburn@bristol.ac.uk</a></dd>
</dl>

### Peter Flach ###
Peter is a Professor of Artificial Intelligence at the University of Bristol.
His research interests include mining highly structured data, the evaluation
and improvement of machine learning models, and human-centred AI. Peter is
Editor-in-Chief of the Machine Learning journal, President of the European
Association for Data Science, and author of several books including "Machine
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

[^2]: Kacper Sokol, Alexander Hepburn, Rafael Poyiadzi, Matthew Clifford,
      Raul Santos-Rodriguez, and Peter Flach. FAT Forensics: A Python Toolbox
      for Implementing and Deploying Fairness, Accountability and Transparency
      Algorithms in Predictive Systems. (To appear.) Journal of Open Source
      Software. <https://github.com/openjournals/joss-reviews/issues/1904>

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
