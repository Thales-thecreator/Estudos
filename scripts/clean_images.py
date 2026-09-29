"""Remove metadados (EXIF: GPS, câmera, data) de todas as imagens do repositório.

    python scripts/clean_images.py           # limpa no lugar
    python scripts/clean_images.py --check   # só verifica; sai com erro se houver metadados

Rode antes de commitar prints e fotos (a /mestre roda sozinha). Requer: pip install pillow
"""
import sys, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXTS = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff"}

def dirty(img):
    return bool(img.getexif()) or any(k in img.info for k in ("exif", "xmp", "XML:com.adobe.xmp", "icc_profile_gps"))

def main():
    check = "--check" in sys.argv; found = []
    for p in ROOT.rglob("*"):
        if p.suffix.lower() not in EXTS or ".git" in p.parts: continue
        try:
            with Image.open(p) as img:
                if not dirty(img): continue
                found.append(str(p.relative_to(ROOT)))
                if check: continue
                clean = Image.frombytes(img.mode, img.size, img.tobytes())
                if img.mode == "P": clean.putpalette(img.getpalette())
                icc, fmt = img.info.get("icc_profile"), img.format or "PNG"
        except OSError:
            continue
        opts = {"quality": 90} if fmt == "JPEG" else {}
        if icc: opts["icc_profile"] = icc
        clean.save(p, fmt, **opts)
    if check and found:
        sys.exit("Imagens com metadados (GPS/câmera): " + ", ".join(found) + "\nRode: python scripts/clean_images.py")
    print(("Limpos: " + ", ".join(found)) if found and not check else "Nenhum metadado encontrado.")

if __name__ == "__main__":
    main()
