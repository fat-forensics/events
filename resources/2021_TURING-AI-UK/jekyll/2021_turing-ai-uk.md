---
layout: custom
permalink: /2021_turing-ai-uk

description: An interactive demonstration of machine learning explainers for The Alan Turing Institute's AI UK 2021

show_resources: true
notebooks: https://github.com/fat-forensics/resources/tree/master/surrogates_overview/
slides: https://github.com/fat-forensics/events/tree/master/resources/2021_AI-UK/slides/
recordings: https://youtu.be/pAeb0y1v2lo?t=2069
---

# Did You Get That? #
{:.no_toc}

## Reviewing Intelligibility of State-of-the-art Machine Learning Explanations ##
{:.no_toc}

<table>
  <thead>
    <tr>
      <th style="text-align: left" colspan="2">An interactive demonstration of machine learning explainers for <i><a href="https://www.turing.ac.uk/ai-uk/demos">The Alan Turing Institute's AI UK 2021</a></i>.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Where:</td>
      <td style="text-align: left">Zoom, The Alan Turing Institute, London, UK.</td>
    </tr>
    <tr>
      <td style="text-align: left">When:</td>
      <td style="text-align: left">11.00–11.15am on Wednesday, March 24<sup>th</sup>, 2021.</td>
    </tr>
  </tbody>
</table>

## Table of Contents ##
{:.no_toc}

* TOC
{:toc}

## About the Demonstration ##
To better understand data-driven predictive models and their decisions, the
artificial intelligence and machine learning communities are developing
dedicated transparency and explainability methods.
While such techniques tend to provide appealing insights, their provenance and
correctness are rarely ever assessed.
In this session I demonstrate how distinct -- and sometimes contradictory --
explanations can be generated with one explainability approach for a single
black-box prediction.
I show how simple changes to the parameterisation of explainability methods
can yield such disparate results[^2].
This observation suggests that each application may require a bespoke explainer
built and tuned for the problem at hand.
Moreover, understanding these dependencies helps with designing robust and
trustworthy explainers, whose insights can be relied upon.

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
Additionally, an independent [Jupyter Notebook]({{ page.notebooks }}) with
all of the interactive widgets is available to facilitate hands-on
experimentation with the explainers introduced during the demonstration.
These notebooks (hence the presentation) can be executed locally on one's own
machine or launched directly in the web browser through Google Colab or
MyBidner.
The recording of the demonstration session is available on
[YouTube]({{ page.recordings }}).

| Resources                          |
|:-----------------------------------|
| [Slides]({{ page.slides }})        |
| [Notebook]({{ page.notebooks }})   |
| [Recording]({{ page.recordings }}) |

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
