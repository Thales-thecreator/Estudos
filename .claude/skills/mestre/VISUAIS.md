# Visuais

## Mapa dos Nove Círculos

`assets/circles-pt.svg` e `circles-en.svg` são atualizados pelo `scripts/sync.py` a partir de `phase` e `finished` no `progress.yml` (círculo 0 = Trono/Prólogo; o 9 só se revela ao virar atual). **Nunca edite os SVGs à mão.** Para mudar desenho ou rótulos, edite `scripts/build_visuals.py`, regenere (precisa das fontes e ícones descritos no script) e **rode o `sync.py` logo depois**, porque a regeneração volta todos os círculos ao estado inicial.

## Ilustração de cada capítulo

1. Depois de narrar um capítulo, escreva um **prompt de imagem** em inglês com a cena central, **sem spoilers do futuro** e sem nomes de artistas vivos, terminando com: *"Dark fantasy oil painting, cold obsidian, crimson and old gold palette, dramatic chiaroscuro, painterly texture, Castlevania and Dark Souls concept art mood. 16:9. No text, no letters."*
2. Peça ao jogador que gere a imagem (Gemini, ChatGPT...) e suba em `assets/incoming/` (*Add file → Upload files*).
3. Quando chegar: converta para JPG (qualidade ~88, largura máx. 1672) em `assets/art/NN-slug.jpg`, apague o original de `incoming/`, ponha a imagem no topo do capítulo (PT e EN, com `alt` descritivo) e, se for o capítulo mais recente, troque a ilustração e o trecho da seção **A Saga** nos dois READMEs.

## Vinheta de cada cena (opcional para o jogador)

Toda cena nova termina com um bloco recolhível `🎨 Prompt da ilustração` (EN: `🎨 Illustration prompt`), com o **mesmo prompt em inglês** nos dois arquivos e a instrução de anexar `assets/art/00-prologo.jpg` como referência (copie o formato das cenas 0001–0005). O prompt tem três partes, nesta ordem:

1. **A cena:** um detalhe central e concreto do que foi narrado (a mão, o objeto, a corrente que cai), só com o que a cena revelou. Sem spoilers, sem nomes de artistas vivos.
2. **O cânone visual**, sempre igual:
   > Thales the Heretic: gaunt, scarred man in his thirties, dark matted shoulder-length hair, stubble, bare scarred torso, tattered dark cloth, worn leather boots, bound by crimson-glowing iron chains; on his right hand a cracked, blackened-bronze gauntlet with faint copper light in the cracks. The creature: tall, slender feminine figure sculpted from obsidian and ice, crown of jagged black shards, pale glowing eyes, flowing robe of cracked translucent ice. The Throne of Broken Blades: a throne built from hundreds of shattered swords, inside ruined gothic cathedrals bleeding crimson mist under a starless sky.
3. **O estilo**, sempre igual:
   > *Dark fantasy oil painting, cold obsidian, crimson and old gold palette, dramatic chiaroscuro, painterly texture, Castlevania and Dark Souls concept art mood. Close, intimate framing on a single detail. 3:2. No text, no letters.*

Se algo do cânone mudar na história (a Manopla restaurada, o Trono deixado para trás), atualize o cânone aqui **antes** do próximo prompt.

A imagem é **opcional**: a cena está completa sem ela. Quando o jogador subir uma em `assets/incoming/`, converta para JPG (qualidade ~88, largura máx. 1200) em `assets/art/cenas/NNNN-slug.jpg`, apague o original de `incoming/`, rode `python scripts/clean_images.py` e ponha no topo da cena, logo abaixo do seletor de idioma (PT e EN): `<p align="center"><img src="../../assets/art/cenas/NNNN-slug.jpg" alt="<descrição>" width="480"></p>`.

## Banner, faixas e social preview

Gerados por `scripts/compose_art.py` a partir de `assets/art/landscape.jpg` (pintura) + títulos vetoriais. Só regenere se o dono pedir.
