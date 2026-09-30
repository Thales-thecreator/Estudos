# Escrita e sincronização (depois de cada vitória)

**Tudo o que é público na saga sai em par PT + EN.** Narre ao jogador em português; grave o original em PT e a tradução em `*.en.md` (mesmo nome), usando o [GLOSSARY-EN.md](./GLOSSARY-EN.md). Toda página nova ganha o seletor de idioma no topo. Issues ficam só em PT.

## 1. Saga (à mão, PT + EN)

- **Cena:** `saga/cenas/NNNN-slug.md` + `.en.md`, numeração sequencial, `# <título>` e `> Missão M?.? · AAAA-MM-DD` (EN: `> Mission M?.? · YYYY-MM-DD`); termine com o bloco `🎨 Prompt da ilustração` ([VISUAIS.md](./VISUAIS.md#vinheta-de-cada-cena-opcional-para-o-jogador)); acrescente uma linha `| Cena N | [título](./cenas/…) · M?.? | <círculo> |` à tabela de `saga/README.md` e `README.en.md`.
- **Capítulo:** `saga/capitulos/NN-slug.md` + `.en.md`; acrescente à tabela de `saga/README.md` e `README.en.md`.
- **Crônica** (`cronica.md` + `.en.md`): só fatos revelados na linha do tempo e nas listas.
- **Ficha** (`ficha.md` + `.en.md`): local, correntes, atributos (1 ponto a cada 100 XP da fase, máx. 10), Manopla, inventário, aliados, pactos. **Nível e XP não**: vêm do sync.

## 2. Estado do jogo (`progress.yml`)

Atualize os campos que mudaram:
- `xp`, `level` (só sobe com XP mínimo **e** chefão da fase), `phase` (ao vencer um chefão), `started`
- `streak.current` / `streak.best`
- `quest.pt` / `quest.en`: próxima missão, com o nome da corrente/etapa (ex.: `"M0.2 · Diário de bordo — Corrente II · Silêncio"`)
- `saga_latest`: título e caminho da cena/capítulo mais recente (PT e EN)
- `achievements`: `"🌱": 2026-10-01` ao desbloquear

Depois rode **`python scripts/sync.py`**: ele atualiza badges, caixa de missão, "estudando agora", painéis, tabelas de fase, datas das conquistas, nível/XP da ficha e o Mapa dos Nove Círculos. **Nunca edite essas partes à mão.** (Requer `pip install pyyaml`.)

## 3. Roadmap e issues

- Marque `[x]` na missão no README da fase (PT e EN).
- Feche a issue da missão (`Thales-thecreator/road-to-ai-engineer`), com `state_reason: completed`.

## 4. Verificar e publicar

1. Se houver imagem nova (print, foto, arte), rode `python scripts/clean_images.py` para tirar GPS e dados de câmera.
2. `python scripts/qa.py` e `python scripts/sync.py --check` precisam passar (o CI roda os mesmos).
3. `git pull --rebase origin main` (o Obsidian Git também faz commits).
4. Commit e push **direto na `main`** (autorização permanente em `.claude/CLAUDE.md`), com mensagem neutra e sem spoilers (ex.: `Saga: M0.1 concluída, Corrente I`).
