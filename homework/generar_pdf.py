"""Genera el PDF imprimible de ``ParcialTaller_Mejorado.md``.

Uso habitual desde la raíz del repositorio::

    python3 homework/generar_pdf.py

El comando anterior crea ``output/pdf/ParcialTaller_Mejorado.pdf``. Use
``--source`` y ``--output`` para generar el PDF de otra versión del parcial.
"""

from __future__ import annotations

import argparse
import asyncio
import html
import sys
import tempfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SOURCE = SCRIPT_DIR / "ParcialTaller_Mejorado.md"
DEFAULT_OUTPUT = SCRIPT_DIR.parent / "output" / "pdf" / "ParcialTaller_Mejorado.pdf"


STYLES = """
:root {
  --navy: #12385d;
  --blue: #1d5f9e;
  --ink: #18212b;
  --muted: #52616f;
  --border: #cbd5df;
  --soft: #eef4f9;
  --stripe: #f8fafc;
  --code: #f3f6f8;
}

* { box-sizing: border-box; }
html { background: #ffffff; }

body {
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
  font-size: 9.15pt;
  line-height: 1.38;
}

h1, h2, h3 { break-after: avoid-page; }

h1 {
  margin: 0 0 10px;
  color: var(--navy);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 20pt;
  font-weight: 700;
  line-height: 1.16;
}

h1:not(:first-of-type) { break-before: page; }

h2 {
  margin: 17px 0 7px;
  padding: 0 0 4px;
  border-bottom: 1.25px solid var(--border);
  color: var(--navy);
  font-family: Georgia, "Times New Roman", serif;
  font-size: 12pt;
  font-weight: 700;
}

h3 {
  margin: 13px 0 5px;
  color: var(--blue);
  font-size: 10pt;
  font-weight: 700;
}

p { margin: 0 0 7px; }
ul, ol { margin: 4px 0 9px; padding-left: 22px; }
li { margin: 0 0 3px; }
strong { font-weight: 700; }
em { color: var(--muted); }
a { color: var(--blue); text-decoration: none; }

hr {
  height: 0;
  margin: 15px 0;
  border: 0;
  border-top: 1px solid var(--border);
}

blockquote {
  margin: 9px 0 11px;
  padding: 7px 10px;
  border-left: 4px solid var(--blue);
  background: var(--soft);
  color: #24384a;
  break-inside: avoid-page;
}

blockquote p:last-child { margin-bottom: 0; }

code {
  padding: 1px 3px;
  border-radius: 2px;
  background: var(--code);
  color: #0f3d60;
  font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
  font-size: 0.88em;
  overflow-wrap: anywhere;
}

pre {
  margin: 7px 0 11px;
  padding: 8px 10px;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
  border: 1px solid var(--border);
  border-radius: 3px;
  background: var(--code);
  break-inside: avoid-page;
}

pre code {
  padding: 0;
  background: transparent;
  color: var(--ink);
  font-size: 7.7pt;
  line-height: 1.28;
}

table {
  width: 100%;
  margin: 8px 0 12px;
  border-collapse: collapse;
  font-size: 7.85pt;
  line-height: 1.28;
}

thead { display: table-header-group; }
tr { break-inside: avoid-page; }
th, td {
  padding: 4px 5px;
  border: 0.7px solid var(--border);
  text-align: left;
  vertical-align: top;
  overflow-wrap: anywhere;
}
th { background: var(--navy); color: #ffffff; font-weight: 700; }
tbody tr:nth-child(even) { background: var(--stripe); }
input[type="checkbox"] { accent-color: var(--blue); }

@page { size: A4; margin: 1.45cm 1.55cm 1.7cm; }
@media print {
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  a { color: var(--blue); }
}
"""


def render_markdown(source: Path) -> str:
    """Convierte el Markdown del parcial en un documento HTML imprimible."""
    try:
        import markdown
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "Falta la dependencia Markdown. Instálela con: "
            "python3 -m pip install Markdown"
        ) from error

    body = markdown.markdown(
        source.read_text(encoding="utf-8"),
        extensions=["tables", "toc", "sane_lists", "fenced_code"],
        output_format="html5",
    )
    title = html.escape(source.stem.replace("_", " "))
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>{STYLES}</style>
</head>
<body>
{body}
</body>
</html>
"""


async def print_pdf(html_path: Path, pdf_path: Path) -> None:
    """Imprime el HTML en A4 con encabezado y numeración de páginas."""
    try:
        from playwright.async_api import async_playwright
    except ModuleNotFoundError as error:
        raise RuntimeError(
            "Falta Playwright. Instálelo con: "
            "python3 -m pip install playwright && python3 -m playwright install chromium"
        ) from error

    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch()
            page = await browser.new_page()
            await page.goto(html_path.as_uri(), wait_until="networkidle")
            await page.pdf(
                path=str(pdf_path),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                display_header_footer=True,
                header_template=(
                    '<div style="width:100%; padding:0 1.55cm; color:#52616f; '
                    'font:7.5pt Arial, sans-serif; text-align:right;">'
                    'Gestión de Datos - Parcial Taller</div>'
                ),
                footer_template=(
                    '<div style="width:100%; padding:0 1.55cm; color:#52616f; '
                    'font:7.5pt Arial, sans-serif; text-align:center;">'
                    'Página <span class="pageNumber"></span> de '
                    '<span class="totalPages"></span></div>'
                ),
                margin={"top": "1.8cm", "bottom": "1.9cm", "left": "1.55cm", "right": "1.55cm"},
            )
            await browser.close()
    except Exception as error:
        message = str(error)
        if "Executable doesn't exist" in message or "playwright install" in message:
            raise RuntimeError(
                "No está instalado Chromium para Playwright. Ejecute: "
                "python3 -m playwright install chromium"
            ) from error
        raise RuntimeError(
            "No fue posible iniciar Chromium para generar el PDF. "
            "Verifique que el entorno permita ejecutar Playwright."
        ) from error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera un PDF A4 imprimible del Parcial Taller."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"Markdown de entrada (predeterminado: {DEFAULT_SOURCE.name}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"PDF de salida (predeterminado: {DEFAULT_OUTPUT.name}).",
    )
    parser.add_argument(
        "--keep-html",
        action="store_true",
        help="Conserva junto al PDF el HTML intermedio para revisión.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    output = args.output.resolve()

    if not source.is_file():
        print(f"Error: no existe el archivo {source}", file=sys.stderr)
        return 2
    if source.suffix.lower() != ".md":
        print("Error: el archivo de entrada debe tener extensión .md", file=sys.stderr)
        return 2
    if output.suffix.lower() != ".pdf":
        print("Error: el archivo de salida debe tener extensión .pdf", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    document = render_markdown(source)

    try:
        if args.keep_html:
            html_path = output.with_suffix(".html")
            html_path.write_text(document, encoding="utf-8")
            asyncio.run(print_pdf(html_path, output))
            print(f"HTML creado: {html_path}")
        else:
            with tempfile.TemporaryDirectory(prefix="parcial_taller_") as directory:
                html_path = Path(directory) / "parcial_taller.html"
                html_path.write_text(document, encoding="utf-8")
                asyncio.run(print_pdf(html_path, output))
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"PDF creado: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
