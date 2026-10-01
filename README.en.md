# rnd-proposal-kit

[![Version](https://img.shields.io/badge/version-0.10.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-purple.svg)

[한국어](README.md) · **English**

A [Claude Code](https://claude.com/claude-code) plugin that writes a Korean government R&D proposal for you, start to finish.

Korean R&D funding works like this: an agency publishes a call document, and attached to it is a scoring rubric — a list of items, each worth a fixed number of points, that a review panel scores you against one by one. Hand this plugin the call document and it reads the requirements and the point weights, drafts an outline, gathers sources, writes the body, and produces a `.hwpx` file (the word-processor format Korean government offices require). Five AIs split the work. What sets this apart from a general writing tool isn't the prose — it's one table: **every rubric item and its points, mapped one-to-one onto the outline**, built before a word gets written.

## What makes it different

A proposal isn't judged as good writing. It's judged **item by item, for points.** However good your sentences are, if the 30-point item runs a page and a half, those 30 points don't come back.

The trouble is that the points live in the call document and the proposal lives in a different file. As you write, the pages drift toward whatever you know best — and when you finally reopen the rubric, the conclusion is always the same: the highest-scoring item is the thinnest one. So this plugin builds **this table first, before any writing.**

| Rubric item | Points | Where it goes | What earns the points | Evidence to find |
|---|---|---|---|---|
| Technical development | **30** | §3 Content & differentiation | Domain-specific + on-premise security | Feature/limitation comparison vs. similar platforms |
| Commercialization | **30** | §4 Commercialization strategy | Subscription model + rollout via public agencies | Market size, demand, distribution channels |
| Execution capacity | 20 | §5.1 Roadmap + §5.2 Capability | Staged milestones + institutional capability | [needs sourcing] track record |

**A blank cell means the outline is wrong.** A rubric item with nowhere to go means you're throwing those points away, and a cell that only says "emphasize X" means there's no scoring argument yet. Putting points and page counts side by side also makes "the 30-point item gets the same space as the 20-point item" visible before anyone writes a word.

The table keeps getting used after that. The AI that gathers sources takes the last column as its to-do list, the AI that writes keeps the table open beside it, and the AI that checks rules against it at both stops.

One more thing gets pulled out of the call document. **The sentence that sinks you never arrives in bold.** It hides after a ※ mark, inside a parenthetical, in a conditional clause like "shall be designed as a precondition for." Those get collected into a separate list, each one assigned to the section that will answer it.

→ [Why I built this, and fuller usage notes](docs/why.md)

## How it runs

```
Call document → Outline + points table → 🚦Check 1 → ★You confirm the outline → Research → Writing → 🚦Check 2 → Korean file
```

It **stops twice.** The first stop catches a bad outline. Deadlines are short, and once research and drafting are finished against the wrong structure there's no time left to go back — so it checks before writing. The second stop reviews the finished draft, because polished writing is hard to doubt on your own. That review goes to **a different AI that wrote none of it.** It can read but not edit, so nobody ever signs off on their own work. What it rules stays on disk as a file.

Things these checks have actually caught. A mandatory requirement — personal data and security — that had neither its own subsection nor a row in the table (→ promoted to §5.3). The 30-point items getting only 3 percentage points more space than the 20-point ones (→ reallocated). And a differentiation table that compared against general-purpose AI tools and in-house enterprise builds instead of the "similar platforms" the call document actually named — a table that looked filled in but answered the wrong question.

The second stop also **opens the sources.** While building the example, two sources the research stage had marked "verified" failed here: one link led to a different article that did not contain the figure, and the other was a forecast made ten years ago. Problems like these — ones that **must not be submitted as they are** — are not waved through when the revision limit is reached; it stops and asks you what to do.

## Install

```
/plugin marketplace add parkjui92/rnd-proposal-kit
/plugin install rnd-proposal-kit@rnd-proposal-kit
```

## Using it

Just ask in plain language.

```
Draft a proposal from the attached call document. Strengths memo attached.   ← from scratch
This isn't technology development — it's a policy-formulation service        ← plan-type project
It's a team proposal; I own part 2-3. Match my teammates' drafts             ← splitting the work
Commercialization is worth 30 points and it's getting far too little space   ← at the outline step
```

After reading the call document it **first sorts out what kind of project this is** — technology development, a commissioned or policy-formulation study, an application to a support program, or one person's share of a joint proposal. Four types, because the outline standard and the shape of the writing differ for each.

If the agency mandates its own form (.hwp/.hwpx), drop it into the `_workspace/00_input/` folder and the outline follows that form's own field order. Prompts work in Korean or English; the proposal itself comes out in Korean.

If the deadline is close, just say "make it fast." Research is split and run in parallel, and the body is written in batches starting with the highest-scoring sections. If a stage runs far over its expected time, it shows you what is finished so far and asks whether to continue. Mechanical steps such as format conversion run on a lighter model from the start, but **the reviewing AI is never downgraded.**

That last example line matters: when it shows you the outline, asking for changes rebuilds it right there. **It's the cheapest moment to change direction.** Between the two stops you can step away.

## What you end up with

Not just a finished proposal — **the whole process stays on disk as files.**

The call analysis, the table linking points to the outline, what the first check flagged and why, a list of which fact came from which source, the draft, what the second check found and what was actually changed, and the final Korean file.

Which means that if you lose, you can reconstruct why — and the same evidence is reusable for the next call.

## Good to know

- Producing the `.hwpx` file needs a separate converter called [kordoc](https://github.com/chrisryugj/kordoc). Without it everything still runs and you get Markdown.
- **The checks reduce errors but don't eliminate them.** The reviewing AI comes from the same model family and can share the same blind spots. A person still needs to look.
- **This repository has no measurement against plain Claude Code.** A sister plugin built on the same idea does — [policy-research-kit's comparison](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md) — but those figures belong to that plugin, not this one.
- If the call publishes no rubric at all, a generic evaluation frame is applied provisionally and labeled as such. The table is correspondingly less reliable.
- It's shaped around Korean government R&D practice (weighted rubric scoring, HWPX submission, mandated forms).
- [If setup gives you trouble](docs/runtime-notes.md) · [Building this kind of check yourself](docs/verification-gates.md)

## Related work

**Plugins that write reports and proposals** — [policy-research-kit](https://github.com/parkjui92/policy-research-kit) (policy research reports) · [socsci-paper-kit](https://github.com/parkjui92/socsci-paper-kit) (social science papers)

**Plugins that build and edit** — [lecture-deck-kit](https://github.com/parkjui92/lecture-deck-kit) (HTML lecture slides you edit right in the browser)

**Single-purpose tools** — [fact-verify](https://github.com/parkjui92/fact-verify) (check whether sources are real) · [paper-proofread](https://github.com/parkjui92/paper-proofread) (Korean academic proofreading) · [form-tailor](https://github.com/parkjui92/form-tailor) (match an organization's document format) · [report-to-brief](https://github.com/parkjui92/report-to-brief) (shorten long reports)

## License

[MIT](LICENSE). Contains no organization-specific templates and no real client deliverables — you bring your own form.
