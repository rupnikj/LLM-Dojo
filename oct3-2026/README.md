# LLM events, 15–27 October 2026

Fifth edition in the LLM Dojo fortnightly series. One self-contained HTML file, no build step.

Live at `https://rupnikj.github.io/llm-dojo/oct3-2026/` once pushed.

## What's in it

Nine threads over 108 events:

| Thread | Events | Subject |
|---|---|---|
| Security | 16 | PHP2Shell, Black October, ARTEX, formal verification at scale |
| Money & compute | 17 | Anthropic's S-1, DeepInfer economics, TPUv7 against GB300 |
| Open weights | 16 | Muse Spark Open, Reflection Beam, Kimi K3.1 Pro, DeepSeek V4.1 Flash |
| Evaluation | 16 | Index v5, the Terminal-Bench and TAU audits, length confounds |
| Harnesses | 10 | Harness², self-editing scaffolds, raw history against memory systems |
| Oversight | 11 | METR and Redwood inside OpenAI, the DNS escape, the Cohere trace |
| Science | 8 | CFSG formalised in Lean, two ETH disproof claims, protein binders |
| Proprietary | 7 | GPT-6.1 Terra, Genie 4, Argon's rollout, Claude Duet |
| In practice | 7 | 90% of Claude Code, the end of the coding interview, local swarms |

## Sources

Everything comes from the ten AINews daily issues covering 14–27 October 2026, read in full,
plus the primary posts they link. Every event carries its own links.

Dates follow the day the issue reported an item. AINews batches weekends, so the issue of
20 October covers 16–19 October and contributes events dated to the last day of its window
unless the underlying post is clearly dated otherwise. The first half of October is in
`oct2-2026/`; this edition starts at 15 October to avoid overlap.

## Adding events later

Everything renders from the single `EVENTS` array in the inline script. To add one:

```js
E("2026-10-27","open","Title","One paragraph of plain prose.",[X("handle","statusid"), I.hire]),
```

`E(date, thread, title, summary, links)`. Thread keys are the keys of `ARCS`:
`sec`, `infra`, `open`, `eval`, `harness`, `safety`, `sci`, `model`, `practice`.
`X(handle, id)` builds an x.com status link; `I.<key>` is one of the ten issue links
defined above the array. The timeline, the per-thread moment lists and the chronology all
regenerate; axis ticks are the hardcoded list a few lines below `xPos`, so extend those if
the window moves past 27 October. Days with more than eight events wrap into side-by-side
columns on the timeline.

## Checks run

- `node --check` on the extracted inline script
- stubbed-DOM run: 108 dots, 9 legend buttons, 108 chronology rows, per-thread moment counts,
  stepping through all 108 events with Next
- every one of the 219 X links checked against the downloaded issue text, confirming both the
  status id and the handle appear together in a source document (this caught three
  transcription errors)
- HTTP check on all 214 distinct X links and all other outbound links; github.com returns 403
  to automated requests but the URL is correct
