<div align="center">

# 🧠 Rumo a AI Engineer

**Minha jornada de estudos em público — do zero em programação até Machine Learning, MLOps, LLMs e AI Engineering.**

[🇺🇸 Read in English](./README.md) · [🗺️ Roadmap](./ROADMAP.md) · [📅 Diário de estudos](./LOG.md)

![Nível](https://img.shields.io/badge/nível-0%20·%20Recruta-6e7681?style=for-the-badge)
![XP](https://img.shields.io/badge/XP-0%20%2F%207000-2ea043?style=for-the-badge)
![Fase](https://img.shields.io/badge/fase-0%20·%20Tutorial-1f6feb?style=for-the-badge)
![Streak](https://img.shields.io/badge/streak-0%20semanas-f0883e?style=for-the-badge)

</div>

<!-- quest:start -->
> - ⚔️ **Missão atual:** o jogo ainda não começou — a primeira corrente espera.
> - 📜 **Último da saga:** [Prólogo: As Cinzas de Aethelgard](./saga/capitulos/00-prologo.md)
> - 🔥 **Streak:** 0 semanas · **Próximo nível:** Aprendiz (faltam 150 XP)
<!-- quest:end -->

---

## 👋 Sobre mim

_Sou Thales Gomes e estou aprendendo em público para me tornar AI Engineer._

- 🎯 **Objetivo:** conseguir minha primeira vaga como ML / AI Engineer
- 🌱 **Estudando agora:** Git, GitHub e hábito de estudo (Fase 0)
- 📫 **Contato:** [LinkedIn](https://www.linkedin.com/in/thales-gomes-2a6a12163/)

---

## 🎮 Progresso

| Fase | Trilha | Semanas | Status | Chefão 🐉 |
|:---:|---|:---:|:---:|---|
| 0 | [Tutorial](./tracks/00-tutorial/) — Git, Colab, hábito | 2 | 🟢 Em andamento | O Guardião do Hábito |
| 1 | [Python](./tracks/01-python/) | 10 | 🔒 | O Construtor de Ferramentas |
| 2 | [Dados & Matemática](./tracks/02-data-math/) — pandas, SQL, estatística, álgebra linear | 10 | 🔒 | O Oráculo dos Dados |
| 3 | [ML Clássico](./tracks/03-classical-ml/) — scikit-learn, Kaggle | 10 | 🔒 | O Kaggler |
| 4 | [Deep Learning](./tracks/04-deep-learning/) — PyTorch, fast.ai | 10 | 🔒 | O Olho da Máquina |
| 5 | [MLOps](./tracks/05-mlops/) — Docker, FastAPI, MLflow, CI/CD | 12 | 🔒 | O Engenheiro de Produção |
| 6 | [LLMs & AI Engineering](./tracks/06-llms-ai-eng/) — RAG, agentes, evals | 12 | 🔒 | O Arquiteto de RAG |
| 7 | [Capstone & Carreira](./tracks/07-capstone-career/) | 8 | 🔒 | O Capstone |
| 8 | [A Caçada](./tracks/08-the-hunt/) — candidaturas e entrevistas | aberta | 🔒 | A Primeira Proposta |

```mermaid
flowchart LR
    F0[F0 Tutorial]:::agora --> F1[F1 Python] --> F2[F2 Dados & Matemática] --> F3[F3 ML Clássico]
    F3 --> F4[F4 Deep Learning] --> F5[F5 MLOps] --> F6[F6 LLMs & AI Eng] --> F7[F7 Capstone] --> F8[F8 A Caçada]
    classDef agora fill:#2ea043,color:#fff,stroke:#2ea043
```

⛓️ **Jogado como um RPG narrativo grimdark**: cada missão avança uma história em [`saga/`](./saga/), publicada em português e inglês.

O jogo completo — missões, XP, níveis, conquistas e todos os materiais gratuitos — está no **[ROADMAP.md](./ROADMAP.md)**.

---

## 🏆 Projetos em destaque

Cada fase termina com um **chefão**: um projeto prático publicado em repositório próprio.

| Projeto | Fase | Stack | Demo |
|---|:---:|---|:---:|
| _Em breve — o primeiro chefão é na Fase 1_ | | | |

---

## 🧰 Stack que estou aprendendo

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?logo=huggingface&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?logo=mlflow&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?logo=postgresql&logoColor=white)

---

## 🗂️ Como este repositório funciona

```
├── ROADMAP.md          # o jogo: fases, missões, XP, níveis, conquistas
│                       #   (todo doc público tem um gêmeo *.en.md)
├── LOG.md              # uma linha por sessão → meta semanal e streak
├── CONTEXT.md          # glossário do vocabulário do jogo
├── tracks/             # uma pasta por fase
│   └── NN-nome/
│       ├── README.md   #   missões + checklist do chefão
│       ├── notes/      #   minhas anotações
│       └── exercises/  #   código e notebooks
├── projects/           # mini-projetos (chefões ganham repositório próprio)
├── saga/               # o RPG: capítulos, ficha do personagem, crônica
├── brain/              # segundo cérebro (vault do Obsidian): conceitos + mapas
├── classroom/          # aulas interativas geradas com a skill /teach do Claude
├── templates/          # modelos de nota e de README de projeto
└── docs/adr/           # decisões sobre a organização do repositório
```

**Ciclo de estudo:** escolher a próxima missão → estudar o material gratuito → escrever a nota → resolver os exercícios → registrar a sessão → ganhar XP. Travou? Gere uma aula curta e interativa com `/teach`, ou pergunte numa comunidade.

**Regras do jogo:** meta semanal (3–4 sessões de 30+ min) em vez de streak diário, XP só com evidência no repositório, e um chefão obrigatório para desbloquear cada fase. Detalhes no [ROADMAP.md](./ROADMAP.md#regras).

---

<a id="jogue-voce-tambem"></a>

## 🎲 Jogue você também

Este roadmap foi feito para receber forks. Para começar a sua partida:

1. **Faça um fork** deste repositório (e confira se o seu e-mail do GitHub está privado — veja o [SECURITY](./SECURITY.pt-BR.md)).
2. **Zere o progresso:** apague as linhas de sessão do `LOG.md`, volte XP/nível para zero nos `ROADMAP*.md` e nos badges do README, desmarque os checkboxes em `tracks/` e reinicie `saga/ficha*.md` e `saga/cronica*.md` (mantenha o prólogo). Apague `saga/cenas/*`.
3. **Deixe com a sua cara:** reescreva o `classroom/MISSION.md`, o *Sobre mim* e o cronograma para a sua vida.
4. **Jogue:** abra o [Claude Code](https://claude.com/claude-code) no seu fork e rode `/mestre começar`. As skills em `.claude/skills/` já vêm junto.

Os pilares da trama são os mesmos para todos — as escolhas não. Dê o crédito conforme as licenças abaixo.

---

## 📄 Licença & segurança

- **Código:** [MIT](./LICENSE) · **Roadmap e notas:** [CC BY-SA 4.0](./LICENSE-CONTENT.md) · **Saga:** [CC BY-NC-SA 4.0](./LICENSE-CONTENT.md) · detalhes em [LICENSE-CONTENT.md](./LICENSE-CONTENT.md)
- Regras de segurança e privacidade deste repositório público: [SECURITY.pt-BR.md](./SECURITY.pt-BR.md)

---

## 📚 Destaques do currículo

Todos os materiais são **gratuitos**. Alguns favoritos:

[CS50P](https://cs50.harvard.edu/python/) ·
[Curso em Vídeo](https://www.cursoemvideo.com/cursos/) ·
[Kaggle Learn](https://www.kaggle.com/learn) ·
[3Blue1Brown](https://www.3blue1brown.com/) ·
[ML Specialization — Andrew Ng](https://www.coursera.org/specializations/machine-learning-introduction) ·
[fast.ai](https://course.fast.ai/) ·
[Zero to Hero — Karpathy](https://karpathy.ai/zero-to-hero.html) ·
[MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) ·
[Made With ML](https://madewithml.com/) ·
[Hugging Face LLM Course](https://huggingface.co/learn/llm-course) ·
[Anthropic Courses](https://github.com/anthropics/courses)

---

<div align="center">

_Aprendendo em público, uma sessão de cada vez._ 🌱

</div>
