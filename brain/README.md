# 🧠 Segundo Cérebro

🇧🇷 **Português** · [🇺🇸 English](./README.en.md)

Este repositório inteiro é um **vault do [Obsidian](https://obsidian.md/)**. Aqui fica o conhecimento que cresce ao longo das fases: o que eu **sei**, não só o que eu estudei. As notas são pessoais e escritas em português.

## Como funciona

| Tipo de nota | Onde | Pergunta que responde |
|---|---|---|
| **Nota de missão** | `tracks/NN-nome/notes/` | "O que eu estudei hoje?" (evidência da missão) |
| **Nota de conceito** | [`concepts/`](./concepts/) | "O que eu sei sobre X?" (1 conceito por nota, cresce com o tempo) |
| **Mapa** | [`maps/`](./maps/) | "Como os conceitos desta fase se conectam?" (um por fase) |

**Regras:**

1. **Só crie uma nota de conceito quando o conceito aparecer pela segunda vez.** Na primeira, ele fica na nota da missão.
2. **Escreva com as suas palavras.** Copiar não fixa conhecimento; o Claude pode sugerir que algo merece nota, mas não escreve por você.
3. **Links Markdown padrão** (`[loop](../concepts/loop.md)`), nunca `[[wikilinks]]`: assim os links funcionam no GitHub também.
4. **Flashcards:** a seção *Pergunte-se* usa o formato `Pergunta::Resposta` e a tag `#flashcards`. O plugin **Spaced Repetition** agenda as revisões; uma revisão de ≥ 15 min conta como **sessão mínima** no [`LOG.md`](../LOG.md).
5. Rascunhos pessoais vão em `privado/`, que **não** vai para o GitHub (e não tem backup — nada importante lá).

## Configuração (missão M1.6b)

1. Instale o Obsidian → *Open folder as vault* → escolha a pasta do repositório clonado.
2. *Settings → Core plugins*: ative **Templates** (a pasta `templates/` já está configurada).
3. *Settings → Community plugins*: instale e ative **Obsidian Git** e **Spaced Repetition**.
4. No Obsidian Git, ative o *auto commit-and-sync* (ex.: a cada 10 min) — o e-mail `noreply` configurado na M1.6 é usado nos commits.

## Conquista

🕸️ **Segundo Cérebro:** 25 notas de conceito interligadas. Veja o [ROADMAP](../ROADMAP.md#regras).
