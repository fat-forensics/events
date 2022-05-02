---
layout: custom
permalink: /2021_adms

description: An overview of machine learning explainability for the ADM+S Machines Programme

show_resources: true
slides: https://github.com/fat-forensics/events/tree/master/resources/2021_ADMS/slides/
---

# Making Machine Learning Explanations Truthful and Intelligible #
{:.no_toc}

<table>
  <thead>
    <tr>
      <th style="text-align: left" colspan="2">An interactive overview of machine learning explainability with focus on robustness of surrogate explainers for image and tabular data for the <i>Machines Programme</i> of the <i><a href="https://www.admscentre.org.au/">ARC Centre of Excellence for Automated Decision-Making and Society</a></i> (ADM+S).</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Where:</td>
      <td style="text-align: left">(MS Teams) ADM+S Centre, RMIT University, Melbourne, Victoria, Australia.</td>
    </tr>
    <tr>
      <td style="text-align: left">When:</td>
      <td style="text-align: left">3.30–4.30pm (AEST) on Friday, August 13<sup>th</sup>, 2021.</td>
    </tr>
  </tbody>
</table>

## Table of Contents ##
{:.no_toc}

* TOC
{:toc}

## About the Invited Talk ##
Surrogate explainability is a popular transparency technique for assessing
trustworthiness of predictions output by black-box machine learning models.
While such explainers are often presented as monolithic, end-to-end tools,
they in fact exhibit high modularity and scope for parameterisation[^2].
This observation suggests that each use case may require a bespoke surrogate
built and tuned for the problem at hand.
This talk provides an introduction to interpretable machine learning and
explainable artificial intelligence, and overviews the influence of
parameterisation and configuration of surrogates on the explanations that they
generate for tabular and image data.
In particular, it discusses the influence of segmentation granularity and
super-pixel occlusion colour for images, as well as discretisation and
binarisation of continuous features for tabular data.
Understanding these dependencies helps with building robust and trustworthy
surrogate explainers, whose insights can be relied upon.

## FAT Forensics (Software) ##
To support the goals of this invited talk, we employ
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
The *modular* architecture[^1][^3] enables
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

| Resources                   |
|:----------------------------|
| [Slides]({{ page.slides }}) |

## Instructors ##

### Kacper Sokol ###
Kacper is a research associate with the TAILOR project at
the University of Bristol.
His main research focus is transparency -- interpretability and
explainability -- of machine learning systems.
In particular, he has done work on enhancing transparency of logical predictive
models (and their ensembles) with counterfactual explanations.
Kacper is the designer and lead developer of the
[`FAT Forensics`](https://fat-forensics.org/) package.

<dl>
  <dt>Contact</dt>
  <dd><a href="mailto: K.Sokol@bristol.ac.uk">K.Sokol@bristol.ac.uk</a></dd>
</dl>

## References ##

[^1]: Kacper Sokol, Alexander Hepburn, Rafael Poyiadzi, Matthew Clifford,
      Raul Santos-Rodriguez, and Peter Flach. 2020. FAT Forensics: A Python
      Toolbox for Implementing and Deploying Fairness, Accountability and
      Transparency Algorithms in Predictive Systems. Journal of Open Source
      Software, 5(49), p.1904.
      <https://joss.theoj.org/papers/10.21105/joss.01904>

[^2]: Kacper Sokol, Alexander Hepburn, Raul Santos-Rodriguez, and
      Peter Flach. 2019. bLIMEy: Surrogate Prediction Explanations Beyond
      LIME. 2019 Workshop on Human-Centric Machine Learning (HCML 2019) at the
      33<sup>rd</sup> Conference on NeuralInformation Processing Systems
      (NeurIPS 2019), Vancouver, Canada (2019).
      <https://arxiv.org/abs/1910.13016>

[^3]: Kacper Sokol, Raul Santos-Rodriguez, and Peter Flach. 2019. FAT
      Forensics: A Python Toolbox for Algorithmic Fairness, Accountability and
      Transparency. arXiv preprint arXiv:1909.05167.
      <https://arxiv.org/abs/1909.05167>
