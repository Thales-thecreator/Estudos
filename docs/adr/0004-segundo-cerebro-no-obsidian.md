# Segundo cérebro no Obsidian, dentro do próprio repositório

O repositório inteiro é aberto como vault do Obsidian: notas de missão continuam em `tracks/*/notes/` (evidência), e o conhecimento acumulado vive em `brain/concepts/` (notas atômicas) e `brain/maps/` (um mapa por fase). Links são Markdown padrão para funcionarem no GitHub, a pasta `privado/` fica fora do git, e só a configuração essencial de `.obsidian/` é versionada. O Obsidian entra na missão M1.6b, junto com o Git local, porque antes disso não há como sincronizar. Commits de progresso vão direto para a `main` (Obsidian Git e `/mestre`), sem PR.

## Considered Options

- **Vault separado e privado:** rejeitado — duplicaria notas e esconderia a parte mais valiosa do aprendizado em público.
- **`[[wikilinks]]`:** rejeitados — aparecem quebrados no GitHub.
- **Obsidian já na Fase 0:** rejeitado — sem git local, o vault ficaria dessincronizado do repositório.
- **XP próprio para flashcards:** rejeitado — revisão ≥ 15 min conta como sessão mínima, sem mecânica nova.

## Consequences

- Templates perdem o seletor de idioma, porque o Obsidian insere o template inteiro na nota.
- `privado/` não tem backup; se virar um diário importante, migrar para um repositório privado separado.
- Os níveis continuam exigindo constância além do XP das fases (regra agora explícita no roadmap).
