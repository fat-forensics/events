|           |          |
| --------  | -------- |
| Slides | [![Slides Part 1](https://img.shields.io/badge/part-I-blue)](https://events.fat-forensics.org/_quarto/2022_UNSW-lecture/intro.html) [![Slides Part 2](https://img.shields.io/badge/part-II-blue)](https://events.fat-forensics.org/_quarto/2022_UNSW-lecture/intro_deux.html) |
| Interactive Case Study | [![Open in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fat-forensics/events/master?filepath=resources%2F2022_UNSW-lecture%2Fslides%2Fsurrogates.md) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fat-forensics/events/blob/master/resources/2022_UNSW-lecture/slides/surrogates.md) |
| Licence | [![new BSD](https://img.shields.io/github/license/fat-forensics/events.svg)](https://github.com/fat-forensics/events/blob/master/LICENCE) |

# Slides (2022 Invited Lecture, UNSW) #

*Introduction to Machine Learning Explainability* slides used for
an invited lecture given for the *Ethics in Computer Science*
(COMP4920/SENG4920 22T3) course at the
*University of New South Wales* (UNSW), Sydney.

| Slides                             | Description            |
|:-----------------------------------|:-----------------------|
| [`intro.qmd`](intro.qmd)           | Part I                 |
| [`intro_deux.qmd`](intro_deux.qmd) | Part II                |
| [`surrogates.md`](surrogates.md)   | Interactive Case Study |

---

The *Part I & II* slides are created with the
[reveal.js][revealjs-quarto] mode of [Quarto][quarto].
To build them you need to install Quarto and run
`quarto render`, e.g., `quarto render intro.qmd`.

The *Case Study* slides are created with [RISE][rise] and
offered as a [MyST Notebook][myst] -- a Jupyter Notebook written in
Markdown.
It can be converted to or opened with Jupyter Notebook by using
[jupytext][jupytext].
To launch the slideshow (based on the [reveal.js][revealjs]
framework) install the dependencies (`pip install -r requirements.txt`) and
open the notebook within a Jupyter Notebook environment (not Jupyter Lab);
next:

1. execute all cells, and
2. launch RISE presentation by clicking the bar chart icon
   (<img src="../../../assets/images/barchart.svg" width=20px />) shown in the
   Jupyter Notebook toolbar.

> A pre-built version of the slides can be accessed with the buttons
> displayed at the top of the page.
> The case study can be launched with Binder or Colab in the same
> way.

More details are available on
<https://events.fat-forensics.org/2022_unsw-lecture>.

[quarto]: https://quarto.org/
[rise]: https://rise.readthedocs.io/
[revealjs]: https://revealjs.com/
[revealjs-quarto]: https://quarto.org/docs/presentations/revealjs/
[myst]: https://jupyterbook.org/en/stable/file-types/myst-notebooks.html
[jupytext]: https://jupytext.readthedocs.io/
