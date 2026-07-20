# rnd-proposal-kit

[![Version](https://img.shields.io/badge/version-0.9.0-blue.svg)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Claude Code](https://img.shields.io/badge/Claude_Code-Plugin-purple.svg)

[한국어](README.md) · **English**

> A [Claude Code](https://claude.com/claude-code) plugin: a **five-agent team** that takes a Korean government R&D proposal from the public call document all the way to a submission-ready Korean `.hwpx` file.
> At the center of this kit is the **evaluation-response map** — a table binding "which rubric item earns how many points" one-to-one to the proposal outline, so that the highest-scoring items structurally cannot end up as the thinnest sections.

> **Context for readers outside Korea.** Korean government R&D funding is awarded through a *gonggo* — a public call document that ships with an itemized scoring rubric. A review panel scores your proposal against that published rubric, item by item, with fixed point weights. Submissions are made in **HWP/HWPX** (Hangul Word Processor), the de facto standard document format for Korean government paperwork, and agencies frequently mandate a specific form template. This kit is built for that regime.

---

## Why I built this

Anyone who has responded to a Korean government R&D call knows the thing that matters most: a proposal is not writing that reads well. It is **writing that collects points**.

The reviewer sits down with a fixed rubric. There are items, each item has a point weight, and no score comes from anywhere else. So it does not matter how good the prose is — if the 30-point item runs a page and a half, those 30 points are not coming back. And if you lavish twenty pages on a 20-point item, the quality of that writing is working against you.

Knowing this does not stop you from slipping in the same three places.

**The point weights live in the call document; you write the proposal in a different file.** You definitely knew the weights when you read the rubric. But a few hours into drafting, the page count drifts toward whatever you personally know best. Open the rubric again after finishing and the conclusion is always the same — the highest-weighted item is the thinnest one.

**Disqualifying conditions do not arrive in bold.** The sentence that sinks you is usually not in the body text. It's after a ※, inside a parenthetical, buried in a conditional clause: "must serve as direct grounds for," "shall be designed as a precondition for commencement." Miss one of those and the rest of the proposal, however excellent, gets marked down as non-responsive. And this is not a problem of reading carefully. It is a problem of **extraction and cross-checking**. On the second pass through a thirty-page call document, a human reads it through the memory of the first pass.

**The deadline is short and an outline cannot be undone.** You get a few weeks between the call and submission. If you research and draft against a wrong outline, by the time you notice, there is no time left to fix it. One line of the outline decides days of research and writing.

Adding an LLM reliably fixes the prose problem. It fixes none of the three above. In one respect it makes things worse — a smooth draft arrives so fast that **the occasion to doubt the outline disappears.**

There was one more thing. A proposal is a **plan for work not yet done**, but drafts keep coming out as if they described a finished design. Lay out completed content topic by topic and it reads as "already done," which loses exactly the *methodology* points the rubric was holding. That's a skeleton problem, not a prose problem, and skeletons are hard to fix after the fact.

So what was needed was not better sentences. It was **an order of operations, and some fixtures**:

1. A step that **extracts** point weights and ※ conditions out of the call document, structurally
2. A table binding those weights **one-to-one** to the outline — the evaluation-response map
3. A gate that rules on whether that mapping has holes **before** research and drafting begin
4. A gate that puts the call document and the finished draft **side by side** afterward

This kit is a personal harness — built by bolting those pieces on, one at a time, while actually writing Korean government R&D proposals — cleaned up and published. The writing rules in [references/](skills/rnd-proposal-writing/references/) likewise didn't come from theory; they were extracted from drafting and revising real joint-proposal modules, and roughly 60 patterns of style, notation, hedging tags, and table conventions are written down there.

Finally, Korean proposal work has two conditions that international tools don't touch. **Submission is in Hangul (`.hwpx`)**, and when the agency supplies a mandated form template, that template's field order *is* your outline. And on a **joint proposal** split across several authors, "does my module read as one document alongside everyone else's" becomes a separate quality bar. This kit handles both.

---

## The central fixture — the evaluation-response map

What separates this kit from a general document-writing tool is not prose. It's this one table, produced after reading the call document and **before any drafting begins**.

| Rubric item | Points | Proposal section | Core scoring argument | Evidence to gather |
|---|---|---|---|---|
| Need | 20 | §1 Need | Low adoption + adoption barriers → case for support | Adoption-rate and barrier statistics |
| Technical development | **30** | §3 Content & differentiation | Domain-specific + on-premise security | Feature/limitation comparison vs. similar platforms |
| Commercialization | **30** | §4 Commercialization strategy | Subscription BM + diffusion via public agencies | Market size, demand, diffusion channels |
| Execution capacity | 20 | §5.1 Roadmap + §5.2 Capability | Staged milestones + institutional capability | [needs sourcing] track record |

*(excerpted from the bundled example, [`examples/rnd-proposal-demo/01_rfp_analysis.md`](examples/rnd-proposal-demo/01_rfp_analysis.md))*

What the table does is simple. **A blank cell means the outline is wrong.** A rubric item with no corresponding section means you are discarding that item's points outright, and a cell that only says "emphasize X" means there is no scoring argument yet. Putting weights and page shares side by side also makes "a 30-point item gets the same space as a 20-point item" visible *before* anyone writes a word.

The table then gets reused throughout the pipeline. The investigator receives the "evidence to gather" column as a work order, the writer keeps the table open while drafting, and the reviewer rules against it at both gates.

**What the gates actually caught.** In the bundled demo, gate 1 flagged as [required] that a mandatory requirement — personal-data protection and security — had been folded into the execution-capacity section with neither its own subsection nor a row in the response map, and had it promoted to §5.3. It also flagged that the 30-point items had only a 3-percentage-point page advantage over the 20-point items, forcing the allocation to be redone. After drafting, gate 2 caught that the differentiation comparison table was benchmarking against general-purpose AI tools and in-house enterprise builds rather than the "similar platforms" the call actually specified — the table was plausibly filled in, but aimed at the wrong target. The rulings are preserved verbatim in [`02_design_gate.md`](examples/rnd-proposal-demo/02_design_gate.md) and [`05_review.md`](examples/rnd-proposal-demo/05_review.md).

> **On A/B measurement.** This repository does not yet contain a head-to-head audit against vanilla Claude Code. A sister kit built on the same design philosophy does, so if you want numbers on what the gate structure actually changes, see [the policy-research-kit audit](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md). Those figures belong to that kit — don't read them as this one's performance.

---

## Pipeline

```
Call/RFP analysis (rfp-analyst — requirements, rubric, weights, ※ conditions; 4-way project typing)
  → Outline + evaluation-response map
  → 🚦 Gate 1: design review (reviewer mode 1 — approve / conditional / reject)
  → ★ You approve the outline and the response map  ← your intervention point
  → Evidence gathering (investigator — 3-tier source grading, every fact sourced)
  → Drafting (writer — skeleton per project type, aimed at the rubric)
  → 🚦 Gate 2: draft review (reviewer mode 2 — five axes)
  → Korean conversion (hwpx-exporter — table row counts verified 1:1)
```

**Why two gates.** Gate 1 protects *cost* — once research and drafting finish against a wrong outline, there is no way back inside the deadline. Gate 2 protects against *overconfidence* — a finished draft looks convincing, and doubting your own text is hard. The reviewer is a **different agent from the writer** and is read-only, so a structure where someone signs off on their own work simply cannot form. Rulings persist as files.

Deadlock is also prevented. If an item has been raised twice and is still unresolved, it is recorded as "residual risk" and the pipeline proceeds. For a document with a deadline, submitting beats perfecting.

**4-way project typing.** The type is determined from the call before anything else, because the outline standard and the drafting skeleton differ by type.

| Type | Skeleton |
|---|---|
| Technology development (TRL, performance targets, commercialization) | Standard 6 sections (need / objectives & content / strategy, structure, schedule / impact & utilization / capability / budget) |
| Commissioned research or policy-formulation service | Plan-form 3 parts (direction → methodology & process → sample outputs) |
| Application-form programs (mandated form supplied) | The form's fields *are* the outline — parse the form, keep its order |
| One module of a joint team proposal | Plan-form 3 parts + conformity to the team's house format |

---

## Install

```
/plugin marketplace add parkjui92/rnd-proposal-kit
/plugin install rnd-proposal-kit@rnd-proposal-kit
```

Restart Claude Code and the orchestrator picks up requests about proposals, R&D plans, and project applications automatically. Prompts work in Korean or English; the proposal output is Korean-first.

---

## How to use it

### Scenario 1 — From scratch, with just the call document

```
Draft a proposal from the attached call document.
I've also attached notes on our institution's strengths and prior track record.
```

The call document (.hwpx/.pdf/.docx/URL) is parsed for mandatory requirements, point weights, ※ conditions, and format constraints; the project type is determined; then the outline and evaluation-response map are built. Gate 1 checks the mapping for holes, and **then it stops and shows you the outline.** Approve, and it continues into research → drafting → gate 2 → hwpx.

The pipeline pauses twice (outline approval, then the final report). You can step away in between.

### Scenario 2 — A commissioned-research or policy-formulation project

```
This isn't technology development — it's a policy-formulation service contract.
Use the plan-form skeleton.
```

For this type the points hang on **how you will carry the work out**, not on what you will build. So the skeleton changes: direction (objective stated up front + design principles) → methodology (staged process table, an N-axis analytical framework, an expert-consultation plan, quality-control principles) → sample outputs (a preview of deliverables plus a disclaimer naming exactly how the final figures get fixed). The register locks to describing execution rather than asserting finished results.

One real commissioned-research RFP has been run end to end through this path, producing a 7-chapter hwpx with 11 tables.

### Scenario 3 — Only my module of a joint team proposal

```
It's a team proposal and I'm responsible for part 2-3.
I'll attach my teammates' drafts — make mine fit alongside theirs.
```

The requirement here differs from solo authoring. The goal isn't "write well," it's **"read as one document alongside what other people wrote."** In module mode the kit first reads teammates' drafts as a style sample, then writes with □◯－ Unicode bullet hierarchy instead of Markdown headings, matches sentence endings to the team's integrated-document convention (nominal endings), and runs an exhaustive check for banned verb forms. Internal working markers, other authors' names, and bold are stripped from the submission copy but preserved in full in a separate note. Cross-references to adjacent modules ("on the basis of what was derived in 1-N…") are stated explicitly.

### Scenario 4 — Audit an existing draft against the point weights

```
Check chapter 4 against the evaluation-response map — is it thin relative to its weight?
```

Nothing gets rewritten from scratch. Only the reviewer is called back in, placing the call document and the draft side by side: a requirement-satisfaction checklist, a rubric-by-rubric check sorted by point weight, and revision requests that each carry location, problem, and fix. You will not get "the evidence is weak." You get "§3.2's '30% performance improvement' has no baseline value and no source → cite the market benchmark figure from the evidence file as the baseline."

### ★ How to intervene at the outline approval gate

When the pipeline stops and shows you the outline and the response map, that is **the cheapest point at which to change direction**. Just say it:

```
Rebuild chapter 3 around differentiation
Commercialization is worth 30 points and it's getting far too little space
The ※ note about "preconditions for commencement" isn't mapped to any section
Give me more title options — lean toward the shorter ones
```

Direction-setting language like the project title and the background statement is presented as **multiple candidates with their emphases noted** rather than a single fixed version (concise ones listed first). You pick.

### When the agency supplies a mandated form

Drop the agency's form (.hwp/.hwpx) into `_workspace/00_input/` and the kit parses it, builds the outline **in the form's own field order**, and converts at the end via the form-filling path. Proprietary institutional templates are not included in this repository (bring-your-own-template) — you supply yours at runtime.

### When the evidence doesn't convince you

```
Chapter 2's market evidence is thin. Verify it against the original statistics
Re-check the source for this figure
```

The investigator attaches both a source and a **confidence grade** to every figure — ★primary (official government or international-organization documents) / ★secondary (academic, press, evaluation bodies) / ▲aggregated or estimated (third-party aggregators, which carry a mandatory "verify against the official source table" footnote). What was checked and what wasn't are separated as 〔verified〕/〔unverified〕, and whatever remains is written up as a "residual verification plan." Evidence that couldn't be found is not invented; it is collected under "unsourced items," which the writer picks up as `[needs sourcing]`.

---

## What you get

Not one document — **an auditable record set**.

| File | Contents |
|---|---|
| `01_rfp_analysis.md` | Structured call analysis — requirements, point weights, ※ conditions, project type, outline, **evaluation-response map** |
| `02_design_gate.md` | Gate 1 ruling — what was flagged as [required] and why |
| `03_evidence.md` | Evidence ledger — source and confidence grade per fact, plus unsourced items |
| `04_proposal.md` | Body draft |
| `05_review.md` | Gate 2 review — requirement checklist, rubric-by-rubric check, revision requests, residual risk |
| `06_proposal.hwpx` | Final submission file |

*(Numbering follows the bundled example folder. On a real run these accumulate in the same order under `_workspace/` in your working directory.)*

Which means that if you lose, you can reconstruct why — and that the same evidence is reusable for the next call.

**A worked example is bundled** — [examples/rnd-proposal-demo/](examples/rnd-proposal-demo/) contains the whole run from design through the final `.hwpx`. It is a **synthetic demo** against a fictional call, at reduced scale (no real client deliverables are included). But the evidence discipline is real: only the key figures were actually verified, with URLs attached, and everything else was left as `[needs sourcing]` — holding that honesty rule even in a demo is itself part of the kit. The example also preserves the point where "5.3% adoption rate" and "52.7% usage rate" are flagged as two different indicators that must not be conflated.

---

## The team

| Agent | Role | Skill |
|---|---|---|
| `rfp-analyst` | Five-part extraction from the call · 4-way project typing · outline and response map | `rnd-rfp-analysis` |
| `proposal-reviewer` | Design gate (mode 1) + draft review (mode 2) · **READ-ONLY** | `rnd-proposal-review` |
| `research-investigator` | Market, technology, prior work, competitive evidence | `rnd-research` (+ built-in geo-search) |
| `proposal-writer` | Body drafting on the type-appropriate skeleton | `rnd-proposal-writing` (+ 4 references) |
| `hwpx-exporter` | `.hwpx` conversion (mandated-form filling takes priority) | `rnd-hwpx-export` |

The orchestrator `rnd-proposal-orchestrator` coordinates them. Partial re-runs ("redo the design," "just chapter 5 again," "regenerate the hwpx only") go through the same skill and update only the affected stage.

**Writing references** — rule sets the writer reads and applies as needed.

- [`plan-style-module.md`](skills/rnd-proposal-writing/references/plan-style-module.md) — the plan-form 3-part skeleton: objective stated up front, four required methodology elements, the three-way mapping table for sample outputs with its preview disclaimer, and three argumentation patterns
- [`style-devices.md`](skills/rnd-proposal-writing/references/style-devices.md) — fixed roles for notation (「」〈〉〔〕), three sentence-ending modes, seven hedging tags, a table catalogue, the 〔figure prompt〕 specification, and rules for figures and sources
- [`team-module-mode.md`](skills/rnd-proposal-writing/references/team-module-mode.md) — joint-proposal module mode: Unicode bullet hierarchy, banned-form checking, three-stage marker isolation, mandatory integration note
- [`proposal-structure.md`](skills/rnd-proposal-writing/references/proposal-structure.md) — detail on the standard sections for technology-development projects

> **Built-in geo-search.** Default web search is pinned to a US locale. The bundled wrapper searches in the target country's language and region (Japanese cases in Japanese), which is what it takes to reach local primary material. Without an API key it falls back to standard search, so it is optional.

---

## Requirements and fallbacks

- **`.hwpx` conversion** requires the [kordoc](https://github.com/chrisryugj/kordoc) MCP server. Without it, the pipeline still runs and stops at Markdown.
- **Without team-API support**, the same pipeline runs via sequential foreground `Agent` calls. The phase order and the artifact file contract are identical.
- Setup, keys, and model selection: [docs/runtime-notes.md](docs/runtime-notes.md).

## Limitations

- **Gates reduce errors; they don't eliminate them.** The reviewer runs on a model from the same family as the writer and can share its blind spots. Final responsibility stays with a human.
- **This repository has no measured A/B against vanilla.** See the sister kit's [audit record](https://github.com/parkjui92/policy-research-kit/blob/main/docs/vanilla-vs-kit.md) — but those figures are that kit's, not this one's.
- **If the call publishes no rubric**, a generic evaluation frame is applied provisionally and labeled as such. The response map is correspondingly less reliable.
- **If a mandated form fails to parse**, conversion falls back to standard hwpx generation — format compliance then needs manual checking.
- **The last stretch into a team's `.hwp` file is manual.** Pasting out of hwpx can drop tables, so the kit also emits the tables as HTML plus a replacement guide to cover that gap.
- This kit is shaped by **Korean government R&D conventions** (weighted rubric scoring, hwpx submission, mandated forms). In other contexts you'll want to adjust the outline skeletons and review axes.

## Further reading

- [docs/verification-gates.md](docs/verification-gates.md) — the two-stage gate design methodology, if you want to build your own
- [docs/runtime-notes.md](docs/runtime-notes.md) — fallbacks, dependencies, key setup
- [examples/](examples/) — the full artifact set and the order to read it in

## Series

Sister kits and standalone skills built on the same design philosophy:

**Agent-team kits** — [policy-research-kit](https://github.com/parkjui92/policy-research-kit) (policy research reports) · [socsci-paper-kit](https://github.com/parkjui92/socsci-paper-kit) (social science papers)

**Authoring kit** — [lecture-deck-kit](https://github.com/parkjui92/lecture-deck-kit) (HTML lecture decks with in-browser live editing)

**Standalone skills** — [fact-verify](https://github.com/parkjui92/fact-verify) (source verification) · [paper-proofread](https://github.com/parkjui92/paper-proofread) (Korean academic proofreading) · [form-tailor](https://github.com/parkjui92/form-tailor) (institutional document formats) · [report-to-brief](https://github.com/parkjui92/report-to-brief) (report compression)

## License

[MIT](LICENSE). No proprietary institutional templates and no real client deliverables are included (bring-your-own-template principle).
