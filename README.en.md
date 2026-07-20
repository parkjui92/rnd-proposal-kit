# rnd-proposal-kit

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-purple.svg)

[한국어](README.md) · **English**

A [Claude Code](https://claude.com/claude-code) plugin: a **five-agent team** that takes a Korean government R&D proposal from the public call document to a submission-ready `.hwpx` file (Hangul Word Processor, the de facto standard for Korean government paperwork).
Korean R&D funding is awarded through a call document that ships with an itemized scoring rubric — a review panel scores your proposal against it, item by item, with fixed point weights.
What separates this kit from a general writing tool is not prose but one table: the **evaluation-response map** binds each rubric weight one-to-one to the outline, so the highest-scoring items structurally cannot end up as the thinnest sections.

<!-- demo GIF goes here -->

## The central fixture — the evaluation-response map

Produced after reading the call document and **before any drafting begins**.

| Rubric item | Points | Proposal section | Core scoring argument | Evidence to gather |
|---|---|---|---|---|
| Technical development | **30** | §3 Content & differentiation | Domain-specific + on-premise security | Feature/limitation comparison vs. similar platforms |
| Commercialization | **30** | §4 Commercialization strategy | Subscription BM + diffusion via public agencies | Market size, demand, diffusion channels |
| Execution capacity | 20 | §5.1 Roadmap + §5.2 Capability | Staged milestones + institutional capability | [needs sourcing] track record |

**A blank cell means the outline is wrong.** A rubric item with no corresponding section means you are discarding that item's points outright, and a cell that only says "emphasize X" means there is no scoring argument yet. Putting weights and page shares side by side also makes "a 30-point item gets the same space as a 20-point item" visible *before* anyone writes a word. The table is reused throughout: the investigator gets the last column as a work order, the writer keeps it open while drafting, and the reviewer rules against it at both gates.

→ [Why I built this + detailed usage](docs/why.md) · [source of the excerpt](examples/rnd-proposal-demo/01_rfp_analysis.md)

## Pipeline

```
Call analysis → Outline + response map → 🚦Gate 1 (design review) → ★You approve
              → Research → Drafting → 🚦Gate 2 (5-axis review) → hwpx
```

Gate 1 protects *cost* — once research and drafting finish against a wrong outline, there is no way back inside the deadline. Gate 2 protects against *overconfidence*. The reviewer is a **different agent from the writer** and is read-only, so nobody signs off on their own work. Rulings persist as files.

Caught in the bundled demo: a mandatory requirement (personal-data protection and security) had neither its own subsection nor a row in the response map → promoted to §5.3 · the 30-point items had only a 3-percentage-point page advantage over the 20-point items → allocation redone · the differentiation table was benchmarking general-purpose AI tools and in-house enterprise builds rather than the "similar platforms" the call specified. The rulings are verbatim in [`02_design_gate.md`](examples/rnd-proposal-demo/02_design_gate.md) and [`05_review.md`](examples/rnd-proposal-demo/05_review.md).

## Install

```
/plugin marketplace add parkjui92/rnd-proposal-kit
/plugin install rnd-proposal-kit@rnd-proposal-kit
```

## Usage

```
Draft a proposal from the attached call document. Strengths memo attached.      ← from scratch
This isn't technology development — it's a policy-formulation service           ← plan-form type
It's a team proposal; I own part 2-3. Match my teammates' drafts                ← team module mode
Commercialization is worth 30 points and it's getting far too little space      ← at the outline gate
```

The project type is determined first — **four types** (technology development / commissioned or policy-formulation / application-form program / one module of a joint proposal), because the outline standard and drafting skeleton differ by type. Drop an agency's mandated form (.hwp/.hwpx) into `_workspace/00_input/` and the outline follows the form's own field order. Prompts work in Korean or English; the proposal output is Korean-first.
It pauses twice (outline approval after gate 1, the final report after gate 2), so you can step away in between.

## What you get

Not one document but **an auditable record set** — call analysis, response map, gate 1 ruling, evidence ledger, body draft, gate 2 review, final hwpx.
Which means that if you lose, you can reconstruct why — and the same evidence is reusable for the next call.

Worked example: [the full run](examples/rnd-proposal-demo/) — a synthetic demo against a fictional call, at reduced scale. But the evidence discipline is real: only the key figures were actually verified, with URLs attached, and everything else was left as `[needs sourcing]`.

## Requirements & limits

- `.hwpx` conversion needs the [kordoc](https://github.com/chrisryugj/kordoc) MCP server (without it the pipeline stops at Markdown)
- **Gates reduce errors; they don't eliminate them.** The reviewer shares a model family with the writer and can share its blind spots
- **This repository has no measured A/B against vanilla.** See the sister kit's [audit record](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md) — but those figures are that kit's, not this one's
- If the call publishes no rubric, a generic evaluation frame is applied provisionally and labeled as such — the response map is correspondingly less reliable
- Shaped by Korean government R&D conventions (weighted rubric scoring, hwpx submission, mandated forms)
- [Fallbacks, dependencies, keys](docs/runtime-notes.md) · [Gate design methodology](docs/verification-gates.md)

## Series

**Agent-team kits** — [policy-research-kit](https://github.com/parkjui92/policy-research-kit) (policy research reports) · [socsci-paper-kit](https://github.com/parkjui92/socsci-paper-kit) (social science papers)

**Authoring kit** — [lecture-deck-kit](https://github.com/parkjui92/lecture-deck-kit) (HTML lecture decks with in-browser live editing)

**Standalone skills** — [fact-verify](https://github.com/parkjui92/fact-verify) (source verification) · [paper-proofread](https://github.com/parkjui92/paper-proofread) (Korean academic proofreading) · [form-tailor](https://github.com/parkjui92/form-tailor) (institutional document formats) · [report-to-brief](https://github.com/parkjui92/report-to-brief) (report compression)

## License

[MIT](LICENSE). No proprietary institutional templates and no real client deliverables are included (bring-your-own-template principle).
