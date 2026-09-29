# Saga narrativa como camada sobre o roadmap, com bíblia selada

O dono quis jogar o roadmap como um RPG grimdark com um Mestre que só revela a história conforme o estudo avança. Como o Claude não tem memória entre sessões nem um "banco de dados" secreto, a saga vive no repositório: a crônica pública (`saga/cronica.md`) é a memória de continuidade, e os pilares da trama (verdade central, traições, finais, itens) ficam numa bíblia codificada em base64 em `.claude/dm/`, lida só pela skill `/mestre`. A saga **veste** o roadmap sem mudar a mecânica: só missões do roadmap dão XP, missões e chefões exigem evidência, e a ausência faz "a Névoa avançar" na história, mas nunca tira XP.

## Considered Options

- **História 100% improvisada:** rejeitada — traições e final ficariam desamarrados.
- **Bíblia em texto puro:** rejeitada — spoiler acidental ao navegar no repo. Base64 não é segurança, só evita a leitura sem querer; o resto é honra.
- **Instruções no CLAUDE.md em vez de skill:** rejeitada — o Mestre entraria em personagem até em dúvidas de Python.
- **Metas livres (qualquer estudo vale):** rejeitada — dispersa um iniciante; estudos fora do roadmap viram só lore, sem XP.

## Consequences

- Os 9 círculos da saga pediram uma **Fase 8 — A Caçada** (candidaturas até a primeira proposta) e o **Nível 9**; o Círculo 9 é a vaga assinada.
- O repositório é público: qualquer pessoa pode decodificar a bíblia. Aceito.
