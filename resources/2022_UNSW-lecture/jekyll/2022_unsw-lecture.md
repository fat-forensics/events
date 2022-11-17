---
layout: custom
permalink: /2022_unsw-lecture

description: An invited lecture offering a high-level introduction to machine learning explainability, given for the Ethics in Computer Science (COMP4920/SENG4920 22T3) course at the University of New South Wales (UNSW), Sydney

show_resources: true
slides: https://github.com/fat-forensics/events/tree/master/resources/2022_UNSW-lecture/slides/
---

# Introduction to Machine Learning Explainability #
{:.no_toc}

<table>
  <thead>
    <tr>
      <th style="text-align: left" colspan="2">An invited lecture offering a high-level introduction to machine learning explainability, given for the <i>Ethics in Computer Science</i> (COMP4920/SENG4920 22T3) course at the <i>University of New South Wales</i> (UNSW), Sydney.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Where:</td>
      <td style="text-align: left">Central Lecture Block, University of New South Wales, Sydney, Australia.</td>
    </tr>
    <tr>
      <td style="text-align: left">When:</td>
      <td style="text-align: left">12.00–2.00pm on Wednesday, November 16<sup>th</sup>, 2022.</td>
    </tr>
  </tbody>
</table>

## Table of Contents ##
{:.no_toc}

* TOC
{:toc}

## About the Lecture ##
This lecture offers a high-level introduction to
machine learning explainability.
It covers topics such as:

- brief history of explainability;
- why we need explainability;
- important developments;
- taxonomy of explainable artificial intelligence;
- what is explainability;
- evaluating explainability;
- examples of explainability; and
- discussion of data explainability, transparent models and
  post-hoc explainability.

This overview is complemented by a case study of surrogate explainers.

## FAT Forensics (Software) ##
To support the goals of this lecture, I employ
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
need of modifying the codebase.

## Resources ##
The [presentation]({{ page.slides }}) is provided as a collection of
(interactive) slides based on [reveal.js](https://revealjs.com/).
The *Part I & II* slides are created with the
[reveal.js mode](https://quarto.org/docs/presentations/revealjs/) of
[Quarto](https://quarto.org/).
The *Case Study* slides are created with [RISE](https://rise.readthedocs.io/)
and offered as a
[MyST Notebook](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html)
-- a Jupyter Notebook written in Markdown -- with embedded iPyWidgets.
(See [this page]({{ page.slides }}) for build instructions.)
This notebook (hence the presentation) can be executed locally on one's own
machine or launched directly in the web browser through Google Colab or
MyBidner.

| [Resources]({{ page.slides }})     | Source | Rendered Version |
|:-----------------------------------|:--|:--|
| Slides                 | [Part I]({{ "intro.qmd" | prepend: page.slides }}) [Part II]({{ "intro_deux.qmd" | prepend: page.slides }}) | [![Slides Part 1](https://img.shields.io/badge/part-I-blue)](https://events.fat-forensics.org/_quarto/2022_UNSW-lecture/intro.html) [![Slides Part 2](https://img.shields.io/badge/part-II-blue)](https://events.fat-forensics.org/_quarto/2022_UNSW-lecture/intro_deux.html) |
| Interactive Case Study | [Surrogates]({{ "surrogates.md" | prepend: page.slides }}) | [![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fat-forensics/events/master?filepath=resources%2F2022_UNSW-lecture%2Fslides%2Fsurrogates.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fat-forensics/events/blob/master/resources/2022_UNSW-lecture/slides/surrogates.md) |

## Instructors ##

### Kacper Sokol ###
Kacper is a Research Fellow at the
[ARC Centre of Excellence for Automated Decision-Making and Society](https://www.admscentre.org.au/)
(ADM+S), affiliated with the School of Computing
Technologies at RMIT University, Australia;
and an Honorary Research Fellow at the Intelligent Systems Laboratory,
University of Bristol, United Kingdom.

His main research focus is transparency -- interpretability and explainability
-- of data-driven predictive systems based on artificial intelligence and
machine learning algorithms.
In particular, he has done work on enhancing transparency of predictive
models with *feasible and actionable counterfactual explanations* and
*robust modular surrogate explainers*.
He has also introduced *Explainability Fact Sheets* -- a comprehensive
taxonomy of AI and ML explainers -- and prototyped *Glass-Box* --
a dialogue-driven interactive explainability system.

Kacper is the designer and lead developer of *FAT Forensics* -- an open
source fairness, accountability and transparency Python toolkit.
Additionally, he is the main author of a collection of online interactive
*training materials about machine learning explainability*, created in
collaboration with the Alan Turing Institute -- the UK's national institute
for data science and artificial intelligence.

Kacper holds a Master's degree in Mathematics and Computer Science, and a
doctorate in Computer Science from the University of Bristol, United Kingdom.
Prior to joining ADM+S he has held numerous research positions at the
University of Bristol, working with projects such as REFrAMe, SPHERE and
TAILOR -- European Union's AI Research Excellence Centre.
Additionally, he was a visiting researcher at the
University of Tartu (Estonia);
Simons Institute for the Theory of Computing, UC Berkeley (California, USA);
and USI -- Università della Svizzera italiana (Lugano, Switzerland).
In his research, Kacper collaborated with numerous industry partners,
such as THALES, and provided consulting on explainable artificial
intelligence and transparent machine learning.

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

[^2]: Kacper Sokol, Raul Santos-Rodriguez, and Peter Flach. 2022. FAT
      Forensics: A Python Toolbox for Algorithmic Fairness, Accountability and
      Transparency. Software Impacts, 14, p.100406.
      <https://doi.org/10.1016/j.simpa.2022.100406>
