# Visuais pintados, estado único em progress.yml e QA no CI

O repositório foi renomeado para `road-to-ai-engineer` e ganhou identidade visual: pinturas geradas por IA (feitas pelo dono no Gemini/ChatGPT) servem de fundo, e todo texto sobre elas é vetor (Cinzel/Cormorant) composto por `scripts/compose_art.py`, porque modelos de imagem erram letras. O Mapa dos Nove Círculos é SVG com estados por classe CSS, para ser atualizado sem regenerar imagem. O progresso, antes copiado em ~12 lugares, passou a viver só em `progress.yml`; `scripts/sync.py` gera badges, caixa de missão, painéis, tabelas de fase, datas de conquistas, ficha e mapa, e `scripts/qa.py` + `sync.py --check` rodam no CI a cada push.

## Considered Options

- **Geração de imagem pela API do Gemini:** adiada — exige plano pago; o dono gera no app e sobe em `assets/incoming/`.
- **Banner claro e escuro:** abandonado quando a arte virou pintura escura; uma versão serve aos dois temas.
- **Manter o progresso manual até a Fase 5:** rejeitado — 12 meses de risco de números divergentes. O chefão da F5 passou a ser reescrever `sync.py`/`qa.py` com código próprio, testes e CI do dono.

## Consequences

- A `/mestre` edita `progress.yml` e roda o sync; nunca edita badges ou painéis à mão.
- Qualquer edição manual fora de sincronia deixa o CI vermelho.
- A conquista 🤖 *Automatizado* vale só para um workflow escrito pelo dono (o de QA foi escrito pelo Claude).
