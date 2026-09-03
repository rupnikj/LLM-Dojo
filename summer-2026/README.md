# Overview of major LLM events, 15 June – 4 September 2026

A single self-contained page: nine thematic threads, an interactive timeline of 81 dated events, an interactive price/capability frontier, and a chronology. No build step; edit `index.html` directly.

## Sources and method

- Events distilled from the daily [AINews](https://news.smol.ai/issues) issues covering the window (67 issues), read at full-issue level; every event links its dated issue and, where available, a primary source (vendor announcement, paper, repository, or X post found verbatim in an issue body).
- The price/capability frontier widget uses the dataset behind [CatalystNeuro's LLM Cost Frontier dashboard](https://catalystneuro.com/llm-cost-frontier/) (`/data/llm-frontier.json`, Artificial Analysis data), with frontier lines as computed by that dashboard. Attribution in the figure caption.
- Model licenses on the open-weights chart were verified individually against model cards and coverage in early September 2026.
- Assembled with Claude; grouping and emphasis are the dojo's.

## Updating

Event data lives in one `EVENTS` array inside `index.html`; the timeline, per-thread lists, and chronology all render from it. The AINews issue-slug map (`ISSUES`) and the frontier dataset are likewise inline.
