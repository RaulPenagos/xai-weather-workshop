#!/usr/bin/env python3
"""Adjusts README.md for the `student` branch: removes mentions of
instructor-only material (which the sync workflow has already deleted from
the working tree) and prepends a banner explaining the branch split.

Best-effort: if a known block's exact text has drifted since this script was
written (because main's README changed), that block is left in place with
a warning printed to the workflow log, rather than failing the sync.
"""

import sys
from pathlib import Path

README = Path("README.md")

BANNER = """> **You're on the `student` branch.** Solutions and facilitator-only
> materials (`solutions/`, `facilitator_notes.md`, `slides-outline.md`,
> `00_framing/framing.md`) live on `main` -- this branch mirrors
> everything else and is kept in sync automatically. This banner and the
> branch content are regenerated on every push to `main`; don't edit
> this branch directly, edit `main` instead.

"""

# Each entry: (label, exact text to remove). Removal is a plain substring
# match -- if main's wording changes, this silently stops matching and the
# text is left in place (see the warning below), which is the safe failure
# mode for a cosmetic cleanup step.
BLOCKS_TO_REMOVE = [
    (
        "Part 1 solutions badge block",
        "\n**Part 1 solutions:** `solutions/01_classic_xai_solutions.ipynb`\n"
        "[![](https://img.shields.io/badge/view-notebook-orange)](solutions/01_classic_xai_solutions.ipynb) "
        "[![](https://img.shields.io/badge/open-colab-yellow)]"
        "(https://colab.research.google.com/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) "
        "[![Binder](https://mybinder.org/badge_logo.svg)]"
        "(https://mybinder.org/v2/gh/jesperdramsch/xai-weather-workshop/HEAD?filepath=solutions/01_classic_xai_solutions.ipynb) "
        "[![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)]"
        "(https://console.paperspace.com/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) "
        "[![Open%20In%20SageMaker%20Studio%20Lab](https://studiolab.sagemaker.aws/studiolab.svg)]"
        "(https://studiolab.sagemaker.aws/import/github/jesperdramsch/xai-weather-workshop/blob/main/solutions/01_classic_xai_solutions.ipynb) "
        "[![Launch%20in%20Deepnote](https://deepnote.com/buttons/launch-in-deepnote-small.svg)]"
        "(https://deepnote.com/launch?url=https%3A%2F%2Fgithub.com%2Fjesperdramsch%2Fxai-weather-workshop%2Fblob%2Fmain%2Fsolutions%2F01_classic_xai_solutions.ipynb)\n",
    ),
    (
        "00_framing repo-layout bullet",
        "- `00_framing/` -- talk track and material for the opening framing\n"
        "  discussion, drawn from Dramsch et al. (2025).\n",
    ),
    (
        "solutions/ repo-layout bullet",
        "- `solutions/` -- worked solutions to the Part 1 exercises.\n",
    ),
    (
        "facilitator_notes.md repo-layout bullet",
        "- `facilitator_notes.md` -- timing, delivery notes, and tips for whoever\n"
        "  teaches this session.\n",
    ),
    (
        "slides-outline.md repo-layout bullet",
        "- `slides-outline.md` -- outline for accompanying slides.\n",
    ),
]


def main():
    if not README.exists():
        print("clean_student_readme: no README.md found, nothing to do")
        return

    text = README.read_text(encoding="utf-8")

    for label, block in BLOCKS_TO_REMOVE:
        if block in text:
            text = text.replace(block, "")
            print(f"clean_student_readme: removed {label}")
        else:
            print(
                f"clean_student_readme: WARNING -- {label} not found, left as-is (main's wording may have changed)",
                file=sys.stderr,
            )

    text = BANNER + text
    README.write_text(text, encoding="utf-8")
    print("clean_student_readme: banner prepended")


if __name__ == "__main__":
    main()
