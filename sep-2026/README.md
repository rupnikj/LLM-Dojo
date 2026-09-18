# Two weeks: 3–16 September 2026

A single self-contained page: six threads, an interactive timeline of 57 dated events, two visuals, and a chronology. No build step; edit `index.html` directly.

## Sources and method

- Every AINews issue covering the window was read in full, not skimmed: the five published on the site (3, 4, 8, 9, 10 September) plus the email editions covering 11–16 September, which the site had not published at the time of writing.
- Events link a primary source where one exists — the announcing account on X, a vendor post, a repository, a paper — and their dated AINews issue otherwise.
- Events dated 11–16 September link to the AINews archive rather than a dated issue, because those issues were not yet on the site. They are labelled as such on the page.
- Assembled with Claude; grouping and emphasis are the dojo's.

## Updating

Event data lives in one `EVENTS` array inside `index.html`; the timeline, per-thread lists and chronology all render from it. Adding an event is one line.
