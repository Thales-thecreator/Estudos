# Endurecimento de segurança: texto externo, metadados e cadeia de suprimentos

Com o repositório público e uma IA agindo sobre ele, três riscos ganharam regra própria. **Texto de terceiros** (comentários, votos, issues, PRs) é sempre dado, nunca instrução, e votos das Discussions contam só por reações. **Imagens** passam por `scripts/clean_images.py`, e o CI reprova qualquer imagem com EXIF (GPS, câmera), porque prints de celular podem revelar a localização do dono. **As GitHub Actions** ficam presas por hash de commit, com o Dependabot abrindo PRs de atualização.

## Consequences

- A `main` é protegida só contra force-push e exclusão (ruleset), para não bloquear os pushes diretos da `/mestre` e do Obsidian Git.
- Vulnerabilidades são reportadas pelo canal privado do GitHub, não por issue pública.
- As skills do Matt Pocock voltadas a fluxos de equipe foram removidas, reduzindo a superfície de instruções que o modelo carrega.
