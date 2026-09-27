#!/usr/bin/env python3
"""
Ensambla la versió autònoma d'un document a partir de la font editable.
Ús:  python3 build/assemble.py  web-<doc>-...html  artifact-<doc>-...html
  1. Treu el <link> de Google Fonts i injecta build/fonts.css (@font-face base64).
  2. Substitueix assets/lockup_light.png pel data-URI de build/logo.datauri.
  3. Incrusta QUALSEVOL altra imatge local (src="...jpg/png/webp/svg/gif") com a
     data-URI, perquè l'autònom no depengui de cap fitxer extern (equip/, etc.).
  4. Manté <!DOCTYPE>, <meta charset> i viewport (imprescindibles per servir directe).
"""
import sys, re, base64, mimetypes, pathlib

HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE / "fonts.css").read_text(encoding="utf-8").strip()
LOGO = (HERE / "logo.datauri").read_text(encoding="utf-8").strip()

def inline_images(html, base_dir):
    """Reemplaça src="ruta/local.ext" per un data-URI en base64 si el fitxer existeix."""
    def repl(m):
        src = m.group(1)
        if src.startswith(("data:", "http:", "https:", "//")):
            return m.group(0)
        path = (base_dir / src).resolve()
        if not path.is_file():
            print(f"  ⚠ imatge no trobada, es deixa tal qual: {src}")
            return m.group(0)
        mime = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        b64 = base64.b64encode(path.read_bytes()).decode("ascii")
        print(f"  ✓ incrustada {src} ({path.stat().st_size:,} B)")
        return f'src="data:{mime};base64,{b64}"'
    return re.sub(r'src="([^"]+)"', repl, html)

def main(src_path, out_path):
    src_path = pathlib.Path(src_path)
    html = src_path.read_text(encoding="utf-8")
    html = re.sub(r'\s*<link rel="preconnect"[^>]*>', "", html)
    html = re.sub(r'\s*<link href="https://fonts\.googleapis\.com[^>]*>', "", html)
    html = html.replace("<style>", "<style>\n" + FONTS + "\n", 1)
    html = html.replace("assets/lockup_light.png", LOGO)
    html = inline_images(html, src_path.resolve().parent)
    pathlib.Path(out_path).write_text(html, encoding="utf-8")
    print(f"escrit {out_path}  ({len(html):,} bytes)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
