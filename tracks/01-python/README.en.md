# 🐍 Phase 1 — Python

[🇧🇷 Português](./README.md) · 🇺🇸 **English**

> **Duration:** 10 weeks · **Phase XP:** 670 · **Weekly goal:** 4 sessions of ≥ 30 min
> **Every month:** one [networking outpost](../../ROADMAP.en.md#postos-avancados) (+15 XP).
> **Goal:** program confidently in Python — from `print` to classes, files and tests.
> **Status:** 🔒 unlocks when the [Phase 0](../00-tutorial/README.en.md) boss is defeated.

---

## 📚 Resources

| | Resource | Why |
|---|---|---|
| ⭐ Main | [CS50P — CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Free, subtitled, auto-graded problem sets and a **free certificate**. Lectures on [YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V). |
| 🇧🇷 Portuguese alt. | [Curso em Vídeo — Python 3 (World 1)](https://www.cursoemvideo.com/curso/python-3-mundo-1/) | If a CS50P lecture feels heavy, watch the same topic here first. |
| 📖 Book | [Think Python, 3rd ed.](https://allendowney.github.io/ThinkPython/) · [PT translation](https://rodrigocarlson.github.io/PensePython3ed/) | Reference and re-reading; runs on Colab. |
| 🏋️ Extra practice | [Exercism — Python](https://exercism.org/tracks/python) | Short exercises with free mentoring. |

**How to study each CS50P lecture:** watch the lecture (split across 2 sessions if needed) → write a note in `notes/` using the [template](../../templates/nota-de-estudo.en.md) → solve the *Problem Set* in `exercises/` → stuck? `/teach <topic>`.

---

## 🗒️ Missions

- [ ] **M1.1 · Functions and variables** — 40 XP
  CS50P **Lecture 0** + Problem Set 0.
- [ ] **M1.2 · Conditionals** — 40 XP
  CS50P **Lecture 1** + Problem Set 1.
- [ ] **M1.3 · Loops** — 40 XP
  CS50P **Lecture 2** + Problem Set 2.
- [ ] **M1.4 · Exceptions** — 40 XP
  CS50P **Lecture 3** + Problem Set 3.
- [ ] **M1.5 · Libraries** — 40 XP
  CS50P **Lecture 4** + Problem Set 4.
- [ ] **M1.6a · Install the tools** — 15 XP · 🏅 *Left Colab*
  Install Python, [Git](https://git-scm.com/downloads) and [VS Code](https://code.visualstudio.com/docs/python/python-tutorial) (with the Python extension) following the guide for your system: [Windows](https://code.visualstudio.com/docs/setup/windows) · [macOS](https://code.visualstudio.com/docs/setup/mac) · [Linux](https://code.visualstudio.com/docs/setup/linux). On Windows, install Python from [python.org](https://www.python.org/downloads/windows/) and tick **"Add python.exe to PATH"**. Open the VS Code terminal and run `python --version` and `git --version` (on macOS/Linux it may be `python3`). Create an `ola.py` file and run it **outside Colab**.
  **Evidence:** a note `notes/ambiente-local.md` with your system, the versions and what went wrong along the way.
- [ ] **M1.6b · Git from the terminal** — 20 XP
  **Before the first commit**, set your private GitHub email: `git config --global user.email "<id>+<username>@users.noreply.github.com"` (find it in *GitHub → Settings → Emails*; see [SECURITY](../../SECURITY.md)). Clone this repo (`git clone`), edit `LOG.md` locally and publish with `git add`, `git commit` and `git push`. On Windows, login may open a browser window; on macOS/Linux, use the [GitHub CLI](https://cli.github.com/) (`gh auth login`) or a token.
  **Evidence:** a commit of yours made from the terminal, with the `noreply` email.
- [ ] **M1.6c · Virtual environment** — 15 XP
  In the repo folder, create and activate a virtual environment: `python -m venv .venv`, then `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (macOS/Linux). Install a package (`pip install requests`) and run a script that uses it. The `.venv/` folder is already in `.gitignore`: check that it does **not** go into the commit.
  **Evidence:** a *Virtual environment* section in `notes/ambiente-local.md`, with the commands that worked on your system.
- [ ] **M1.6d · Second brain** — 30 XP
  Install [Obsidian](https://obsidian.md/) and open the cloned repository folder as a vault (*Open folder as vault*). The basic configuration ships with the repo (Markdown links, templates folder). In *Settings → Community plugins*, install and enable **Obsidian Git** (syncs with GitHub) and **Spaced Repetition** (flashcards). Read [`brain/README.en.md`](../../brain/README.en.md) and create your **first 2 concept notes** in `brain/concepts/` with the [concept template](../../templates/conceito.en.md), linked from a mission note.
  **Evidence:** the 2 notes in `brain/concepts/` and a commit made by Obsidian Git.
- [ ] **M1.7 · Tests** — 40 XP · 🏅 *Tested*
  CS50P **Lecture 5** + Problem Set 5 (`pytest`).
- [ ] **M1.8 · Files** — 40 XP
  CS50P **Lecture 6** + Problem Set 6 (read/write CSV).
- [ ] **M1.8b · The spell on your own file** — 30 XP
  Go back to the [M0.7](../00-tutorial/README.en.md) model, now **locally**, in your virtual environment (`pip install transformers torch`). Write a script that reads a file of **your own** (exported messages, reviews, notes, ~50 lines; strip names and personal data first), classifies the sentiment of each line and writes a CSV with the result and the count per sentiment.
  **Evidence:** the script in `exercises/`, the output CSV **with no personal data**, and 3 lines on where the model failed on your kind of text.
- [ ] **M1.9 · Regular expressions** — 20 XP
  CS50P **Lecture 7** + at least 2 exercises from Problem Set 7.
- [ ] **M1.10 · Object-oriented programming** — 50 XP
  CS50P **Lecture 8** + Problem Set 8.
- [ ] **M1.11 · Et cetera** — 10 XP
  CS50P **Lecture 9** (no problem set). A note with the 3 features that surprised you most.

**Mission total:** 470 XP

---

## ⚔️ Elite mini-boss — The Sentinel · 50 XP

After M1.5, **no tutorial and no peeking at solutions**: a terminal program from scratch, in up to 3 sessions, that solves a small problem of yours (e.g. a monthly expense calculator, a chore picker, a review quiz). You may read the Python docs; you may not copy ready-made code or ask an AI to write it.

- [ ] Code in `exercises/sentinela/`, running, handling invalid input.
- [ ] In the mission note: where you got stuck and how you got unstuck.

---

## 🐉 Boss — The Toolmaker · 150 XP

Build the **CS50P Final Project** as **its own repository** on your GitHub, following the [boss standard](../../ROADMAP.en.md#padrao-de-chefao):

- [ ] A command-line tool that solves **your own** problem (e.g. organizing expenses from a CSV, generating study plans, a unit converter, a terminal game).
- [ ] At least 3 functions tested with `pytest`.
- [ ] A `README.md` from the [boss template](../../templates/chefao-readme.en.md): the problem, how to install, how to use, and the **demo** (a terminal GIF or sample output).
- [ ] A short post on what the tool does and what you learned.
- [ ] Repo link added to *Featured projects* in the [main README](../../README.md).
- [ ] (Optional) Submit to CS50P and earn the certificate.

Defeating the boss = **Level 2 · Pythonista** 🐍 and unlocks [Phase 2 — Data & Math](../02-data-math/README.en.md).
