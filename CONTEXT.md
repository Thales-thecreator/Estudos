# Estudos — Jogo de Aprendizado

Repositório de estudos para sair do zero até a primeira vaga como ML / MLOps / AI Engineer, organizado como um jogo. Este glossário fixa o vocabulário do jogo; os termos técnicos de ML ficam no `classroom/GLOSSARY.md`.

## Estrutura do jogo

**Fase**:
Um bloco do roadmap (0 a 8) com tema, duração estimada em semanas, missões e um chefão. Cada fase vive em `tracks/NN-nome/`.
_Avoid_: Módulo, etapa, trilha

**Missão**:
Uma unidade de estudo concluível em 1 a 4 sessões, com XP definido e evidência exigida no repo.
_Avoid_: Tarefa, lição, atividade

**Chefão**:
O projeto prático obrigatório no fim de uma fase; vencê-lo desbloqueia a fase seguinte.
_Avoid_: Projeto final, desafio, boss

**Mini-chefão de elite**:
Problema pequeno no meio de uma fase (a partir da F1), resolvido sem tutorial e sem IA escrevendo o código, em até 3 sessões; ~50 XP pagos do XP da fase.
_Avoid_: Checkpoint, prova

**Padrão de chefão**:
O que todo chefão precisa além dos itens da fase: repositório próprio com o template de README, métricas reais, demo pública, post, e dados reais (nada de dataset de tutorial).

**Desafiar o chefão**:
Enfrentar o chefão de uma fase sem fazer as missões (speedrun); vencer dá todo o XP da fase. Não vale na F0.
_Avoid_: Pular fase

**Prova oral**:
As 2 perguntas curtas que o Mestre faz sobre a evidência antes de aceitar uma missão. Não tira XP: só adia até a resposta.
_Avoid_: Quiz, teste

**A Ponte**:
As 2 primeiras semanas da Fase 3: terminal, HTTP e APIs, JSON, projeto Python em módulos e banco de dados a partir do código.

**Side quest**:
Missão opcional fora do caminho principal, desbloqueada a partir da Fase 3.
_Avoid_: Extra, bônus

**Posto avançado**:
Missão de carreira em paralelo às fases: networking (+15 XP, 1 por mês, a partir da F1) ou carreira (vagas adjacentes, freelas, open source; 50–150 XP, a partir da F3).
_Avoid_: Side quest

**Taverna**:
Ambiente gratuito de computação (Colab, Kaggle Notebooks, Hugging Face Spaces) usado no lugar de GPU própria.

**Evidência**:
Um artefato no repo (nota, código, notebook, link no `LOG.md`) que prova que uma missão foi concluída. Sem evidência, sem XP.

## Progresso

**Sessão**:
Um período de estudo focado registrado como uma linha no `LOG.md`. Padrão: ≥ 30 min. Mínima: 15 min, no máximo uma por semana.
_Avoid_: Estudo, aula

**Meta semanal**:
O número de sessões a cumprir de segunda a domingo: 3 no primeiro mês, 4 depois.

**Semana de aquecimento**:
Os dias entre o `/mestre começar` e o primeiro domingo; sessões valem XP de missão, mas não entram na meta semanal nem no streak.

**Streak**:
Número de semanas seguidas em que a meta semanal foi batida. Quebrar o streak só zera a contagem; nunca remove XP.
_Avoid_: Sequência diária, ofensiva

**Santuário**:
Semana de pausa planejada, anunciada no `LOG.md` antes de começar (máx. 4 por ano); não conta para a meta e congela o streak.
_Avoid_: Férias, folga

**Ritual de retorno**:
Semana com meta reduzida (2 sessões) e uma missão de revisão, aberta pelo Mestre depois de mais de 3 semanas sem sessão.

**Estado do jogo**:
O arquivo `progress.yml`, fonte única de verdade do progresso; badges, painéis, ficha e mapa são gerados a partir dele por `scripts/sync.py`.
_Avoid_: Placar, save

**XP**:
Pontos ganhos por missões, chefões, side quests, aulas e metas semanais. Nunca diminuem.

**Nível**:
Título do jogador (0 · Recruta a 9 · Lenda). Sobe quando o XP mínimo **e** o chefão da fase correspondente foram alcançados.

**Conquista**:
Marco único desbloqueado uma vez (ex.: Primeiro Commit), registrado com data no `ROADMAP.md`.
_Avoid_: Badge, troféu

## Saga

**Mestre**:
O narrador da saga, invocado pela skill `/mestre`; confere evidências e narra as consequências.
_Avoid_: DM, narrador

**Círculo**:
Uma fase vista na saga: F1–F8 são os Círculos 1–8; a vaga assinada é o Círculo 9. A F0 é o Prólogo.

**Corrente**:
Cada uma das missões M0.1–M0.6 da Fase 0, na saga; quebrar as seis e vencer o Trono encerra o Prólogo. A M0.7 é a **Faísca**, não uma corrente.

**Suserano**:
O chefão de uma fase, na saga.
_Avoid_: Vilão, boss

**Cena**:
Narração curta de uma missão cumprida, salva em `saga/cenas/`.

**Capítulo**:
Narração longa de um chefão vencido, com revelação e dilema, salva em `saga/capitulos/`.

**Eco**:
Narração de 2–3 frases quando a meta semanal é batida.

**Item lendário**:
Uma conquista, na saga; fica no inventário da ficha.

**Bíblia**:
Os pilares secretos da trama em `.claude/dm/biblia.md.b64`; só o Mestre lê.

## Segundo cérebro

**Nota de conceito**:
Nota atômica em `brain/concepts/` sobre um único conceito, escrita pelo dono com as próprias palavras; criada quando o conceito aparece pela segunda vez.
_Avoid_: Resumo, fichamento

**Mapa**:
Índice em `brain/maps/` que liga as notas de conceito de uma fase.
_Avoid_: MOC, índice

**Flashcard**:
Linha `Pergunta::Resposta` numa nota com a tag `#flashcards`, revisada pelo plugin Spaced Repetition.

## Estudo

**Aula**:
Lição curta e interativa gerada pela skill `/teach`, salva em `classroom/lessons/`. Vale +10 XP com o quiz feito.
_Avoid_: Lesson

**Nota** (de missão):
Anotação sua sobre um tema, em português, em `tracks/NN-nome/notes/`, seguindo `templates/nota-de-estudo.md`.
