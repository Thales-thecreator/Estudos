# Visuais

## Mapa dos Nove Círculos

`assets/circles-pt.svg` e `circles-en.svg` são atualizados pelo `scripts/sync.py` a partir de `phase` e `finished` no `progress.yml` (círculo 0 = Trono/Prólogo; o 9 só se revela ao virar atual). **Nunca edite os SVGs à mão.** Para mudar desenho ou rótulos, edite `scripts/build_visuals.py`, regenere (precisa das fontes e ícones descritos no script) e **rode o `sync.py` logo depois**, porque a regeneração volta todos os círculos ao estado inicial.

## Ilustração de cada capítulo

1. Depois de narrar um capítulo, escreva um **prompt de imagem** em inglês com a cena central, **sem spoilers do futuro** e sem nomes de artistas vivos, terminando com: *"Dark fantasy oil painting, cold obsidian, crimson and old gold palette, dramatic chiaroscuro, painterly texture, Castlevania and Dark Souls concept art mood. 16:9. No text, no letters."*
2. Peça ao jogador que gere a imagem (Gemini, ChatGPT...) e suba em `assets/incoming/` (*Add file → Upload files*).
3. Quando chegar: converta para JPG (qualidade ~88, largura máx. 1672) em `assets/art/NN-slug.jpg`, apague o original de `incoming/`, ponha a imagem no topo do capítulo (PT e EN, com `alt` descritivo) e, se for o capítulo mais recente, troque a ilustração e o trecho da seção **A Saga** nos dois READMEs.

## Banner, faixas e social preview

Gerados por `scripts/compose_art.py` a partir de `assets/art/landscape.jpg` (pintura) + títulos vetoriais. Só regenere se o dono pedir.
