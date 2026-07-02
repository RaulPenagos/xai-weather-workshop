# From SHAP to AIFS -- Explainable AI for Weather and Climate

*(working title; alternates under consideration: "Explaining the Black Box: From Penguins to Weather Models", "XAI in Geoscience: From Feature Importance to Adjoint Sensitivities")*

A 60-minute hands-on workshop introducing explainable AI (XAI) methods to a
geoscience audience, taught at the Climademics Summer School on 2026-07-03.
<!-- TODO: link the event's official page here once confirmed. -->

## Who this is for, and why

As AI models used in weather and climate applications grow more complex and
more skillful, their interpretability from a physical perspective tends to
decrease -- and in high-stakes settings such as natural hazard forecasting,
that opacity can erode trust and slow adoption. Explainable AI (XAI) methods
address this by giving domain experts a way to interrogate a model's
reasoning rather than accepting its output on faith (Dramsch et al., 2025,
*Nature Geoscience*). This workshop is built around a second, complementary
observation: much of the thinking behind XAI is not new to geoscientists.
Sensitivity and adjoint methods from numerical weather prediction (NWP) and
data assimilation transfer directly to modern gradient-based explainability
techniques. Part 1 builds a foundation in classic XAI methods -- most of
them model-agnostic -- on a deliberately simple tabular dataset. Part 2 applies that same thinking
to a state-of-the-art operational AI weather model, closing the loop back to
adjoint sensitivities that many NWP practitioners already know well. The
intended audience is climate, geoscience, and epidemiology researchers who
are comfortable with Python, pandas, and scikit-learn but do not need any
prior XAI background.

## Prerequisites

- Basic familiarity with Python, pandas, and scikit-learn (e.g. training a
  classifier, working with a DataFrame). No prior XAI experience is assumed.
- A Google account, if using Colab (recommended, see below).
- No account or install is required if using Binder instead.
- No GPU is required. Part 2 renders entirely from pre-committed artifacts by
  default; live model inference is optional and off unless explicitly
  enabled.

## Setup

**Colab is the primary path for the workshop** (see Prerequisites above) --
click the yellow badge for the notebook you want. The other badges are
optional convenience alternatives; most (Gradient, SageMaker Studio Lab,
Deepnote) need their own account, so **Binder remains the true no-account
fallback** if you don't have a Google account (see below).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jesperdramsch/xai-weather-workshop/HEAD)

**Part 1 -- Classic XAI (guided exercise):** `01_classic_xai.ipynb`
[![](https://img.shields.io/badge/view-notebook-orange)](01_classic_xai.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/jesperdramsch/xai-weather-workshop/blob/main/01_classic_xai.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jesperdramsch/xai-weather-workshop/HEAD?filepath=01_classic_xai.ipynb) [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/jesperdramsch/xai-weather-workshop/blob/main/01_classic_xai.ipynb) [![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/jesperdramsch/xai-weather-workshop/blob/main/01_classic_xai.ipynb) [![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fjesperdramsch%2Fxai-weather-workshop%2Fblob%2Fmain%2F01_classic_xai.ipynb)

**Part 1 solutions:** `solutions/01_classic_xai_solutions.ipynb`
[![](https://img.shields.io/badge/view-notebook-orange)](solutions/01_classic_xai_solutions.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jesperdramsch/xai-weather-workshop/HEAD?filepath=solutions/01_classic_xai_solutions.ipynb) [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) [![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) [![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fjesperdramsch%2Fxai-weather-workshop%2Fblob%2Fmain%2Fsolutions%2F01_classic_xai_solutions.ipynb)

**Part 2 -- AIFS sensitivities (instructor demo):** `02_aifs_sensitivities.ipynb`
[![](https://img.shields.io/badge/view-notebook-orange)](02_aifs_sensitivities.ipynb) [![](https://img.shields.io/badge/open-colab-yellow)](https://colab.research.google.com/github/jesperdramsch/xai-weather-workshop/blob/main/02_aifs_sensitivities.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jesperdramsch/xai-weather-workshop/HEAD?filepath=02_aifs_sensitivities.ipynb) [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/jesperdramsch/xai-weather-workshop/blob/main/02_aifs_sensitivities.ipynb) [![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/jesperdramsch/xai-weather-workshop/blob/main/02_aifs_sensitivities.ipynb) [![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)](https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fjesperdramsch%2Fxai-weather-workshop%2Fblob%2Fmain%2F02_aifs_sensitivities.ipynb)

Each notebook installs its own dependencies in the first cell (Colab/Binder/etc.), so any badge above gets you to a working environment without a local install.

### Binder details

Binder builds its environment from [`binder/requirements.txt`](binder/requirements.txt),
which mirrors the pinned dependencies in `pyproject.toml`. Startup can take a
few minutes on a cold build; if you don't have a Google account, launch this
ahead of the session rather than at the start.

### Local / uv

If you prefer to run locally with [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/jesperdramsch/xai-weather-workshop.git
cd xai-weather-workshop
uv sync
uv run jupyter lab
```

This uses the pinned dependency set in `pyproject.toml` (and `uv.lock` for a
fully reproducible environment).

## Repository layout

- `00_framing/` -- talk track and material for the opening framing
  discussion, drawn from Dramsch et al. (2025).
- `01_classic_xai.ipynb` -- Part 1: guided exercise on classic XAI methods
  (tree importance, permutation importance, PDP/ICE, SHAP) using the Palmer
  Penguins dataset.
- `02_aifs_sensitivities.ipynb` -- Part 2: instructor demo of backward
  (adjoint) sensitivities in ECMWF's AIFS weather model.
- `solutions/` -- worked solutions to the Part 1 exercises.
- `artifacts/` -- pre-rendered images and data used so Part 2 runs
  offline-first, without requiring live model inference.
- `facilitator_notes.md` -- timing, delivery notes, and tips for whoever
  teaches this session.
- `slides-outline.md` -- outline for accompanying slides.
- `handout.md` -- a leave-behind reference summarizing the methods covered.
- `extensions.md` -- pointers for what a longer (90-120 min) version of this
  session would add.
- `pyproject.toml` -- pinned Python dependencies (uv-compatible).
- `LICENSE` -- MIT license for this repository.
- `NOTICE` -- third-party attribution notices (see Licensing below).

## Licensing and attribution

This repository is released under the MIT License, Copyright (c) 2026
Jesper Dramsch (see [`LICENSE`](LICENSE)). It builds on and adapts material
from other sources, credited below and in [`NOTICE`](NOTICE).

**Part 1** adapts material from
[`ml-for-science-reproducibility-tutorial`](https://github.com/JesperDramsch/ml-for-science-reproducibility-tutorial)
("ml.recipes") by Jesper Dramsch, MIT License, Copyright (c) 2022 Jesper
Dramsch. Per that repository's `CITATION.cff`, both original authors should
be credited:

> Dramsch, J. S., & Maggio, V. (2022). *ML Recipes - Increase citations, ease
> review & foster collaboration* (Version PyData-Global-2022) [Computer
> software]. https://github.com/JesperDramsch/ml-for-science-reproducibility-tutorial
> Zenodo: https://doi.org/10.5281/zenodo.10381234

The Palmer Penguins dataset used throughout Part 1 is due to Dr. Kristen
Gorman and the Palmer Station, Antarctica Long Term Ecological Research
(LTER) Program. This workshop loads it via the
[`palmerpenguins`](https://pypi.org/project/palmerpenguins/) PyPI package by
Muhammad Chenariyan Nakhaee (MIT License).

**Part 2** adapts material from ECMWF's internal 2025 ML training course
(`ecmwf-training` organization on GitHub, notebook
`5-xAI-with-AIFS/explain_AIFS-cpu.ipynb`). That source repository has no
public `LICENSE` file; it is reused here with the direct authority of this
workshop's instructor, an ECMWF-affiliated contributor to that course, with
attribution to "ECMWF / ecmwf-training course materials". Two helper files
originating from that source, `perturbation.py` and `sensitivities.py`,
carry an Apache License 2.0 header (Copyright 2024 Anemoi contributors)
because they were originally copied from the
[`anemoi-inference`](https://github.com/ecmwf/anemoi-inference) package;
that header is preserved wherever those files appear.

**Framing** for the opening discussion is drawn from:

> Dramsch, J.S., Kuglitsch, M.M., Fernández-Torres, M.-Á., Toreti, A.,
> Albayrak, R.A., Nava, L., Ghaffarian, S., Cheng, X., Ma, J., Samek, W.,
> Venguswamy, R., Koul, A., Muthuregunathan, R. & Hrast Essenfelder, A.
> (2025). Explainability can foster trust in artificial intelligence in
> geoscience. *Nature Geoscience*.
> https://doi.org/10.1038/s41561-025-01639-x

See [`NOTICE`](NOTICE) for the consolidated third-party attribution notice.

## Code of Conduct

Participation in this workshop is governed by our
[Code of Conduct](./CODE_OF_CONDUCT.md). Please read it before attending or
contributing.

## How to cite this workshop

If you use or adapt material from this workshop, please cite it as:

> Dramsch, J. S. (2026). *From SHAP to AIFS -- Explainable AI for Weather and
> Climate* [Workshop materials]. Climademics Summer School.
> https://github.com/jesperdramsch/xai-weather-workshop

and, for the conceptual framing this workshop is built around, please also
cite Dramsch et al. (2025), *Nature Geoscience*,
https://doi.org/10.1038/s41561-025-01639-x.
