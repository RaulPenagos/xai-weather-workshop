# Framing Talk Track (~8 minutes)

Speaker notes for the opening of "From SHAP to AIFS -- Explainable AI for Weather and Climate".

Source: Dramsch, J.S. et al. (2025). "Explainability can foster trust in artificial
intelligence in geoscience." _Nature Geoscience_. https://doi.org/10.1038/s41561-025-01639-x

---

## 1. Hook -- why trust matters

Quick show of hands: who here already uses a machine learning model in their work?

Keep your hand up if you've ever had a colleague, reviewer, or forecaster ask
_"why should I believe this?"_

Think about natural hazards for a second.

-   Where should we anticipate tornadoes?
-   How early can we predict a volcanic eruption?
-   What determines flood susceptibility?

If a model gives you an answer but not a reason -- would you act on it?
Would your stakeholders?

---

## 2. The trust problem, precisely

Here's the pattern the paper describes.

As AI models get more complex... they tend to get more skillful.

But their interpretability -- from a physical, process-based perspective -- tends to
go _down_.

More skill, less insight. That's the trade-off.

In everyday applications, maybe that's a fair trade.

In high-stakes situations -- hazards, warnings, decisions with lives attached --
that gap erodes trust. And erosion of trust is an adoption barrier.

XAI is one way to close that gap.

Not by making the model simpler. By making the model's reasoning visible.

---

## 3. What XAI buys you

A useful mental image from the paper: XAI as a **magnifying lens**.

It lets you look at your data _through the model's eyes_.

Concretely, that's useful for:

-   Catching spurious correlations and data problems before they bite you
-   Surfacing input-prediction links worth a closer scientific look

Real examples from the literature: landslide susceptibility studies, meteorological
drought index studies -- where XAI outputs lined up with, and reinforced,
physical understanding researchers already had.

XAI isn't just a trust exercise. It can be a discovery tool.

---

## 4. The adoption gap -- a surprising number

Now here's the part that motivated this workshop.

The paper's authors scanned 2.3 million arXiv abstracts, 2007 to 2022.
Sampled and read the full text of 12,429 geoscience papers across 30 subfields.

Two numbers:

**25.5%** of geoscience papers mention AI.

**6.1%** mention XAI.

And that gap? It's not closing. Roughly flat for over a decade.

Geoscience has adopted AI. It has not, at anywhere near the same rate,
adopted the tools to explain that AI.

XAI mentions cluster in a couple of subfields -- remote sensing, seismology,
volcanology -- and barely touch the rest.

That's the gap this session is trying to help you personally close.

---

## 5. A framework: where, when, what

The paper organizes XAI questions along three axes. Think of it as a Venn diagram.

**Space** -- _where._ Where should we anticipate tornadoes?

**Time** -- _when._ How early can an eruption be predicted?

**Feature** -- _what._ What factors drive flooding susceptibility?

And they combine: _where and when_ should we expect landslides?
_Where_ does low humidity contribute to wildfire risk?

Keep this framework in your pocket for the next 45 minutes.

---

## 6. Where today's session sits in that framework

Here's the roadmap, mapped onto that Venn diagram.

**Part 1**, the next half hour: penguins, tabular data, classic XAI methods --
tree importance, permutation importance, PDP/ICE, SHAP.

These methods mostly answer **"what"**. What features drove this prediction.
Feature-focused questions.

**Part 2**, the instructor demo: ECMWF's AIFS, an operational AI weather model.
Backward sensitivity maps.

Those answer **"where"** -- which locations upstream mattered -- and **"when"** --
which lead times, which input timesteps.

Same underlying goal. Different axis of the same framework.

By the end, you'll have touched all three corners of that triangle.

---

## 7. Four things the paper asks of the field

The paper closes with four recommendations. Quickly:

**Demand.** Funders, reviewers, end users -- ask for interpretable, transparent
approaches. Make it a explicit requirement, not a nice-to-have.

**Resources.** If you use XAI, understand how it actually works, and where
it breaks. Read the library docs closely -- popular tools have real, specific
shortcomings. Benchmark your black-box models properly.

**Partnerships.** International efforts -- the UN Global Initiative on Resilience
to Natural Hazards through AI Solutions, the EU's Climate Intelligence project --
exist to put geoscientists and AI experts in the same room.

**Integration.** The field needs standardized, interoperable workflows with
XAI built in from the start, not bolted on after.

---

## 8. Where this workshop fits -- and what's next

This session is "Resources" in action. That's literally why we're here.

Over the next 45 minutes:

**Part 1** -- a simple, well-understood tabular problem (penguins), where we can
build careful intuition for four classic XAI methods, including where each one
misleads you.

**Part 2** -- the same thinking, applied to a real, operational AI weather model.

If you take one thing from this framing: the skills transfer. What you learn on
penguins in the next half hour is directly the lens we'll use on a state-of-the-art
weather model at the end.

Let's get into it.

---

### Further reading

Dramsch, J.S., Kuglitsch, M.M., Fernández-Torres, M.-Á., Toreti, A., Albayrak, R.A.,
Nava, L., Ghaffarian, S., Cheng, X., Ma, J., Samek, W., Venguswamy, R., Koul, A.,
Muthuregunathan, R. & Hrast Essenfelder, A. (2025). Explainability can foster trust
in artificial intelligence in geoscience. _Nature Geoscience_.
https://doi.org/10.1038/s41561-025-01639-x
