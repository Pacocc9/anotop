"""Genera Anotop_diapositivas.pdf a partir de diapositivas/anotop_diapositivas.html.

Usa Chrome (vía Playwright) para imprimir el HTML a PDF en 16:9 (1920x1080).
Antes, ejecuta el notebook para que las gráficas de figuras/ estén actualizadas.

    python generar_diapositivas_pdf.py
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent
HTML = RAIZ / "diapositivas" / "anotop_diapositivas.html"
PDF = RAIZ / "Anotop_diapositivas.pdf"

with sync_playwright() as p:
    try:
        navegador = p.chromium.launch(channel="chrome")  # Chrome instalado
    except Exception:
        navegador = p.chromium.launch()  # Chromium de Playwright
    pagina = navegador.new_page(viewport={"width": 1920, "height": 1080})
    pagina.goto(HTML.as_uri(), wait_until="networkidle")
    pagina.pdf(path=str(PDF), width="1920px", height="1080px",
               print_background=True, prefer_css_page_size=True)
    navegador.close()

print(f"{PDF.name} generado exitosamente.")
