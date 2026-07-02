# Extensions for a longer slot

The core session (`README.md`, timing table below repeated for reference) is built for a tight
60-minute slot: a guided Part 1 on tabular data and an instructor-led Part 2 demo that renders
entirely from pre-committed artifacts. Both notebooks are deliberately modular so that a longer
slot can go deeper on the same material rather than requiring new content.

This document lists what to add for a 90-minute or 120-minute variant, split by part, plus two
suggested extended timing tables. Nothing here changes the 60-minute core; everything below is
additive.

---

## 1. Part 1 extensions (`01_classic_xai.ipynb`)

All of these slot in after their corresponding core method, before moving on to the next one.
Suggested order below follows the notebook's naive-to-robust arc.

### 1.1 After Method 1 (tree/impurity importance)

- **Compare impurity importance across model families.** Add a `GradientBoostingClassifier` (or
  `HistGradientBoostingClassifier`, which handles the one-hot columns more gracefully) alongside
  the RF/SVC pair used in the core notebook. Impurity importance is specific to tree ensembles,
  so this is a natural place to show that even within "tree-based importance" the numbers shift
  with boosting vs. bagging, splitting criteria, and tree depth -- reinforcing that impurity
  importance is a property of *how a particular model happened to be fit*, not a stable property
  of the data.

### 1.2 After Method 2 (permutation importance)

- **A third model family in the grouped boxplot.** Extend the flagship RF-vs-SVM train/test
  permutation importance figure with the gradient boosting model from 1.1. A three-model,
  two-split grouped boxplot is still readable and makes the train/test-agreement argument (no
  overfitting signal) more convincing with a third data point.
- **Correlated-feature discussion.** Palmer Penguins' bill length/depth and flipper length are
  correlated with body mass and with species. Permutation importance can split credit
  unstably between correlated features (or double-count them) because permuting one feature at a
  time breaks and then randomly reconstructs its correlation with the others. A short
  demonstration -- permute two correlated features jointly vs. independently and compare -- makes
  a good bridge into SHAP interaction values later.

### 1.3 After Method 3 (PDP/ICE)

- **2D / interaction PDPs.** `sklearn.inspection.PartialDependenceDisplay` supports two-feature
  contour plots (e.g. bill length x bill depth, or flipper length x body mass). This is the
  natural fix for the core notebook's stated pitfall ("averaging hides interactions") -- a 2D PDP
  directly shows where the response surface is non-additive, which a 1D PDP by construction
  cannot.
- **Centered ICE (c-ICE) plots.** Re-centering each ICE curve at its leftmost (or a chosen
  reference) value isolates the *shape* of each individual's response from the *level*, making
  divergent individuals easier to spot than in the raw ICE plot used in the core Exercise 3.

### 1.4 After Method 4 (SHAP)

- **SHAP interaction values** (`shap.TreeExplainer` with `interaction_index`, or
  `shap.plots.scatter` with automatic interaction coloring). This is the direct SHAP-side
  counterpart to the 2D PDP extension above and to the correlated-permutation-importance
  discussion -- worth explicitly connecting the three so participants see the same phenomenon
  (feature interaction / correlation) surfaced by three different methods.
- **SHAP dependence plots** (`shap.plots.scatter`) for one or two continuous features, colored by
  a likely interacting feature. Good complement to the beeswarm summary already in the core
  notebook: beeswarm shows global ranking + direction, dependence plots show the functional
  relationship per feature, similar in spirit to a PDP but built from local attributions rather
  than averaged model output.
- **Fairness / proxy-feature discussion, building on the `Sex`-as-proxy pitfall.** The core
  notebook's Method 4 pitfall already flags that SHAP explains *the model*, not *the world*, using
  `Sex` as the example of a feature that may be a proxy rather than a causal driver. For a longer
  slot, extend this into a short discussion (10-15 min, can be run as a facilitated conversation
  rather than more code):
  - What would it mean for `Sex` to be a proxy here -- proxy for what underlying biological or
    measurement variable?
  - Contrast **explanatory fidelity** (SHAP faithfully describes what the trained model does)
    with **causal/physical validity** (whether that description matches a real-world mechanism).
    This distinction is exactly the challenge Dramsch et al. (2025) raise about XAI reliability in
    geoscience: methods built for image data may attribute importance to spurious correlations
    that are statistically real but not physically meaningful.
  - Optional hands-on component: refit the model *without* `Sex`, compare SHAP rankings before and
    after, and discuss whether removing a proxy feature is generally the right fix (it usually
    isn't, on its own -- the underlying correlation the proxy encoded may still leak through other
    features).
  - This is a good place to explicitly reference the "Resources" recommendation from the framing
    talk: understanding a method's mechanics and limitations, rather than applying it
    unquestioned, is exactly what this discussion practices.

---

## 2. Part 2 extensions (`02_aifs_sensitivities.ipynb`)

The core 60-minute session runs Part 2 fully offline, rendering the five pre-committed artifacts
in `artifacts/images/`. For a longer slot with a reliable venue network, Part 2 can go fully
hands-on by flipping the `RUN_LIVE` flag and having participants run live AIFS inference
themselves, reproducing (and then varying) the artifacts instead of just viewing them.

### 2.1 Feasibility

- **Checkpoint:** the AIFS O48-resolution checkpoint used by the source ECMWF course notebook is
  small by NWP-model standards (~180 MB) and runs on CPU -- no GPU required. This makes it
  realistic for a workshop room of laptops on Colab CPU runtimes or local CPU environments.
- **Network caveat:** ~180 MB per participant over shared venue wifi will be slow and can stall a
  session if everyone triggers the download at the same moment. **Pre-stage the checkpoint** where
  possible:
  - Have participants download it before the session (link + instructions sent in advance), or
  - Host a local mirror / shared drive on the venue network, or
  - Cache it into the Colab runtime's persistent storage / a shared Google Drive folder referenced
    by the notebook, so the download happens once rather than N times.
  Budget a few minutes of session time for this even if pre-staged, since not everyone will have
  followed the pre-session instructions.
- **Gating:** keep the `RUN_LIVE` flag as the single switch between offline (artifact-rendering)
  and live (inference) modes, so the same notebook degrades gracefully if the network or the
  checkpoint download fails mid-session -- fall back to the committed artifacts and keep going.

### 2.2 Hands-on tasks (from the original ECMWF course notebook)

With `RUN_LIVE=True` and the checkpoint staged, participants can work through the same tasks the
source ECMWF 2025 ML training course notebook (`5-xAI-with-AIFS/explain_AIFS-cpu.ipynb`,
`ecmwf-training` org) sets up, adapted here as a guided sequence:

- **Task 5.1 -- Different location.** Re-run the backward-sensitivity computation with the unit
  perturbation moved to a new location instead of the Bohai Sea / China coast point used in the
  core artifacts. Good candidate regions to suggest: a mid-latitude storm track location, a
  tropical location (to contrast convective vs. synoptic sensitivity structure), or a location
  chosen by the participant tied to their own research area. Compare the resulting z_500 and
  cross-section sensitivity maps to the pre-committed artifacts -- does the upstream synoptic
  structure look qualitatively similar in character (spatial decay scale, alignment with flow) or
  very different?
- **Task 5.2 -- Different perturbation radius.** Repeat with a smaller (e.g. 100 km) and larger
  (e.g. 700 km) radius than the core session's 350 km, at the same location. This probes how
  sensitivity magnitude and spatial spread of the backward signal scale with the size of the
  initial perturbation -- a direct, hands-on way to build intuition for what "sensitivity" is
  measuring, and a natural link back to scale arguments familiar from ensemble sensitivity
  analysis and adjoint-based targeting in NWP.
- **Task 5.3 -- Custom `Perturbation` subclass.** The source notebook's `perturbation.py` (from
  `anemoi-inference`, Apache-2.0) defines the perturbation applied to the forecast output before
  backpropagating. Have participants write a small custom subclass -- e.g. a perturbation shaped
  as a Gaussian bump rather than a hard-cutoff disk, or a perturbation on a different output
  variable entirely (e.g. 10m wind instead of 2t) -- and inspect how the resulting sensitivity
  maps change. This is the most open-ended task and works well as a small-group exercise with
  participants comparing results at the end.

### 2.3 Suggested framing for the hands-on version

Keep the bridge-back-to-Part-1 message central even in the extended version: permutation
importance and SHAP are perturbation-based and model-agnostic (probe the model from the outside),
while backward/adjoint sensitivities are gradient-based and model-aware (require access to
internals via automatic differentiation). Tasks 5.1/5.2 are literally perturbation experiments on
a gradient-based method, which is a good opportunity to make that contrast concrete: participants
are perturbing the *output* location/radius, then reading off how the *gradient-based* backward
sensitivity redistributes -- not perturbing inputs and reading off output change, the way
permutation importance does. Meteorologists and geoscientists with adjoint or 4D-Var experience
should be encouraged to narrate what they're seeing in those terms.

### 2.4 Attribution reminder

Any live-inference extension still runs on the ECMWF `ecmwf-training` 2025 ML training course
materials (`5-xAI-with-AIFS/explain_AIFS-cpu.ipynb`), reused here with the instructor's authority
as an ECMWF-affiliated contributor to that course. `perturbation.py` and `sensitivities.py` carry
an Apache-2.0 header (Copyright 2024 Anemoi contributors) since they originate from the
`anemoi-inference` package -- keep that header intact in any copies used for Tasks 5.1-5.3, and
continue crediting "ECMWF / ecmwf-training course materials" generally, per the repo's licensing
notes.

---

## 3. Extended timing tables

Both variants keep the framing talk, Part 1 core methods, and wrap-up intact, and add time in the
places described above. Extension items are additive and can be trimmed live if running short --
the fully-offline Part 2 core (artifact walkthrough + bridge-back) should always be treated as the
non-negotiable minimum for Part 2, even in the extended variants, in case `RUN_LIVE` has to be
abandoned for network reasons.

### 3.1 90-minute variant (+30 min vs. core)

| Time | Duration | Segment |
|---|---|---|
| 0:00-0:08 | 8 min | Framing (unchanged) |
| 0:08-0:12 | 4 min | Part 1 setup |
| 0:12-0:20 | 8 min | Method 1: Tree/impurity importance + Exercise 1 + gradient boosting comparison (1.1) |
| 0:20-0:30 | 10 min | Method 2: Permutation importance + train/test boxplot + Exercise 2 + correlated-feature demo (1.2) |
| 0:30-0:38 | 8 min | Method 3: PDP/ICE + Exercise 3 + 2D interaction PDP (1.3) |
| 0:38-0:52 | 14 min | Method 4: SHAP + Exercise 4 + interaction values / dependence plots + proxy-feature discussion (1.4) |
| 0:52-1:12 | 20 min | Part 2 hands-on: `RUN_LIVE` walkthrough + **one** of Tasks 5.1/5.2 (participant choice), bridge-back to Part 1 |
| 1:12-1:16 | 4 min | Extensions pointer (what a 120-min slot adds beyond this) |
| 1:16-1:20 | 4 min | Wrap: resources, ml.recipes, Nature Geoscience paper, contact/questions |

### 3.2 120-minute variant (+60 min vs. core)

| Time | Duration | Segment |
|---|---|---|
| 0:00-0:10 | 10 min | Framing (unchanged, slightly more room for questions) |
| 0:10-0:15 | 5 min | Part 1 setup |
| 0:15-0:25 | 10 min | Method 1: Tree/impurity importance + Exercise 1 + gradient boosting comparison (1.1) |
| 0:25-0:38 | 13 min | Method 2: Permutation importance + train/test boxplot + Exercise 2 + correlated-feature demo (1.2) |
| 0:38-0:50 | 12 min | Method 3: PDP/ICE + Exercise 3 + 2D interaction PDP + centered ICE (1.3) |
| 0:50-1:08 | 18 min | Method 4: SHAP + Exercise 4 + interaction values / dependence plots + proxy-feature / fairness discussion (1.4) |
| 1:08-1:13 | 5 min | Break |
| 1:13-1:16 | 3 min | Part 2 setup: checkpoint status check, `RUN_LIVE` toggle, offline-fallback reminder |
| 1:16-1:24 | 8 min | Part 2 core: artifact walkthrough (all 5 images) + bridge-back to Part 1 (unchanged core content) |
| 1:24-1:44 | 20 min | Part 2 hands-on: Tasks 5.1, 5.2, and 5.3 in small groups, own location/radius/perturbation choice |
| 1:44-1:52 | 8 min | Group share-out: 2-3 groups briefly present what changed in their sensitivity maps |
| 1:52-1:56 | 4 min | Extensions beyond 120 min pointer (e.g. other AIFS output variables, ensemble sensitivity, longer lead times) |
| 1:56-2:00 | 4 min | Wrap: resources, ml.recipes, Nature Geoscience paper, contact/questions |

Notes on both tables:

- The 90-minute variant intentionally offers only **one** of Tasks 5.1/5.2 rather than all three,
  to leave the bridge-back message enough room -- that message is the payoff of the whole
  session and should not be rushed.
- The 120-minute variant is the first slot length where a mid-session break becomes worth
  scheduling explicitly (also gives the checkpoint download extra buffer if it wasn't fully
  pre-staged).
- In both variants, if `RUN_LIVE` inference fails or the checkpoint isn't ready, fall back
  immediately to the offline artifact walkthrough from the 60-minute core and treat the hands-on
  tasks as a "try this after the session" pointer instead -- do not let infrastructure trouble
  eat into the framing or bridge-back content.
