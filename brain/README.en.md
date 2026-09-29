# 🧠 Second Brain

[🇧🇷 Português](./README.md) · 🇺🇸 **English**

This whole repository is an **[Obsidian](https://obsidian.md/) vault**. This is where knowledge grows across the phases: what I **know**, not just what I studied. Notes are personal and written in Portuguese.

## How it works

| Note type | Where | Question it answers |
|---|---|---|
| **Mission note** | `tracks/NN-name/notes/` | "What did I study today?" (mission evidence) |
| **Concept note** | [`concepts/`](./concepts/) | "What do I know about X?" (one concept per note, grows over time) |
| **Map** | [`maps/`](./maps/) | "How do this phase's concepts connect?" (one per phase) |

**Rules:**

1. **Only create a concept note the second time a concept shows up.** The first time, it stays in the mission note.
2. **Write it in your own words.** Copying doesn't stick; Claude may suggest a note is worth writing, but never writes it for you.
3. **Standard Markdown links** (`[loop](../concepts/loop.md)`), never `[[wikilinks]]` — so links also work on GitHub.
4. **Flashcards:** the *Ask yourself* section uses the `Question::Answer` format and the `#flashcards` tag. The **Spaced Repetition** plugin schedules reviews; a review of ≥ 15 min counts as a **minimum session** in [`LOG.md`](../LOG.md).
5. Personal drafts go in `privado/`, which is **not** pushed to GitHub (and has no backup — nothing important there).

## Setup (mission M1.6b)

1. Install Obsidian → *Open folder as vault* → pick the cloned repository folder.
2. *Settings → Core plugins*: enable **Templates** (the `templates/` folder is already configured).
3. *Settings → Community plugins*: install and enable **Obsidian Git** and **Spaced Repetition**.
4. In Obsidian Git, enable *auto commit-and-sync* (e.g. every 10 min) — commits use the `noreply` email set in M1.6.

## Achievement

🕸️ **Second Brain:** 25 interlinked concept notes. See the [ROADMAP](../ROADMAP.en.md#regras).
