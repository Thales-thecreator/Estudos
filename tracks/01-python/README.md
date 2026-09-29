# 🐍 Fase 1 — Python

🇧🇷 **Português** · [🇺🇸 English](./README.en.md)

> **Duração:** 10 semanas · **XP da fase:** 670 · **Meta semanal:** 4 sessões de ≥ 30 min
> **Todo mês:** um [posto avançado de networking](../../ROADMAP.md#postos-avancados) (+15 XP).
> **Objetivo:** programar em Python com segurança — do `print` a classes, arquivos e testes.
> **Status:** 🔒 desbloqueia ao vencer o chefão da [Fase 0](../00-tutorial/).

---

## 📚 Materiais

| | Material | Por quê |
|---|---|---|
| ⭐ Principal | [CS50P — CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Gratuito, com legendas, exercícios corrigidos automaticamente e **certificado gratuito**. Aulas no [YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V). |
| 🇧🇷 Alternativa PT | [Curso em Vídeo — Python 3 (Mundo 1)](https://www.cursoemvideo.com/curso/python-3-mundo-1/) | Se uma aula do CS50P ficar pesada, veja o mesmo assunto aqui primeiro. |
| 🇧🇷 Livro PT | [Pense em Python, 3ª ed. (tradução)](https://rodrigocarlson.github.io/PensePython3ed/) | Consulta e releitura; roda no Colab. |
| 🏋️ Treino extra | [Exercism — Python](https://exercism.org/tracks/python) | Exercícios curtos com mentoria gratuita. |

**Como estudar cada aula do CS50P:** assista à aula (pode ser em 2 sessões) → faça a nota em `notes/` usando o [template](../../templates/nota-de-estudo.md) ([EN](../../templates/nota-de-estudo.en.md)) → resolva o *Problem Set* em `exercises/` → travou? `/teach <assunto>`.

---

## 🗒️ Missões

- [ ] **M1.1 · Funções e variáveis** — 40 XP
  CS50P **Lecture 0** + Problem Set 0.
- [ ] **M1.2 · Condicionais** — 40 XP
  CS50P **Lecture 1** + Problem Set 1.
- [ ] **M1.3 · Loops** — 40 XP
  CS50P **Lecture 2** + Problem Set 2.
- [ ] **M1.4 · Exceções** — 40 XP
  CS50P **Lecture 3** + Problem Set 3.
- [ ] **M1.5 · Bibliotecas** — 40 XP
  CS50P **Lecture 4** + Problem Set 4.
- [ ] **M1.6a · Instalar as ferramentas** — 15 XP · 🏅 *Saí do Colab*
  Instale Python, [Git](https://git-scm.com/downloads) e o [VS Code](https://code.visualstudio.com/docs/python/python-tutorial) (com a extensão Python) seguindo o guia do seu sistema: [Windows](https://code.visualstudio.com/docs/setup/windows) · [macOS](https://code.visualstudio.com/docs/setup/mac) · [Linux](https://code.visualstudio.com/docs/setup/linux). No Windows, instale o Python pelo [python.org](https://www.python.org/downloads/windows/) marcando **"Add python.exe to PATH"**. Abra o terminal do VS Code e rode `python --version` e `git --version` (no macOS/Linux pode ser `python3`). Crie um arquivo `ola.py` e rode-o **fora do Colab**.
  **Evidência:** nota `notes/ambiente-local.md` com o seu sistema, as versões e o que deu errado no caminho.
- [ ] **M1.6b · Git pelo terminal** — 20 XP
  **Antes do primeiro commit**, configure o e-mail privado do GitHub: `git config --global user.email "<id>+<usuario>@users.noreply.github.com"` (o endereço está em *GitHub → Settings → Emails*; veja o [SECURITY](../../SECURITY.pt-BR.md)). Clone este repositório (`git clone`), edite o `LOG.md` localmente e publique com `git add`, `git commit` e `git push`. No Windows, o login pode abrir uma janela do navegador; no macOS/Linux, use o [GitHub CLI](https://cli.github.com/) (`gh auth login`) ou um token.
  **Evidência:** um commit seu feito pelo terminal, com e-mail `noreply`.
- [ ] **M1.6c · Ambiente virtual** — 15 XP
  Na pasta do repositório, crie e ative um ambiente virtual: `python -m venv .venv` e depois `.venv\Scripts\activate` (Windows) ou `source .venv/bin/activate` (macOS/Linux). Instale um pacote (`pip install requests`) e rode um script que o use. A pasta `.venv/` já está no `.gitignore`: confira que ela **não** entra no commit.
  **Evidência:** a seção *Ambiente virtual* na `notes/ambiente-local.md`, com os comandos que funcionaram no seu sistema.
- [ ] **M1.6d · Segundo cérebro** — 30 XP
  Instale o [Obsidian](https://obsidian.md/) e abra a pasta do repositório clonado como vault (*Open folder as vault*). A configuração básica já vem no repositório (links Markdown, pasta de templates). Em *Settings → Community plugins*, instale e ative **Obsidian Git** (sincroniza com o GitHub) e **Spaced Repetition** (flashcards). Leia o [`brain/README.md`](../../brain/README.md) e crie suas **2 primeiras notas de conceito** em `brain/concepts/` com o [template de conceito](../../templates/conceito.md), linkadas a partir de uma nota de missão.
  **Evidência:** as 2 notas em `brain/concepts/` e um commit feito pelo Obsidian Git.
- [ ] **M1.7 · Testes** — 40 XP · 🏅 *Testado*
  CS50P **Lecture 5** + Problem Set 5 (`pytest`).
- [ ] **M1.8 · Arquivos** — 40 XP
  CS50P **Lecture 6** + Problem Set 6 (ler/escrever CSV).
- [ ] **M1.8b · O feitiço no seu arquivo** — 30 XP
  Volte ao modelo da [M0.7](../00-tutorial/), agora **localmente**, no seu ambiente virtual (`pip install transformers torch`). Escreva um script que lê um arquivo **seu** (mensagens exportadas, avaliações, anotações, ~50 linhas; tire nomes e dados pessoais antes), classifica o sentimento de cada linha e grava um CSV com o resultado e a contagem por sentimento.
  **Evidência:** o script em `exercises/`, o CSV de saída **sem dados pessoais** e 3 linhas sobre onde o modelo errou no seu tipo de texto.
- [ ] **M1.9 · Expressões regulares** — 20 XP
  CS50P **Lecture 7** + pelo menos 2 exercícios do Problem Set 7.
- [ ] **M1.10 · Orientação a objetos** — 50 XP
  CS50P **Lecture 8** + Problem Set 8.
- [ ] **M1.11 · Et cetera** — 10 XP
  CS50P **Lecture 9** (sem problem set). Nota com os 3 recursos que mais te surpreenderam.

**Total de missões:** 470 XP

---

## ⚔️ Mini-chefão de elite — O Sentinela · 50 XP

Depois da M1.5, **sem tutorial e sem olhar soluções**: um programa de terminal do zero, em até 3 sessões, que resolve um problema pequeno seu (ex.: calculadora de gastos do mês, sorteio de tarefas, quiz de revisão). Pode consultar a documentação do Python; não pode copiar código pronto nem pedir para uma IA escrever.

- [ ] Código em `exercises/sentinela/`, rodando, com tratamento de entrada inválida.
- [ ] Na nota da missão: o que travou e como você destravou.

---

## 🐉 Chefão — O Construtor de Ferramentas · 150 XP

Faça o **Final Project do CS50P** como um **repositório próprio** no seu GitHub, seguindo o [padrão de chefão](../../ROADMAP.md#padrao-de-chefao):

- [ ] Uma ferramenta de linha de comando que resolve um problema **seu** (ex.: organizar gastos a partir de um CSV, gerar planos de estudo, conversor de unidades, jogo no terminal).
- [ ] Pelo menos 3 funções testadas com `pytest`.
- [ ] `README.md` a partir do [template de chefão](../../templates/chefao-readme.md): problema, como instalar, como usar, e a **demo** (GIF do terminal ou exemplo de saída).
- [ ] Um post curto contando o que a ferramenta faz e o que você aprendeu.
- [ ] Link do repositório adicionado à seção *Projetos em destaque* do [README principal](../../README.md).
- [ ] (Opcional) Submeter ao CS50P e ganhar o certificado.

Vencer o chefão = **Nível 2 · Pythonista** 🐍 e desbloqueia a [Fase 2 — Dados & Matemática](../02-data-math/).
