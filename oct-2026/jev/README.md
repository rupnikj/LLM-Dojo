# Decision models: Jev

Materials for the LLM Dojo session on TypeSafe's Jev, October 2026. Two self-contained pages, linked from the site's main index; no build step.

- `decision-models.html`: the slides. Arrow keys, space or a click move between slides; `F` toggles full screen, `N` shows the speaker notes; the URL hash holds the slide number (`#12`).
- `radar.html`: the Jev Radar Atlas. 3,404 projects merged from jevradar.com, madewithjev.com and 13 GitHub awesome-lists (fetched 1 October 2026), each labelled by Jev with its job, field and what it replaces; ten hand-picked examples per job; a searchable list.

## Method

- Measurements use hosted Jev (`typesafe/jev-1.13`) and GPT-6 Luna through OpenRouter, and open models run locally with llama.cpp on a 16 GB M2 MacBook.
- The 324 hard decisions are Bespoke Labs' held-out set from the Nimble repository; the 232 everyday decisions are our own.
- The example requests and answers on the slides were captured live on 1 October 2026.
- Project labels in the atlas are Jev's own answers; a hand check of 24 random projects agreed on the job for 21.

Generated from the working folder `jev/` (deck sources in `jev/deck/`, atlas in `jev/scripts/build_atlas.py`). Assembled with Claude.
