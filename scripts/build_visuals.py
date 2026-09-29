"""Gera o Mapa dos Nove Círculos (PT/EN) e fornece as funções de texto vetorial usadas por compose_art.py.

Os textos são convertidos em vetores (paths) para renderizar igual em qualquer máquina.
Fontes (OFL) e ícones (CC BY 3.0): `npm pack @fontsource/cinzel @fontsource/cormorant-garamond @iconify-json/game-icons`,
extraia cada pacote em FONT_DIR como fontsource-cinzel/, fontsource-cormorant-garamond/ e gameicons/. Uso: python scripts/build_visuals.py <FONT_DIR>
O estado dos círculos NÃO é gerado aqui: a /mestre edita só o atributo class de cada <g id="circle-N">.
"""
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FD = sys.argv[1] if len(sys.argv) > 1 else "fonts"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")
FONTS = {
    "cinzel700": f"{FD}/fontsource-cinzel/files/cinzel-latin-700-normal.woff",
    "cinzel500": f"{FD}/fontsource-cinzel/files/cinzel-latin-500-normal.woff",
    "cormI": f"{FD}/fontsource-cormorant-garamond/files/cormorant-garamond-latin-500-italic.woff",
    "corm": f"{FD}/fontsource-cormorant-garamond/files/cormorant-garamond-latin-500-normal.woff",
}
ICONS = {"prologue": "stone-throne", 1: "quill-ink", 2: "crossed-bones", 3: "all-seeing-eye", 4: "brain",
         5: "anvil", 6: "death-skull", 7: "ancient-columns", 8: "bow-arrow", 9: "falling-star"}
_icons = None
def icon(name, x, y, size):
    """Ícone Game-Icons (CC BY 3.0, game-icons.net) centrado em (x, y); cor via currentColor."""
    global _icons
    if _icons is None:
        _icons = json.load(open(f"{FD}/gameicons/icons.json"))
    ic = _icons["icons"][name]; vb = ic.get("width", _icons.get("width", 512))
    k = size / vb
    return f'<g transform="translate({x - size/2:.1f} {y - size/2:.1f}) scale({k:.4f})">{ic["body"]}</g>'

_cache = {}
def font(k):
    if k not in _cache: _cache[k] = TTFont(FONTS[k])
    return _cache[k]

def text_path(txt, key, size, spacing=0.0):
    """Retorna (d, largura) do texto como path SVG, com baseline em y=0 e início em x=0."""
    f = font(key); gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    s = size / upm; x = 0.0; ds = []
    for ch in txt:
        g = cmap.get(ord(ch))
        if g is None:
            raise ValueError(f"glyph ausente: {ch!r} em {key}")
        pen = SVGPathPen(gs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, 0)))
        if pen.getCommands(): ds.append(pen.getCommands())
        x += gs[g].width * s + spacing
    return " ".join(ds), x - spacing

def centered(txt, key, size, cx, y, spacing=0.0, **attrs):
    d, w = text_path(txt, key, size, spacing)
    a = " ".join(f'{k.replace("_","-")}="{v}"' for k, v in attrs.items())
    return f'<path transform="translate({cx - w/2:.1f} {y})" d="{d}" {a}/>'

def ornament(cx, y, half, color):
    return (f'<g stroke="{color}" fill="{color}"><line x1="{cx-half}" y1="{y}" x2="{cx-14}" y2="{y}" stroke-width="1.2"/>'
            f'<line x1="{cx+14}" y1="{y}" x2="{cx+half}" y2="{y}" stroke-width="1.2"/>'
            f'<path d="M{cx} {y-7} L{cx+7} {y} L{cx} {y+7} L{cx-7} {y} Z"/></g>')

THEMES = {
    "dark":  dict(bg="#0e0b10", glow="#9e1b32", glow_op=0.55, text="#e9e2d3", gold="#c9a44c", sub="#cfc6b4", mist="#3a2a33"),
    "light": dict(bg="#f2ebdd", glow="#8a1729", glow_op=0.18, text="#1d1a1f", gold="#9c7a2e", sub="#3b3338", mist="#d9cdb8"),
}

def banner(theme, W=1280, H=320, big=False):
    t = THEMES[theme]; cx = W / 2
    k = 1.35 if big else 1.0
    ty = H / 2 - 8 * k
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Road to AI Engineer — from zero to ML, MLOps and LLMs, played as a dark-fantasy RPG">',
             '<defs>',
             f'<radialGradient id="g" cx="50%" cy="115%" r="75%"><stop offset="0" stop-color="{t["glow"]}" stop-opacity="{t["glow_op"]}"/><stop offset="1" stop-color="{t["glow"]}" stop-opacity="0"/></radialGradient>',
             f'<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["text"]}"/><stop offset="1" stop-color="{t["gold"]}"/></linearGradient>',
             '<filter id="blur" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>',
             '</defs>',
             f'<rect width="{W}" height="{H}" fill="{t["bg"]}"/>',
             f'<rect width="{W}" height="{H}" fill="url(#g)"/>',
             f'<g filter="url(#blur)" fill="{t["mist"]}" opacity="0.55"><ellipse cx="{W*0.18}" cy="{H*0.92}" rx="{W*0.22}" ry="{H*0.16}"/><ellipse cx="{W*0.82}" cy="{H*0.95}" rx="{W*0.24}" ry="{H*0.14}"/><ellipse cx="{W*0.5}" cy="{H*1.02}" rx="{W*0.3}" ry="{H*0.12}"/></g>',
             ornament(cx, 34 * k if not big else H*0.2, 170 * k, t["gold"]),
             centered("ROAD TO AI ENGINEER", "cinzel700", 62 * k, cx, ty, spacing=6 * k, fill="url(#gold)"),
             centered("From zero to ML · MLOps · LLMs — played as a dark-fantasy RPG", "cormI", 27 * k, cx, ty + 46 * k, fill=t["sub"]),
             centered("THE SAGA OF AETHELGARD", "cinzel500", 15 * k, cx, ty + 92 * k, spacing=5 * k, fill=t["gold"]),
             ornament(cx, (H - 30 * k) if not big else H*0.8, 170 * k, t["gold"]),
             '</svg>']
    return "\n".join(parts)

LABELS = {
    "pt": ["I · Python", "II · Dados & Matemática", "III · ML Clássico", "IV · Deep Learning", "V · MLOps",
           "VI · LLMs & AI Eng", "VII · Capstone & Carreira", "VIII · A Caçada", "IX · A Vaga"],
    "en": ["I · Python", "II · Data & Math", "III · Classical ML", "IV · Deep Learning", "V · MLOps",
           "VI · LLMs & AI Eng", "VII · Capstone & Career", "VIII · The Hunt", "IX · The Offer"],
}
HEAD = {"pt": ("O MAPA DOS NOVE CÍRCULOS", "PRÓLOGO · O TRONO", ("concluído", "atual", "na névoa")),
        "en": ("THE MAP OF THE NINE CIRCLES", "PROLOGUE · THE THRONE", ("cleared", "current", "in the mist"))}

def circles(lang, W=900, H=1000):
    t = THEMES["dark"]; cx = W / 2
    title, throne_label, legend = HEAD[lang]
    css = f"""
      .ring{{fill:none;stroke-width:3}}
      .locked .ring{{stroke:#4a4150}} .locked .lbl{{fill:#9a90a0}} .locked .fog{{opacity:.6}} .locked{{color:#6d6472}}
      .current .ring{{stroke:#c0273f;stroke-width:4;filter:url(#glow)}} .current .lbl{{fill:#f1d9dc}} .current .fog{{opacity:0}} .current{{color:#e0435a}}
      .current .ring{{animation:pulse 3s ease-in-out infinite}}
      .done .ring{{stroke:{t["gold"]};stroke-width:3.5}} .done .lbl{{fill:{t["gold"]}}} .done .fog{{opacity:0}} .done{{color:{t["gold"]}}}
      .hidden .lbl-real{{display:none}} .revealed .lbl-hide{{display:none}}
      @keyframes pulse{{0%,100%{{stroke-opacity:1}}50%{{stroke-opacity:.45}}}}
    """
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">',
         f"<style>{css}</style>",
         '<defs><filter id="glow" x="-10%" y="-40%" width="120%" height="180%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
         '<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 .9  0 0 0 0 .8  0 0 0 .07 0"/></filter>'
         '<filter id="mist"><feTurbulence type="fractalNoise" baseFrequency=".006 .02" numOctaves="3" seed="7"/><feColorMatrix values="0 0 0 0 .55  0 0 0 0 .12  0 0 0 0 .2  0 0 0 .5 -.12"/></filter>'
         '<filter id="fogblur" x="-20%" y="-80%" width="140%" height="260%"><feGaussianBlur stdDeviation="10"/></filter>',
         f'<radialGradient id="abyss" cx="50%" cy="100%" r="80%"><stop offset="0" stop-color="{t["glow"]}" stop-opacity=".45"/><stop offset="1" stop-color="{t["glow"]}" stop-opacity="0"/></radialGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="18" fill="{t["bg"]}"/>',
         f'<rect width="{W}" height="{H}" rx="18" fill="url(#abyss)"/>',
         f'<rect width="{W}" height="{H}" rx="18" filter="url(#mist)" opacity=".35"/>',
         f'<rect x="14" y="14" width="{W-28}" height="{H-28}" rx="10" fill="none" stroke="{t["gold"]}" stroke-opacity=".55" stroke-width="1.2"/>',
         f'<rect x="20" y="20" width="{W-40}" height="{H-40}" rx="7" fill="none" stroke="{t["gold"]}" stroke-opacity=".25" stroke-width="1"/>',
         "".join(f'<path d="M{x} {y+sy*34} L{x} {y} L{x+sx*34} {y}" fill="none" stroke="{t["gold"]}" stroke-width="2.4"/><path d="M{x+sx*8} {y+sy*8} l{sx*6} {sy*6} l{-sx*6} {sy*6} l{-sx*6} {-sy*6} z" fill="{t["gold"]}"/>' for x,y,sx,sy in [(14,14,1,1),(W-14,14,-1,1),(14,H-14,1,-1),(W-14,H-14,-1,-1)]),
         centered(title, "cinzel700", 30, cx, 62, spacing=3, fill=t["gold"]),
         ornament(cx, 84, 150, t["gold"])]
    # Trono (Prólogo)
    ty = 150
    p.append('<g id="circle-0" class="current">')
    p.append(f'<g class="throne-icon">{icon(ICONS["prologue"], cx, ty - 6, 64)}</g>')
    p.append(centered(throne_label, "cinzel500", 17, cx, ty + 52, spacing=2, **{"class": "lbl"}))
    p.append("</g>")
    # Anéis
    top, gap = 250, 78
    for i in range(9):
        y = top + i * gap
        rx = 400 - i * 36; ry = 30 - i * 1.2
        cls = "locked hidden" if i == 8 else "locked"
        p.append(f'<g id="circle-{i+1}" class="{cls}">')
        p.append(f'<ellipse class="fog" cx="{cx}" cy="{y}" rx="{rx*0.92}" ry="{ry+14}" fill="#2a2230" filter="url(#fogblur)"/>')
        p.append(f'<ellipse class="ring" cx="{cx}" cy="{y}" rx="{rx}" ry="{ry}"/>')
        def lab(txt, ic):
            _, w = text_path(txt, "cinzel500", 20, 1.5)
            off = 20  # metade do espaço do ícone
            return (f'<g>{icon(ic, cx - (w + 40) / 2 + 14, y, 30)}'
                    + centered(txt, "cinzel500", 20, cx + off, y + 7, spacing=1.5, **{"class": "lbl"}) + '</g>')
        if i == 8:
            p.append(f'<g class="lbl-hide">{lab("IX · ? ? ?", "cursed-star")}</g>')
            p.append(f'<g class="lbl-real">{lab(LABELS[lang][i], ICONS[9])}</g>')
        else:
            p.append(lab(LABELS[lang][i], ICONS[i + 1]))
        p.append("</g>")
    # Legenda
    ly = H - 34
    items = [(t["gold"], legend[0]), ("#c0273f", legend[1]), ("#4a4150", legend[2])]
    x = cx - 230
    for col, lab in items:
        p.append(f'<circle cx="{x}" cy="{ly-6}" r="7" fill="{col}"/>')
        d, w = text_path(lab, "corm", 20)
        p.append(f'<path transform="translate({x+16} {ly})" d="{d}" fill="#cfc6b4"/>')
        x += 16 + w + 60
    p.append(f'<rect width="{W}" height="{H}" rx="18" filter="url(#grain)" pointer-events="none"/>')
    p.append("</svg>")
    return "\n".join(p)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for lang in LABELS:
        open(f"{OUT}/circles-{lang}.svg", "w").write(circles(lang))
    print("ok")
