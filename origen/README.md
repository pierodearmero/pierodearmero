# ORIGEN · Biblioteca editorial

Sistema editorial consultable para **ORIGEN, Restaurante Gourmet** (Country Club de Villa, Chorrillos, Lima):
240 conceptos (C001–C120 carruseles, P001–P120 posteos) en 16 bloques, cada uno con guion slide por slide, 793 prompts listos para copiar y caption, investigación con fuentes,
manifiesto de anclas reales, carta estructurada, fichas completas de C001 y C002, planificador y exportación.

## Abrir

Abre `index.html` en el navegador (junto a la carpeta `data/`). No necesita servidor.

Las fotos del local (`assets/loc`, `assets/mesa`) y el logo (`assets/marca`) **no están en este repositorio**:
es público y las fotos incluyen personas reconocibles. Copia tus archivos a esas carpetas con los nombres
`LOC-01.jpg`, `LOC-02.jpg`, `LOC-03.jpg`, `MESA-01.jpg`, `MESA-02.jpg`, `MARCA-01.png`, o usa
«Adjuntar» dentro de la herramienta.

## Guardado

- **Copia local:** etapas, responsables, fechas, notas, favoritos y fotos adjuntadas viven solo en tu navegador
  (localStorage e IndexedDB). Usa *Exportar y respaldo* para moverlos. No hay sincronización entre personas.
- **Como artefacto de claude.ai:** el plan y las fotos de anclas se comparten con quien abre el artefacto
  (según su nivel de acceso). La página indica en qué modo está.

## Regenerar los datos

```bash
python3 origen/build/build_data.py   # escribe data/origen-data.{json,js}, banco-240.csv, referencias.csv, prompts-todos.txt
python3 origen/build/build_page.py   # envuelve build/pagina.html en index.html
```

| Archivo | Contenido |
|---|---|
| `build/datos_carta.py` | Carta de septiembre 2026 transcrita y discrepancias D01–D09 |
| `build/datos_banco.py` | Las 240 ideas (una línea por idea) |
| `build/datos_investigacion.py` | Aprendizajes, 56 referentes, anotación de referencias, oportunidades, reglas, legado y manifiesto de activos |
| `build/datos_fichas.py` | Fichas completas C001 y C002 (guion, tomas, caption, producción, medición) |
| `build/guiones_*.py` | Guion slide por slide de C003–C120 y P001–P120: tipo de toma, platos, acción, texto en arte y caption |
| `build/guiones.py` | Valida los guiones y arma el prompt de cada slide con la plantilla de producción |
| `build/fuentes_verificadas.json` | Registro técnico de lo consultado el 26-oct-2026 (HTTP, títulos, URLs de imagen, pines) |
| `data/` | Salidas generadas: no editar a mano |

## Estado honesto

- Ninguna pieza está LISTA: no hay fotos de platos, falta confirmar qué ambientes son ORIGEN y aprobar textos.
- Instagram no se inspeccionó (requiere sesión). Las cuentas @ provienen de enlaces en los sitios oficiales.
- El visor de artefactos bloquea imágenes de otros dominios: en él, la galería muestra la descripción anotada
  y el enlace; las miniaturas se ven en esta copia local mientras los sitios de origen las sirvan.
