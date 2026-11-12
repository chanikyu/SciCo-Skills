---
name: scientific-workflow-viz
description: 'Use when the user wants a high-quality BioRender-style scientific figure — workflow, pipeline, mechanism, comparison, timeline, or multi-panel infographic — DRAWN as an editable vector file in the VectorCraft desktop app (REQUIRED; install from https://getartcraft.com/apps/vectorcraft), with exact real-text labels and SVG/PDF/PNG export. Follows a 5-step process (analyze the content → choose the design → set the components → choose the illustrations → draw it in VectorCraft) with a FLEXIBLE layout (any number of panels/steps/stages; default 16:9). Triggers — "워크플로우 그림", "scheme/pipeline/mechanism figure", "BioRender 스타일", or "scientific workflow infographic". Invoke when the user asks to visualize a method/process/comparison as a figure.'
---

# Scientific Workflow Viz

Draw a high-quality, BioRender-style scientific figure **directly in the VectorCraft desktop app** — an editable vector file with real text labels, not an AI-generated image. Steps 1–4 design the figure; step 5 draws it, looks at the render, and fixes it.

**Requirement — VectorCraft must be installed:** <https://getartcraft.com/apps/vectorcraft> (source: <https://github.com/storytold/vectorcraft>). Check this before step 1. If the app is missing, **stop and ask the user to install it from that link** — do not fall back to an image prompt or another renderer, and do not install it yourself.

The layout is **flexible** — do NOT force a fixed 3-panel structure. Choose the design that fits the content.

## The 5-step process (follow in order)

1. **Analyze the content.** Read what the figure must convey. Extract the key entities, the steps/relationships, and the single main message. If unsure about a method, read the docs/code first — never invent steps.
2. **Decide the design type.** Pick the layout that matches the content (see the menu below). The number of panels / steps / stages is whatever the content needs — 2, 3, 4, a cycle, columns, levels, etc. Do not default to 3 panels.
3. **Set the components.** Decide the concrete blocks: how many panels/steps/stages, what each one is, and how they connect (arrows, increasing scope, side-by-side, loop…).
4. **Choose the illustrations.** For each component, decide the icons / mini-diagrams (microbe cluster, abundance bar chart, DNA helix, molecule, gut-lining, matrix grid, network, table, gauge, etc.). Ground them in the real content.
5. **Draw it in VectorCraft.** Build steps 2–4 in the app with the house style and the arrow rules, export a PNG, look at it, and fix what you see — details in "Step 5 in detail" below.

## House style (always)

- **Title & type:** give the figure a short title and name its type ("workflow infographic", "pipeline diagram", "comparison figure", "mechanism schematic", "timeline", …).
- **Aesthetic:** professional flat scientific icons; white background; dark-grey text; clean typography; soft color-coded sections with rounded borders / colored header bars; clear arrows.
- **Size:** **default 16:9** unless the user specifies otherwise (e.g. square, A4, poster).
- **Color:** distinct soft color per section, used consistently. Use the deck's brand accent if part of one (e.g. `#4A90E2` for xMeta).
- **Honesty:** ground in the real method; tag "(optional)" / "(proposed)"; don't invent stages.

## Design menu (step 2 — pick what fits, not fixed)

- **Linear pipeline** — input → step 1 → step 2 → … → output (one row).
- **Multi-panel** — 2–4 colored panels (e.g. Input / Core Workflow / Output; or Problem / Approach / Result). Panel count follows the content.
- **Comparison** — 2+ side-by-side columns, head-to-head on shared rows.
- **Stacked levels** — top-to-bottom or left-to-right by increasing scope (e.g. species → community → host).
- **Cycle / loop** — steps arranged in a circle.
- **Mechanism / network** — nodes + labeled arrows (e.g. T → M → Y mediation, cross-feeding handoff).
- **Hybrid** — e.g. a core pipeline with an optional branch, or a panel that itself contains a sub-diagram.

## Arrows & flow (keep connectors clean)

Mixed, bent, or randomly-colored arrows are what make a workflow figure look off. **Apply these
rules to every connector you draw:**

- **Single global flow direction (the #1 rule)** — pick ONE reading direction for the whole figure
  (everything **left→right**, or everything **top→bottom**) and make **every arrow point that
  way; none ever points backward (up / left / return)**. Forks and merges are completely fine — a
  backward or ambiguous arrow just means a node is in the **wrong position** for that flow; **move the
  node**, don't bend the arrow. This — not arrow thickness — is what makes a workflow read as "which
  way does this even go?".
- **One arrow style** — flat solid arrows, uniform thickness, a single clean arrowhead; **all**
  arrows use it. Don't mix big block/chevron arrows with thin arrows at random.
- **No block / chevron / tapered arrows** — these are what read as "weird". **Every** arrow is the
  same **thin** flat arrow. Do NOT draw a "larger main-spine arrow".
- **Exactly one of each node** — each box appears once; NEVER duplicate a box to route a connection.
  A duplicated node (e.g. two "abundance table" boxes) is the classic sign a merge was not routed.
- **Position forks & merges precisely (this is the real fix)** — branching and re-joining are normal;
  the trick is WHERE the node sits. Decide exactly **where the fork splits** and **where its branches
  re-join**, and place the **single merge node at the convergence point so BOTH branches reach it with
  short forward arrows** — e.g. centered just below both branches (top→bottom flow), or in a shared
  column at both branches' right ends (left→right flow). A node only gets duplicated (two
  "abundance table" boxes) when its position is left implicit — pin it down.
- **Straight, not bent** — no curved / elbow / S-shaped / diagonal connectors between distant
  panels (they tangle). Arrows are strictly horizontal or vertical.
- **Neutral color** — connectors are **dark-grey** by default; color an arrow **only** to mark a fork
  (the two fork arrows take their track colors; every other arrow is dark-grey).
- **Lay panels so arrows CAN be straight** — reading order in a single row, or a **serpentine**
  (row 1 left→right, row 2 right→left). A long **bent "return" connector is a layout smell** — re-order
  the panels instead of bending an arrow back across the figure.
- **One arrow per connection**, centered on panel edges; no double-heads unless truly bidirectional.

Arrow checklist — verify it on the exported PNG:
`ARROWS: every connector is the SAME thin flat dark-grey arrow with one arrowhead, strictly horizontal or vertical — NO curved/elbow/diagonal arrows and NO wide block/chevron/tapered arrows anywhere. Each box appears exactly once (never duplicate a node to route a line). Forks and merges are allowed but POSITIONED so every arrow flows forward: the fork splits at a stated point and ONE merge node sits where both branches reach it with short straight arrows (never duplicate that node). Only the two fork arrows may take their track colors; all others dark-grey.`

## Step 5 in detail — draw it in VectorCraft

**VectorCraft is required** (<https://getartcraft.com/apps/vectorcraft>). How to start it and send commands:
**[vectorcraft-runtime.md](vectorcraft-runtime.md)**; the sender is `vectorcraft_control.py` in this
skill folder.

1. **Check the app first.** Not installed → stop, give the user the install link, and wait. No
   image-prompt fallback, no other renderer.
2. **Start your own instance** on a free port with a temporary profile (runtime file, section 2).
   Never attach to a VectorCraft the user already has open.
3. **Build the figure** from steps 2–4: new document (16:9 → e.g. 1600 × 900 pt), then panels →
   icons → labels → arrows last. Type every label as a **real text object**. Group each panel and
   the flow arrows under clear names so the file stays editable. A script may compute coordinates
   and send the commands; VectorCraft does the rendering.
4. **Look at it.** Export a PNG and open it — a saved file is not a visual check. Check three
   views, fix the biggest defect first, then re-export:
   - whole figure: main message, reading order, balance, empty or crowded areas;
   - final display size: export at the width it will be shown and confirm every label is readable;
   - zoomed crops: clipped objects, overlaps, text touching borders, arrow start/end points.
5. **Deliver** to the folder the user named (else a per-figure folder): the editable
   `.vectorcraft` file, SVG, PDF, and a PNG preview. Say what you actually checked and what is
   still unresolved — do not claim BioRender-equivalent quality.
6. **Quit only the instance you started**, after saving (runtime file, section 5).

## Examples — figure specs from steps 2–4 (each is ONE design choice, not the only shape)

Write the spec like this before drawing; it is what you build in step 5.

**Multi-panel workflow (3 panels):**
```
Workflow infographic titled "How xReact works." Multi-panel, color-coded, left to right, colored header bars, rounded borders, large arrows. Flat scientific icons, white background, dark-grey text, 16:9.
PANEL (1) "Input" (light-blue): microbial community as a taxa-abundance bar chart + a chemical card "chemical (drug / diet / unknown) + dose".
PANEL (2) "Core xReact Workflow" (cream/yellow): Box 1 "Perturbation Atlas" (chemical x species grid -> growth up/down; "AGORA2 + FVA, calibrated with Maier 2018"); Box 2 "Community Rebalancing" (before/after bars; "reweight -> shifted STRUCTURE, no per-sample simulation"); Box 3 "Functional Change (xFeed)" (metabolite exchange; "shifted FUNCTION"); Box 4 (green, "optional") "Host Outcome (xHost)".
PANEL (3) "Output" (green): before->after bars + list "taxa up/down, metabolites changed".
Large arrows (1)->(2)->(3).
```

**Comparison (2 columns):**
```
Comparison figure titled "Two routes to causal inference." Two side-by-side panels, colored headers, white background, flat icons, 16:9.
LEFT "Mendelian Randomization" (grey): instrument(SNP) -> exposure -> outcome, with a dashed red "pleiotropy" arrow and limitation badges "weak instruments", "needs large GWAS".
RIGHT "xHost" (blue): longitudinal multi-omics -> cross-lagged M(t)->Y(t+1) -> mediator->outcome, badge "E-value sensitivity".
Bottom banner: "Both observational; xHost applies where MR's instruments are too weak."
```

## Pitfalls

- **Don't force 3 panels** — match the design to the content (step 2).
- Don't over-stuff one block — split into steps/boxes.
- Captions = one short phrase; icons carry the meaning.
- Use the deck's accent color; default 16:9.
- Ground in the real method; mark optional/proposed parts.
