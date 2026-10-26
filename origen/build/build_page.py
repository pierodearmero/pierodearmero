"""Envuelve build/pagina.html (formato de artefacto, sin <html>/<head>/<body>) en un documento
completo para abrirlo localmente: origen/index.html.

Uso:  python3 origen/build/build_page.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "pagina.html"), encoding="utf-8").read()
cut = src.index('<div class="app">')
head, body = src[:cut].strip(), src[cut:].strip()
doc = ("<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
       "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
       "<!-- Generado desde build/pagina.html por build/build_page.py: editar allí. -->\n"
       + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
open(os.path.join(os.path.dirname(HERE), "index.html"), "w", encoding="utf-8").write(doc)
print("index.html", len(doc), "bytes")
