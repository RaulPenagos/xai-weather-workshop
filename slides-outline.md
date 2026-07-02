# Slides Outline — "From SHAP to AIFS: Explainable AI for Weather and Climate"

> Working title (alternates under consideration: "Explaining the Black Box: From Penguins to Weather Models",
> "XAI in Geoscience: From Feature Importance to Adjoint Sensitivities"). One slide per bullet-level entry below.
> This is a build-the-deck-from outline: terse titles + 2-4 content notes per slide, not a script.
>
> Mirrors `00_framing/framing.md` (being authored separately — not yet present in the repo as of this writing)
> for the framing section slide-breaks, then one slide per Part 1 method, artifact-image slides for Part 2,
> a bridge-back slide, and a closing resources slide.
>
> **Estimated total: 34 slides** (title 1 + framing 8 + Part 1 setup/transition 2 + Part 1 methods 4 + Part 1
> exercises 4 + Part 2 title/context 2 + Part 2 artifacts 5 + bridge-back 1 + extensions 1 + wrap/resources 2
> + buffer/contact 4 — see per-section counts below for exact breakdown).

---

## 0. Title (1 slide)

### Slide 1 — Title
- "From SHAP to AIFS: Explainable AI for Weather and Climate" (note: working title)
- Subtitle: Climademics Summer School, 2026-07-03
- Presenter name / ECMWF affiliation
- Session badge: Part 1 hands-on (Colab) + Part 2 instructor demo

---

## 1. Framing (0:00–0:08, ~8 min) — mirrors `00_framing/framing.md` (8 slides)

### Slide 2 — Why explainability, why now
- AI model complexity/predictive skill up -> physical interpretability tends down
- In high-stakes settings (natural hazards) this erodes trust -> adoption barrier
- XAI: methods that reveal the AI's decision process to rebuild that trust

### Slide 3 — What XAI actually gives you
- Definition: an explanation that "justifies its recommendation, decision, or action"
- Acts as a "magnifying lens" — see the data through the model's "eyes"
- Detects spurious correlations / data issues before they cause harm
- Can motivate new science (e.g. landslide susceptibility, drought index studies)

### Slide 4 — The adoption gap (the numbers)
- 2.3M arXiv abstracts (2007–2022) screened; 12,429 geoscience abstracts full-text analysed
- 25.5% of geoscience papers reference AI — only 6.1% reference XAI
- Gap has stayed roughly flat 2007–2022, no clear upward trend
- XAI mentions cluster in geoinformatics/remote sensing and geophysics (seismology, volcanology)

### Slide 5 — Why the gap exists (researcher survey)
- Motivations to use XAI: trust, insight into data/model issues, efficiency, discovery of physical processes
- Source: ITU/WMO/UN Environment Focus Group on AI for Natural Disaster Management
- Non-adopters: mostly cite lack of time/effort/resources, not lack of perceived value
- Almost all non-adopters plan to apply XAI eventually

### Slide 6 — Framing question: where / when / what
- 3-circle Venn: Space ("where"), Time ("when"), Feature ("what")
- Example (natural hazards): "Where should we anticipate tornadoes?" / "How early can a volcanic eruption be predicted?" / "What determines flood susceptibility?"
- Intersections: "Where and when should we expect landslides?" / "Where does low humidity contribute to wildfires?" / "Where and when does a lack of precipitation contribute to drought?"
- Preview: Part 1 methods mostly answer "what" (feature importance); Part 2 answers "where" (maps) and "when" (lead time)

### Slide 7 — Challenges
- Most XAI historically built for image data; geospatial/spatiotemporal data behaves differently
- Need for object/concept-level explanations, not just pixel attribution
- Pixel/feature attribution often still not interpretable by non-specialists in physical terms
- Relevance, accuracy and reliability of XAI methods for geoscience remain open questions

### Slide 8 — Four recommendations
- **Demand**: funders, reviewers, end-users should explicitly ask for interpretable/transparent approaches
- **Resources**: understand method mechanics/limits, read library docs carefully, benchmark black boxes quantitatively
- **Partnerships**: e.g. UN Global Initiative on Resilience to Natural Hazards through AI Solutions, EU Climate Intelligence project
- **Integration**: streamlined, standardized, interoperable workflows integrating XAI build trust at scale

### Slide 9 — This workshop is "Resources" in action
- We will apply XAI methods hands-on, understand their mechanics and where they mislead
- Today's arc: classic tabular XAI (Part 1) -> state-of-the-art operational AI weather model (Part 2)
- Core message: domain expertise you already have (adjoint thinking, sensitivity analysis) transfers directly
- Citation: Dramsch et al. (2025), *Nature Geoscience*, https://doi.org/10.1038/s41561-025-01639-x

---

## 2. Part 1 setup (0:08–0:12, ~4 min) (2 slides)

### Slide 10 — Part 1: Classic XAI, roadmap
- Notebook: `01_classic_xai.ipynb` (self-contained, runs on Colab free CPU tier)
- Dataset: Palmer Penguins (species classification from bill/flipper/mass/sex/island)
- Models trained inline: `RandomForestClassifier` and `SVC`
- Didactic arc: naive -> robust; each method = question it answers -> worked example -> where it misleads you

### Slide 11 — Data + models (participants run cells)
- Load via `palmerpenguins` package (fallback: `sns.load_dataset('penguins')`)
- Quick EDA: species/island/sex distributions, colorblind-safe palette (viridis/cmocean)
- Train/test split, fit RF + SVM
- Baseline accuracy check before any explanation method is introduced

---

## 3. Part 1 — Method slides (0:12–0:40, ~28 min) (4 method slides + 4 exercise slides = 8 slides)

### Slide 12 — Method 1: Tree / impurity importance
- **Question it answers**: which features did the trees actually split on, weighted by impurity reduction?
- **Worked example**: RF impurity importance on penguins; classic `Sex` -> one-hot `Female`/`Male` split artifact (fixed here via `get_feature_names_out()`)
- **Where it misleads you**: biased toward high-cardinality / correlated features; fast but not trustworthy in isolation

### Slide 13 — Exercise 1
- Add a random-noise feature to the training data
- Re-run tree impurity importance with the noise feature included
- Task: explain why pure noise gets nonzero importance
- Discussion prompt: what does this imply about trusting impurity importance alone?

### Slide 14 — Method 2: Permutation importance
- **Question it answers**: how much does shuffling one feature degrade model performance? (model-agnostic)
- **Worked example**: grouped boxplot — RF vs SVM, train vs test permutation importance, uncertainty via `n_repeats`
- **Where it misleads you**: correlated features share/dilute importance; train/test agreement is itself a diagnostic (agreement = no overfitting signal)

### Slide 15 — Exercise 2
- Repeat the noise-feature experiment, now with permutation importance, on both RF and SVM
- Task: does the noise feature show up now?
- Task: explain the disagreement with Exercise 1's tree-importance result
- Discussion prompt: which method would you trust more, and why?

### Slide 16 — Method 3: PDP / ICE
- **Question it answers**: how does the prediction change as one feature varies, on average (PDP) and per-instance (ICE)?
- **Worked example**: average response curves + individual ICE curves for a bill/culmen feature (historical source only showed averages — this rebuild adds real ICE)
- **Where it misleads you**: averaging (PDP) hides interactions between features; curves extrapolate into empty/sparse regions of feature space

### Slide 17 — Exercise 3
- Add ICE curves for a bill/culmen-depth feature
- Task: find an individual penguin whose ICE curve diverges from the average PDP
- Discussion prompt: what does that divergence tell you about feature interactions?

### Slide 18 — Method 4: SHAP
- **Question it answers**: how does each feature push an individual prediction away from the baseline (local), and what matters globally (beeswarm)?
- **Worked example**: `shap.plots.waterfall` (single prediction) + `shap.plots.beeswarm` (global summary) — modern matplotlib-native API, replacing broken JS `force_plot`/`initjs()` in static exports
- **Where it misleads you**: explaining the model is not explaining the world — e.g. `Sex` may be a proxy/confound, not a causal driver

### Slide 19 — Exercise 4
- Compare SHAP's global feature ranking to permutation importance's ranking
- Task: where do the two rankings disagree, and why?
- Discussion prompt: correlation vs causation — what would you need to claim a causal driver?

---

## 4. Part 2 — AIFS backward sensitivities (0:40–0:53, ~13 min) (title/context/mechanism 3 + 4 result slides = 7 slides)

### Slide 20 — Part 2: title
- "From perturbation to adjoint: sensitivities in an operational AI weather model"
- Notebook: `02_aifs_sensitivities.ipynb` — offline-first, computed live from committed `artifacts/sensitivities_o48.npz` plus two pre-rendered PNGs
- Source: ECMWF's internal 2025 ML training course (`ecmwf-training`), reused with instructor's authority as course contributor
- `RUN_LIVE=False` by default — live AIFS inference optional, gated behind this flag

### Slide 21 — The experiment setup
- Model: AIFS (ECMWF's AI Forecasting System), O48-resolution checkpoint, 6-hour lead time
- Perturbation: unit perturbation to 2m temperature (2t) forecast output, all grid points within 350 km of (40°N, 120°E) — Bohai Sea / China coast near Beijing/Tianjin
- Method: backward sensitivities via `torch.autograd.functional.vjp` — classic reverse-mode automatic differentiation (adjoint / vector-Jacobian product)
- Goal: which input variables / locations / levels most influenced that 2t forecast?

### Slide 22 — How does this actually work?
- Recreate (or screenshot) the notebook's mechanism diagram: forward pass (state -> AIFS -> forecast) vs backward pass (perturbation -> reverse-mode autodiff -> sensitivity map)
- Say explicitly before showing any results: this is differentiating *through* the network, not querying it from outside
- Land the callback line early: "the same operation as an adjoint model's gradient in 4D-Var"

### Slide 23 — Artifact: pressure-level summary
- `artifacts/images/01_pressure_level_summary.png`
- Grid of heatmaps: rows = input hour offset (-6H / 0H), columns = min/max stat
- Shows which pressure-level variables/levels have the largest-magnitude sensitivities overall
- Purpose: overview before drilling into specific spatial maps

### Slide 24 — Live demo: the interactive map (or screenshots if presenting without the notebook open)
- Prefer switching to the live notebook here over a static slide -- the dropdown toggle is the point
- If a static slide is unavoidable, use two screenshots side by side: `2t` (self-consistency check -- signal sits right on the perturbation point) and `z_500` (the "wow" cross-variable moment -- a paired +/- structure, not just a bigger blob)
- Framing for `2t`: "does the model's own explanation make physical sense?"
- Framing for `z_500`: a surface perturbation reaching into upper-air dynamics, structurally different from the self-check

### Slide 25 — Artifact: temperature cross-section
- `artifacts/images/05_cross_section_temperature.png`
- Longitude-vs-pressure-level cross-section of temperature (t) sensitivity along 40.5°N
- Slice passes directly through the perturbation point
- Shows vertical structure of the backward sensitivity — boundary layer vs free troposphere

### Slide 26 — Live demo: vertical profile and pressure-level flythrough
- Vertical profile: sensitivity by pressure level at the single grid point closest to the perturbation -- normalised per variable, noisier than the maps (name that explicitly, it's a teaching point, not a flaw)
- Pressure-level flythrough: animated across all 13 levels on a fixed colour scale -- press play once and narrate over it rather than waiting in silence
- Both are first/second cut candidates if short on time (see `facilitator_notes.md`) -- if cutting for the slide deck too, this slide can be dropped without breaking the narrative arc

---

## 5. Bridge back to Part 1 (1 slide)

### Slide 27 — The "aha": you already know this
- Permutation importance & SHAP: perturbation-based, model-agnostic — probe the model with input changes, treat it as a black box
- Backward/adjoint sensitivities: gradient-based, model-aware — require access to internals via automatic differentiation
- Adjoint sensitivities are old friends: 4D-Var data assimilation, adjoint modelling in NWP
- Punchline: your existing sensitivity-analysis expertise transfers directly to XAI — this is not a new skill, it's a new application

---

## 6. Extensions pointer (0:53–0:55, ~2 min) (1 slide)

### Slide 28 — If we had 90–120 minutes
- Part 1 hands-on extensions (see `extensions.md`): counterfactuals, LIME comparison, fairness/robustness probes
- Part 2 hands-on extensions: live `RUN_LIVE=True` inference, perturb a different variable/location, compare lead times
- Cross-cutting: quantitative benchmarking of XAI methods against each other (per the paper's "Resources" recommendation)
- Pointer: `extensions.md` in repo root for the full list

---

## 7. Wrap (0:55–1:00, ~5 min) (2 slides + buffer/contact = 4 slides total)

### Slide 29 — Recap: the arc
- Framing: adoption gap is real, XAI builds trust, four recommendations (Demand / Resources / Partnerships / Integration)
- Part 1: naive -> robust XAI on a simple tabular problem — impurity, permutation, PDP/ICE, SHAP
- Part 2: same thinking, operational AI weather model — adjoint sensitivities via automatic differentiation
- Core message: your domain expertise transfers; XAI is a lens, not a black box unto itself

### Slide 30 — Resources
- Part 1 basis: ml.recipes — https://github.com/JesperDramsch/ml-for-science-reproducibility-tutorial (Dramsch & Maggio, 2022, MIT License)
- Framing paper: Dramsch et al. (2025), *Nature Geoscience*, https://doi.org/10.1038/s41561-025-01639-x
- Workshop repo: `github.com/jesperdramsch/xai-weather-workshop`
- Palmer Penguins data: Dr. Kristen Gorman & Palmer Station Antarctica LTER; `palmerpenguins` package by Muhammad Chenariyan Nakhaee (MIT)

### Slide 31 — Acknowledgements / attribution
- Part 2 materials: ECMWF / ecmwf-training course materials (2025 ML training course), reused with instructor's authority as course contributor
- `perturbation.py`, `sensitivities.py`: Apache-2.0, Copyright 2024 Anemoi contributors (from `anemoi-inference`)
- Nature Geoscience Comment: Dramsch, Kuglitsch, Fernández-Torres, Toreti, Albayrak, Nava, Ghaffarian, Cheng, Ma, Samek, Venguswamy, Koul, Muthuregunathan & Hrast Essenfelder (2025)
- This repo: MIT License, Copyright (c) 2026 Jesper Dramsch

### Slide 32 — Questions / contact
- Contact: ai-in-public-health@rki.de
- Questions welcome now, or via repo issues once pushed
- Colab links for Part 1 notebook (`jesperdramsch/xai-weather-workshop`)
- Thank you / Climademics Summer School 2026-07-03

---

## Slide count summary

| Section | Slides |
|---|---|
| Title | 1 |
| Framing (mirrors `00_framing/framing.md`) | 8 |
| Part 1 setup | 2 |
| Part 1 methods + exercises | 8 |
| Part 2 title/context/mechanism | 3 |
| Part 2 results (map, cross-section, profile/animation demos) | 4 |
| Bridge back | 1 |
| Extensions pointer | 1 |
| Wrap / resources / attribution / contact | 4 |
| **Total** | **32** |

(Text above the table estimated ~34 accounting for possible title/section-divider slides between Parts 1 and 2 in the final deck; treat 32–34 as the working range — add divider slides freely if the deck tool benefits from them, e.g. a bare "Part 1" and "Part 2" section-break slide, which would bring the total to 34.)

---

## Notes for the slide-deck builder

- Slides 2-9 above mirror `00_framing/framing.md`'s structure (why now -> what XAI gives you -> adoption gap -> survey -> where/when/what framing -> challenges -> recommendations -> this workshop as "Resources") -- double-check them against that file for wording drift, since both were authored from the same source facts independently.
- Keep colorblind-safe palettes (viridis/cmocean) on any recreated chart slides (e.g. adoption-gap time series, Venn diagram); avoid red-green encodings, consistent with notebook style.
- Tone: measured, evidence-based, no hype language ("revolutionary", "game-changing", "unlock the power of" are all out).
- Do not embed the Nature Geoscience PDF or copy figures from it directly into slides without checking copyright/reuse terms with the corresponding author (Comment articles are typically journal-copyrighted, unlike the workshop's own MIT-licensed materials) — paraphrase and cite instead, consistent with how the notebooks/framing.md handle this.
