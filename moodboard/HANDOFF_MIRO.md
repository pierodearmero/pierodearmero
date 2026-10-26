# Traspaso: armar el moodboard GUDCUK en Miro

- Tablero de destino: https://miro.com/app/board/uXjVEVO6-WQ= (nombre "Sin título", vacío al 26-10-2026)
- Moodboard completo con imágenes (página privada): https://claude.ai/artifact/Fmui45wbHGNkezgZHy82WS
- Texto completo con enlaces: `moodboard/MOODBOARD.md`
- Datos estructurados: `moodboard/kit/content.py` (escenas, prompts, referencias), `moodboard/kit/selected_meta.json` (metadatos de los 24 pins)

## Pasos para la sesión que tenga las herramientas de escritura de Miro

1. Confirmar que el conector de Miro ofrece `canvas_create_from_svg` / `canvas_update_from_svg` (y `image_create` para subir imágenes locales).
2. Leer la página privada con la herramienta Artifact (`action: "read"`) para recuperar los fotogramas del video y las miniaturas de los PDFs (vienen como imágenes data: dentro del HTML).
3. Imágenes de Pinterest: usar la URL `og:image` de cada pin (i.pinimg.com), o volver a descargarlas desde `https://www.pinterest.com/pin/<id>/`.
4. Crear en el tablero los marcos 01 a 08 en este orden, de izquierda a derecha:
   01 Brief y objetivo comercial · 02 Análisis del video original · 03 Identidad visual y dirección artística · 04 Productos y propuesta gastronómica · 05 Moodboard cronológico (E1 a E7 en horizontal, con conectores entre escenas) · 06 Referencias alternativas · 07 Prompts finales para Higgsfield · 08 Checklist de producción.
5. Nombre del tablero sugerido: GUDCUK — WEDDING PLANNERS | CINEMATIC AD MOODBOARD | 25s
