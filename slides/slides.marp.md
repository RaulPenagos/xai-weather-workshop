---
marp: true
theme: dramsch
paginate: true
_paginate: false
title: XAI in Geoscience -- From Feature Importance to Adjoint Sensitivities
header: Climademics Summer School · 2026-07-03
footer: Jesper Dramsch · ECMWF
---

<!-- _class: invert lead -->

# XAI in Geoscience:<br/>From Feature Importance to Adjoint Sensitivities <!--fit-->

Jesper Dramsch (they/them) · ECMWF
Climademics Summer School, 2026-07-03

Part 1: hands-on (Colab) · Part 2: instructor demo

---

## Why explainability, why now

-   AI model complexity and predictive skill keep going up -- physical interpretability tends to go down
-   In high-stakes settings (natural hazards) that erodes trust -- and slows adoption
-   XAI: methods that reveal the AI's decision process, to rebuild that trust

---

## What XAI actually gives you

-   An explanation that "justifies its recommendation, decision, or action"
-   A **magnifying lens** -- see the data through the model's "eyes"
-   Detects spurious correlations / data issues before they cause harm
-   Can motivate new science (e.g. landslide susceptibility, drought index studies)

---

## The adoption gap (the numbers)

-   2.3M arXiv abstracts (2007–2022) screened; 12,429 geoscience abstracts analysed in full text
-   25.5% of geoscience papers reference AI -- only 6.1% reference XAI
-   Gap has stayed roughly flat 2007–2022, no clear upward trend
-   XAI mentions cluster in geoinformatics/remote sensing and geophysics (seismology, volcanology)

---

## Why the gap exists (researcher survey)

-   Motivations to use XAI: trust, insight into data/model issues, efficiency, discovery of physical processes
-   Source: ITU/WMO/UN Environment Focus Group on AI for Natural Disaster Management
-   Non-adopters mostly cite lack of time/effort/resources -- not lack of perceived value
-   Almost all non-adopters plan to apply XAI eventually

---

## Framing question: where / when / what

-   Three lenses: Space ("where"), Time ("when"), Feature ("what")
-   Natural hazards: "Where should we anticipate tornadoes?" / "How early can a volcanic eruption be predicted?" / "What determines flood susceptibility?"
-   Intersections: "Where **and** when should we expect landslides?" / "Where does low humidity contribute to wildfires?"
-   Preview: Part 1 mostly answers "what" (feature importance); Part 2 answers "where" (maps) and "when" (lead time)

---

## Challenges

-   Most XAI historically built for image data; geospatial/spatiotemporal data behaves differently
-   Need for object/concept-level explanations, not just pixel attribution
-   Pixel/feature attribution is often still not interpretable by non-specialists in physical terms
-   Relevance, accuracy and reliability of XAI methods for geoscience remain open questions

---

## Four recommendations

-   **Demand**: funders, reviewers, end-users should explicitly ask for interpretable/transparent approaches
-   **Resources**: understand method mechanics/limits, read library docs carefully, benchmark black boxes quantitatively
-   **Partnerships**: e.g. UN Global Initiative on Resilience to Natural Hazards through AI, EU Climate Intelligence project
-   **Integration**: streamlined, standardized, interoperable workflows build trust at scale

---

## This workshop is "Resources" in action

-   We apply XAI methods hands-on -- their mechanics, and where they mislead
-   Today's arc: classic tabular XAI (Part 1) → state-of-the-art operational AI weather model (Part 2)
-   Core message: domain expertise you already have (adjoint thinking, sensitivity analysis) transfers directly
-   Dramsch et al. (2025), *Nature Geoscience*, doi.org/10.1038/s41561-025-01639-x

---

<!-- _class: invert lead -->

# Part 1: Classic XAI <!--fit-->

From Penguins to Pitfalls

---

## Part 1 roadmap

-   Notebook: `01_classic_xai.ipynb` -- self-contained, runs on Colab's free CPU tier
-   Dataset: Palmer Penguins (species classification from bill/flipper/mass/sex/island)
-   Models trained inline: `RandomForestClassifier` and `SVC`
-   Arc per method: question it answers → worked example → where it misleads you

---

## Data + models (participants run cells)

-   Load via `palmerpenguins` package (fallback: `sns.load_dataset('penguins')`)
-   Quick EDA: species/island/sex distributions, colorblind-safe palette (viridis/cmocean)
-   Train/test split, fit RF + SVM
-   Baseline accuracy check before any explanation method is introduced

---

## Method 1: Tree (impurity) importance

-   **Question it answers**: which features did the trees split on, weighted by impurity reduction?
-   **Worked example**: RF impurity importance on penguins -- the classic `Sex` → one-hot `Female`/`Male` split artifact, fixed here via `get_feature_names_out()`
-   **Where it misleads you**: biased toward high-cardinality / correlated features -- fast, but not trustworthy alone

---

## Exercise 1

-   Add a random-noise feature to the training data
-   Re-run tree impurity importance with the noise feature included
-   Task: explain why pure noise gets nonzero importance
-   Discuss: what does this imply about trusting impurity importance alone?

---

## Method 2: Permutation importance

-   **Question it answers**: how much does shuffling one feature degrade model performance? (model-agnostic)
-   **Worked example**: grouped boxplot -- RF vs SVM, train vs test, uncertainty via `n_repeats`
-   **Where it misleads you**: correlated features share/dilute importance; train/test agreement is itself a diagnostic

---

## Exercise 2

-   Repeat the noise-feature experiment with permutation importance, on both RF and SVM
-   Task: does the noise feature show up now?
-   Task: explain the disagreement with Exercise 1's tree-importance result
-   Discuss: which method would you trust more, and why?

---

## Method 3: PDP / ICE

-   **Question it answers**: how does the prediction change as one feature varies -- on average (PDP) and per-instance (ICE)?
-   **Worked example**: average response curves (PDP) plus individual curves (ICE) for a bill/culmen feature
-   **Where it misleads you**: averaging (PDP) hides interactions; curves extrapolate into empty/sparse regions of feature space

---

## Exercise 3

-   Add ICE curves for a bill/culmen-depth feature
-   Task: find an individual penguin whose ICE curve diverges from the average PDP
-   Discuss: what does that divergence tell you about feature interactions?

---

## Method 4: SHAP

-   **Question it answers**: how much did each feature push this prediction from the baseline (local), and what matters globally (beeswarm)?
-   **Worked example**: `shap.plots.waterfall` + `shap.plots.beeswarm` -- modern matplotlib-native API, replacing the broken JS `force_plot`/`initjs()`
-   **Where it misleads you**: explaining the model is not explaining the world -- e.g. `Sex` may be a proxy/confound, not a causal driver

---

## Exercise 4

-   Compare SHAP's global feature ranking to permutation importance's ranking
-   Task: where do the two rankings disagree, and why?
-   Discuss: correlation vs causation -- what would you need to claim a causal driver?

---

<!-- _class: invert lead -->

# Part 2: AIFS Backward Sensitivities <!--fit-->

An instructor demo

---

## The experiment setup

-   Model: AIFS (ECMWF's AI Forecasting System), O48-resolution checkpoint, 6-hour lead time
-   Perturbation: unit nudge to 2m temperature (`2t`), all grid points within 350 km of (40°N, 120°E) -- Bohai Sea / China coast
-   Method: backward sensitivities via `torch.autograd.functional.vjp` -- reverse-mode automatic differentiation (adjoint / vector-Jacobian product)
-   Goal: which input variables / locations / levels most influenced that `2t` forecast?

---

## How does this actually work?

-   Forward pass: initial state → AIFS → forecast (an ordinary run)
-   Backward pass: perturbation → reverse-mode autodiff → sensitivity map
-   This is differentiating **through** the network, not querying it from outside
-   The same operation as an adjoint model's gradient in 4D-Var

---

## Live demo: hand-differentiate this network

-   A real feedforward net: 2 inputs → 4 tanh hidden units → 1 output
-   **Act 1 (forward)**: drag `x1`/`x2`, watch `y` respond; the sensitivity bar chart rides along as a preview
-   **Act 2 (backward)**: fixed at that same point, one slider only -- `output perturbation v` (the same `v` AIFS's code sets to 1.0)
-   `x1`, `x2`, `y` never move in Act 2 -- only the halo around `y`, sized by `|v|`, represents `v` itself
-   Drag `v`: every edge and bar scales proportionally -- a backward pass is linear in `v`

---

## Artifact: pressure-level summary

![bg right:40%](../artifacts/images/01_pressure_level_summary.png)

-   Grid of heatmaps: rows = input hour offset (-6H / 0H), columns = min/max stat
-   Shows which pressure-level variables/levels have the largest-magnitude sensitivities overall
-   Purpose: overview before drilling into specific spatial maps

---

## Live demo: the interactive map

-   `2t` (self-check): does the model's own explanation make physical sense? -- signal sits right on the perturbation point
-   `z_500`: a paired +/- structure spanning a wide area -- a surface perturbation reaching into upper-air dynamics
-   Structurally different signals, both physically sensible

---

## Artifact: temperature cross-section

![bg left:40%](../artifacts/images/05_cross_section_temperature.png)

-   Longitude vs. pressure-level cross-section of temperature (`t`) sensitivity along 40.5°N
-   Slice passes directly through the perturbation point
-   Shows vertical structure: boundary layer vs. free troposphere

---

## Live demo: vertical profile & flythrough

-   Vertical profile: sensitivity by pressure level at the grid point closest to the perturbation -- normalised per variable
-   A single grid point is noisy -- that's expected, the same caution as SHAP explaining one prediction
-   Flythrough: animated across all 13 levels on a fixed colour scale

---

<!-- _class: invert lead -->

# Bridge back <!--fit-->

You already know this

---

## You already know this

-   Permutation importance, PDP/ICE, SHAP: **perturbation-based**, model-agnostic -- probe the model, treat it as a black box
-   Backward/adjoint sensitivities: **gradient-based**, model-aware -- require access to internals via automatic differentiation
-   Adjoint sensitivities are old friends: 4D-Var data assimilation, adjoint modelling in NWP
-   Your existing sensitivity-analysis expertise transfers directly to XAI -- not a new skill, a new application

---

## If we had 90–120 minutes

-   Part 1 extensions: counterfactuals, LIME comparison, fairness/robustness probes
-   Part 2 extensions: live `RUN_LIVE=True` inference, perturb a different variable/location, compare lead times
-   Cross-cutting: quantitative benchmarking of XAI methods against each other
-   See `extensions.md` in the repo for the full list

---

<!-- _class: invert lead -->

# Recap <!--fit-->

---

## Recap: the arc

-   Framing: adoption gap is real, XAI builds trust, four recommendations
-   Part 1: naive → robust XAI on a simple tabular problem -- impurity, permutation, PDP/ICE, SHAP
-   Part 2: same thinking, operational AI weather model -- adjoint sensitivities via automatic differentiation
-   Core message: your domain expertise transfers; XAI is a lens, not a black box unto itself

---

## Resources

-   Part 1 basis: ml.recipes -- github.com/JesperDramsch/ml-for-science-reproducibility-tutorial (Dramsch & Maggio, 2022, MIT)
-   Framing paper: Dramsch et al. (2025), *Nature Geoscience*, doi.org/10.1038/s41561-025-01639-x
-   Workshop repo: `github.com/jesperdramsch/xai-weather-workshop`
-   Palmer Penguins: Dr. Kristen Gorman & Palmer Station Antarctica LTER; `palmerpenguins` package (Muhammad Chenariyan Nakhaee, MIT)

---

## Acknowledgements

-   Part 2 materials: ECMWF / ecmwf-training course materials, reused with instructor's authority as course contributor
-   `perturbation.py`, `sensitivities.py`: Apache-2.0, Copyright 2024 Anemoi contributors (from `anemoi-inference`)
-   Nature Geoscience Comment: Dramsch, Kuglitsch, Fernández-Torres, Toreti, Albayrak, Nava, Ghaffarian, Cheng, Ma, Samek, Venguswamy, Koul, Muthuregunathan & Hrast Essenfelder (2025)
-   This repo: MIT License, Copyright (c) 2026 Jesper Dramsch

---

<!-- _class: invert lead -->

## Questions?

&nbsp;

Jesper Dramsch (they/them) · ECMWF
ai-in-public-health@rki.de

Repo: `github.com/jesperdramsch/xai-weather-workshop`
