# LLM events, 1–14 October 2026

Fourth edition in the LLM Dojo fortnightly series. One self-contained HTML file, no build step.

Live at `https://rupnikj.github.io/llm-dojo/oct2-2026/` once pushed.

## What's in it

Nine threads over 83 events:

| Thread | Events | Subject |
|---|---|---|
| Mathematics | 9 | OpenAI's 722 manuscripts, the AHM statement, Meta's six papers |
| Model releases | 14 | Haiku 5.5, Muse Wonder, Argon GA, Mistral Large 4 |
| Decision models | 7 | TypeSafe's revenue, four vendors in one day, open reproductions |
| Evaluation | 12 | The MiMo RL-environment audit, 206 verifier bugs, hallucination gates |
| Harnesses | 11 | 62% against 33% on identical weights, agent teams, Pi 1.0 |
| Oversight | 12 | The OpenAI dismissals, monitor evasion, evaluation awareness |
| Open weights | 7 | Reflection Beam, EmbeddingGemma 2, Kolibri, shared RL environments |
| In practice | 7 | A planet candidate, Torvalds on old kernel code, ten papers from five million health records |
| Infrastructure | 4 | Modal at $1B ARR, sandboxes as a product category, tokens per megawatt |

## Sources

Everything comes from the ten AINews daily issues covering 1–14 October 2026, read in full,
plus the primary posts they link. Every event carries its own links. All 131 X links and the
25 other links were checked and resolve.

Dates follow the day the issue reported an item. AINews batches weekends, so the issues of
6 October (covering 3–5 October), 13 October (10–12), 14 October (12–13) and
15 October (13–14) contribute
events dated to the last day of their window unless the underlying post is clearly dated
otherwise. Days with more than eight events wrap into side-by-side columns on the timeline.

## Adding events later

Everything renders from the single `EVENTS` array in the inline script. To add one:

```js
E("2026-10-14","model","Title","One paragraph of plain prose.",[X("handle","statusid"), I.nyc]),
```

`E(date, thread, title, summary, links)`. Thread keys are the keys of `ARCS`:
`math`, `model`, `decide`, `eval`, `harness`, `safety`, `open`, `practice`, `infra`.
`X(handle, id)` builds an x.com status link; `I.<key>` is one of the ten issue links
defined above the array. The timeline, the per-thread moment lists and the chronology all
regenerate; axis ticks are the hardcoded list a few lines below `xPos`, so extend those if
the window moves past 14 October.

## Checks run

- `node --check` on the extracted inline script
- stubbed-DOM run: 83 dots, 9 legend buttons, 83 chronology rows, per-thread moment counts,
  stepping through all 83 events with Next
- HTTP check on every outbound link (github.com and openai.com return 403 to automated
  requests but are correct; both came straight out of the issue HTML)
