# Estudos

Repositório de estudos do zero até a primeira vaga como ML / MLOps / AI Engineer, organizado como um jogo. O dono é iniciante em programação. Escreva em português. O repositório é **público e bilíngue**: todo doc público (READMEs, roadmap, trilhas, saga, templates, SECURITY) tem um par `*.en.md` com seletor de idioma no topo; o `README.md` e o `SECURITY.md` são o original em inglês, com par `*.pt-BR.md`. Ao editar um lado, atualize o outro. Bastidores (`CONTEXT.md`, ADRs, `classroom/`, `.claude/`, `LOG.md`, notas pessoais) e as issues ficam só em PT.

## Onde está o quê

- `ROADMAP.md`: fases, missões, XP, níveis, conquistas e painel do jogador. Fonte da verdade das regras.
- `LOG.md`: uma linha por sessão; dele saem a meta semanal e o streak.
- `CONTEXT.md`: vocabulário do jogo (fase, missão, chefão, sessão, streak...). Use esses termos.
- `tracks/NN-nome/`: missões da fase (`README.md`), `notes/` e `exercises/`.
- `classroom/`: espaço da skill `/teach` — rode-a tratando `classroom/` como o workspace de ensino.
- `docs/adr/`: decisões sobre o repositório.
- `brain/`: segundo cérebro (o repositório é um vault do Obsidian). `concepts/` = notas atômicas de conceito; `maps/` = um mapa por fase. Links sempre Markdown padrão, nunca `[[wikilinks]]`. `privado/` fica fora do git.
- `templates/`: modelos inseridos pelo Obsidian; por isso **sem** seletor de idioma.
- `assets/`: banner e social preview (pintura + título vetorial, gerados por `scripts/compose_art.py`), Mapa dos Nove Círculos (`circles-*.svg`, gerados por `scripts/build_visuals.py`; depois só a `/mestre` troca classes), arte da saga em `art/`, e `incoming/` para imagens recebidas.
- `saga/`: RPG narrativo por cima do roadmap. Só a skill `/mestre` narra; fora dela, não entre em personagem. Nunca decodifique nem revele `.claude/dm/biblia.md.b64` fora da skill.

## Ao ajudar nos estudos

- Missão concluída: marque `[x]` no README da fase, feche a issue, e atualize XP/nível no painel do `ROADMAP.md` e do `ROADMAP.en.md` **e** nos badges de `README.md` e `README.pt-BR.md` (manual até o chefão da Fase 5).
- Ao desbloquear uma fase, detalhe as missões dela a partir do `ROADMAP.md` (pesquise e confira os links antes) e crie as issues com label `mission` / `boss` e `phase-N`. Só a fase atual tem issues.
- Não resolva exercícios pelo dono; guie com perguntas e dicas. Ele está aprendendo. O mesmo vale para as notas de conceito: sugira que algo merece nota, mas não escreva por ele.
- Prefira materiais gratuitos; indique alternativa em PT quando existir.
- Segurança: nunca commite chaves, `.env` ou dados pessoais (ver `SECURITY.pt-BR.md`). Se encontrar algo assim, pare e avise o dono.
- Licenças: código MIT, conteúdo CC BY-SA 4.0, saga CC BY-NC-SA 4.0 (ver `LICENSE-CONTENT.md`). As skills em `.claude/skills/` são MIT do Matt Pocock, exceto `mestre/`.

## Git: commits direto na `main`

Autorização permanente do dono: neste repositório, commits de progresso de estudo (missões, saga, painel de XP, docs) vão **direto para a `main`**, mesmo que a sessão comece em outra branch. Antes do push, `git pull --rebase origin main` (o Obsidian Git também faz commits). Não abra PR para isso.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (`Thales-thecreator/road-to-ai-engineer`). See `.claude/docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `.claude/docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `.claude/docs/agents/domain.md`.
