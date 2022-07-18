---
layout: custom
permalink: /2022_simons-institute

description: An interactive presentation for the AI and Humanity summer cluster workshop, discussing how machine learning explainers can help humans to understand automated decision-making

show_resources: true
slides: https://github.com/fat-forensics/events/tree/master/resources/2022_simons-institute/slides/
recordings: https://youtu.be/9z-9yngCcTA
---

# Where Does the Understanding Come From When Explaining Automated Decision-making Systems? #
{:.no_toc}

<table>
  <thead>
    <tr>
      <th style="text-align: left" colspan="2">An interactive presentation discussing how to interpret machine learning explanations for the <i><a href="https://simons.berkeley.edu/workshops/ai-and-humanity">AI and Humanity Summer Cluster Workshop</a></i>.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Where:</td>
      <td style="text-align: left">The Simons Institute for the Theory of Computing, UC Berkeley, California, US.</td>
    </tr>
    <tr>
      <td style="text-align: left">When:</td>
      <td style="text-align: left">11.15–11.45am on Thursday, July 14<sup>th</sup>, 2022.</td>
    </tr>
  </tbody>
</table>

## Table of Contents ##
{:.no_toc}

* TOC
{:toc}

## About the Presentation ##
A myriad of approaches exists to help us peer inside automated decision-making
systems based on artificial intelligence and machine learning algorithms.
These tools and their insights, however, are socio-technological constructs
themselves, hence subject to human biases and preferences as well as technical
limitations.
Under these conditions, how can we ensure that explanations are meaningful and
fulfil their role by leading to understanding?
In this talk I will demonstrate how different configurations of an
explainability algorithm may impact the resulting insights and show the
importance of the strategy employed to present them to the user, arguing in
favour of a clear separation between the technical and social aspects of such
tools.

## FAT Forensics (Software) ##
To support the goals of this demonstration, we employ
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
The *modular* architecture[^1][^2] enables
[`FAT Forensics`](https://fat-forensics.org/) to deliver robust and tested
low-level FAT building blocks as well as a collection of FAT tools built on top
of them.
Users can choose from these ready-made tools or, alternatively, combine the
available building blocks to create their own bespoke algorithms without the
need of modifying the code base.

## Resources ##
The [presentation]({{ page.slides }}) is provided as an interactive set of
slides utilising iPyWidgets and built with a Jupyter Notebook based on
[RISE](https://rise.readthedocs.io/) and [reveal.js](https://revealjs.com/).
This notebook (hence the presentation) can be executed locally on one's own
machine or launched directly in the web browser through Google Colab or
MyBidner.
The recording of the talk is available on [YouTube]({{ page.recordings }}).

| Resources                          |
|:-----------------------------------|
| [Slides]({{ page.slides }})        |
| [Recording]({{ page.recordings }}) |

## Instructors ##

### Kacper Sokol ###
Kacper is a research fellow with
[The ARC Centre of Excellence for Automated Decision-Making and Society (ADM+S)](https://www.admscentre.org.au/)
at the RMIT University.
His main research focus is transparency -- interpretability and
explainability -- of machine learning systems.
In particular, he has done work on enhancing transparency of logical predictive
models (and their ensembles) with counterfactual explanations.
Kacper is the designer and lead developer of the
[`FAT Forensics`](https://fat-forensics.org/) package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: Kacper.Sokol@rmit.edu.au">Kacper.Sokol@rmit.edu.au</a></dd>
</dl>

## References ##

[^1]: Kacper Sokol, Alexander Hepburn, Rafael Poyiadzi, Matthew Clifford,
      Raul Santos-Rodriguez, and Peter Flach. 2020. FAT Forensics: A Python
      Toolbox for Implementing and Deploying Fairness, Accountability and
      Transparency Algorithms in Predictive Systems. Journal of Open Source
      Software, 5(49), p.1904.
      <https://joss.theoj.org/papers/10.21105/joss.01904>

[^2]: Kacper Sokol, Raul Santos-Rodriguez, and Peter Flach. 2019. FAT
      Forensics: A Python Toolbox for Algorithmic Fairness, Accountability and
      Transparency. arXiv preprint arXiv:1909.05167.
      <https://arxiv.org/abs/1909.05167>
