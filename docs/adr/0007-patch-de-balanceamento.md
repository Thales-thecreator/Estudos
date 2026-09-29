# Patch de balanceamento depois do red team

Um comitê simulado de red team (Tech Lead de IA, Game Designer, Mentor de Carreira, PM de EdTech e QA educacional) e uma segunda análise externa apontaram: primeiro "uau" tarde demais, XP que mede tempo e não domínio (risco de "scripter de IA"), chefões com cara de brinquedo (Titanic, House Prices), matemática concentrada na F2, falta de ferramentas de engenheiro antes do MLOps, nenhuma saída de carreira antes da F8 e nenhuma regra para pausas planejadas. Decidimos:

- **Poder cedo:** M0.7 (modelo pré-treinado de sentimento em PT no Colab) e M1.8b (o mesmo modelo no arquivo do jogador). O XP da F0 e da F1 foi redistribuído; os totais de fase não mudaram.
- **Domínio acima de tempo:** prova oral de 2 perguntas antes de aceitar cada missão (adia, nunca tira XP) e um mini-chefão de elite por fase, sem tutorial e sem IA escrevendo o código.
- **Chefões de portfólio:** um padrão comum (template de README, métricas reais, demo pública, post, dados reais e recentes). F3 com baseline, análise de erros e relatório de 1 página; F4 num problema útil; F6 com evals, custo/latência, agente com ferramentas e defesas contra prompt injection. LoRA virou side quest.
- **Currículo:** matemática na hora certa (cálculo sai da F2 para a F4; matrizes e softmax entram na F6) com teto de 2 sessões por tópico; a Ponte de 2 semanas no começo da F3 (terminal, HTTP/APIs, JSON, projeto em módulos, SQLite), que leva a F3 a 12 semanas e o jogo a ~76; DVC obrigatório e cloud explícita (AWS ou GCP, free tier) na F5; segurança e observabilidade de LLM na F6.
- **Carreira:** postos avançados — networking mensal a partir da F1 e vagas adjacentes/freelas a partir da F3, com XP próprio.
- **Custos:** tavernas gratuitas (Colab, Kaggle, HF Spaces) como caminho padrão; nuvem só no free tier com alerta na F5; até R$ 50/mês em APIs na F6, com alerta.
- **Constância sem punição:** Santuário (até 4 semanas por ano que congelam o streak) e ritual de retorno depois de 3+ semanas fora.
- **Speedrun:** desafiar o chefão direto dá todo o XP da fase (não vale na F0).
- **A reescrita de `sync.py`/`qa.py`** saiu do chefão da F5 (troca de contexto no meio do MLOps) e virou a side quest *A Forja Própria*.
- **README em inglês** abre com uma linha de resultados de engenharia e os projetos em destaque; o RPG vem depois.

**Considerado e rejeitado:** perda de streak/XP como *debuff* (contraria a regra de nunca punir, feita para quem não tem hábito); sessão mínima de 1 hora (vira dica de "sessão profunda" a partir da F2, porque o risco maior é abandono); mover pandas/SQL para a F1 (a F1 já é densa; a F2 ficou leve tirando o cálculo); "primeiro feitiço" com API paga da OpenAI (exige chave e cartão no dia 1; o modelo local é grátis e sem segredo para vazar); vídeos no Loom defendendo o código (a prova oral cobre o mesmo risco sem expor rosto e voz num repositório público); limitar XP de sessão mínima (ela já não dá XP, só conta para a meta, e no máximo 1 por semana).
