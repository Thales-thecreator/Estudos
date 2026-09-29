"""Compõe o banner e o social preview: pintura de fundo + título vetorial (Cinzel/Cormorant).

Uso: python scripts/compose_art.py <FONT_DIR> <banner-bg.jpg> <social-bg.jpg> <saída>
Requer: fonttools, pillow, playwright (Chromium). Gera banner.jpg (2560x800), social-preview.jpg (1280x640)
e as faixas de seção strip-*.jpg (2560x400) a partir de assets/art/landscape.jpg.
"""
import sys, os, base64, asyncio, pathlib
sys.argv, args = sys.argv[:2], sys.argv[2:]
import build_visuals as bv
from PIL import Image
from playwright.async_api import async_playwright

def svg(bg_file, W, H, k, title_y):
    b64 = base64.b64encode(open(bg_file, "rb").read()).decode()
    gold, bone = "#c9a44c", "#e9e2d3"; cx = W / 2
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<defs><radialGradient id="v" cx="50%" cy="42%" r="70%"><stop offset=".35" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".55"/></radialGradient>',
        f'<radialGradient id="halo" cx="50%" cy="{title_y/H*100:.0f}%" r="38%"><stop offset="0" stop-color="#050306" stop-opacity=".7"/><stop offset="1" stop-color="#050306" stop-opacity="0"/></radialGradient>',
        f'<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3ead6"/><stop offset=".55" stop-color="{bone}"/><stop offset="1" stop-color="{gold}"/></linearGradient>',
        '<filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity=".9"/></filter></defs>',
        f'<image href="data:image/jpeg;base64,{b64}" width="{W}" height="{H}" preserveAspectRatio="xMidYMid slice"/>',
        f'<rect width="{W}" height="{H}" fill="url(#v)"/>',
        f'<rect width="{W}" height="{H}" fill="url(#halo)"/>',
        '<g filter="url(#shadow)">',
        bv.ornament(cx, title_y - 82 * k, 170 * k, gold),
        bv.centered("ROAD TO AI ENGINEER", "cinzel700", 62 * k, cx, title_y, spacing=6 * k, fill="url(#gold)"),
        bv.centered("From zero to ML · MLOps · LLMs — played as a dark-fantasy RPG", "cormI", 27 * k, cx, title_y + 44 * k, fill=bone),
        bv.centered("THE SAGA OF AETHELGARD", "cinzel500", 15 * k, cx, title_y + 86 * k, spacing=5 * k, fill=gold),
        '</g></svg>'])

def strip(bg_file, title, sub, W=1280, H=200, y_off=0.35):
    """Faixa fina de seção: pintura + título em Cinzel + subtítulo."""
    b64 = base64.b64encode(open(bg_file, "rb").read()).decode()
    gold, bone = "#c9a44c", "#e9e2d3"; cx = W / 2
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<defs><linearGradient id="d" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity=".65"/></linearGradient>',
        f'<radialGradient id="halo" cx="50%" cy="50%" r="45%"><stop offset="0" stop-color="#050306" stop-opacity=".75"/><stop offset="1" stop-color="#050306" stop-opacity="0"/></radialGradient>',
        f'<linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3ead6"/><stop offset="1" stop-color="{gold}"/></linearGradient>',
        '<filter id="shadow"><feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000" flood-opacity=".9"/></filter></defs>',
        f'<image href="data:image/jpeg;base64,{b64}" x="0" y="{-H * y_off * 2:.0f}" width="{W}" height="{W * 599 / 1916:.0f}" preserveAspectRatio="xMidYMid slice"/>',
        f'<rect width="{W}" height="{H}" fill="url(#d)"/><rect width="{W}" height="{H}" fill="url(#halo)"/>',
        '<g filter="url(#shadow)">',
        bv.centered(title, "cinzel700", 44, cx, H / 2 + 6, spacing=8, fill="url(#gold)"),
        bv.centered(sub, "cormI", 22, cx, H / 2 + 42, fill=bone),
        bv.ornament(cx, H / 2 - 42, 120, gold),
        '</g></svg>'])

async def render(svg_text, W, H, out, scale):
    tmp = pathlib.Path(out).with_suffix(".svg"); tmp.write_text(svg_text)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = await b.new_page(viewport={"width": W, "height": H}, device_scale_factor=scale)
        await pg.goto(f"file://{tmp.resolve()}"); await pg.wait_for_timeout(500)
        png = pathlib.Path(out).with_suffix(".png"); await pg.screenshot(path=str(png)); await b.close()
    Image.open(png).convert("RGB").save(out, quality=86, optimize=True, progressive=True)
    png.unlink(); tmp.unlink()

if __name__ == "__main__":
    banner_bg, social_bg, outdir = args
    asyncio.run(render(svg(banner_bg, 1280, 400, 1.0, 190), 1280, 400, f"{outdir}/banner.jpg", 2))
    asyncio.run(render(svg(social_bg, 1280, 640, 1.3, 300), 1280, 640, f"{outdir}/social-preview.jpg", 1))
    land = os.path.join(os.path.dirname(__file__), "..", "assets", "art", "landscape.jpg")
    for name, title, sub in [("roadmap-pt", "O ROADMAP", "Do zero a AI Engineer em nove círculos"),
                             ("roadmap-en", "THE ROADMAP", "From zero to AI Engineer in nine circles"),
                             ("saga-pt", "A SAGA", "As Cinzas de Aethelgard"),
                             ("saga-en", "THE SAGA", "The Ashes of Aethelgard")]:
        asyncio.run(render(strip(land, title, sub), 1280, 200, f"{outdir}/strip-{name}.jpg", 2))
    print("ok")
