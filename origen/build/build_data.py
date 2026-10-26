"""Genera los datos de la biblioteca ORIGEN.

Uso:  python3 origen/build/build_data.py
Salida: origen/data/origen-data.json, origen-data.js, banco-240.csv, referencias.csv, prompts-todos.txt
"""
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(os.path.dirname(HERE), "data")

from datos_carta import CARTA_FUENTE, DISHES, SECCIONES, DISCREPANCIAS  # noqa: E402
from datos_banco import BLOQUES, ESTRUCTURAS, BANCO  # noqa: E402
from datos_investigacion import (  # noqa: E402
    FECHA, SEGMENTOS, SEGMENTOS_NOTA, OBJETIVOS, KPI_LABEL, APRENDIZAJES, PERFILES, PERFILES_NO_VERIFICADOS,
    NOTAS_SITIO, NOTAS_PIN_LEGACY, NOTAS_PIN_NUEVO, OPORTUNIDADES, REGLAS_TRANSFERIBLES, RECOMENDACIONES,
    LEGADO, LEGADO_GLOBAL, ACTIVOS, PENDIENTES_CLAVE)
from datos_fichas import FICHAS, ESCENA_LOC, ESCENA_MESA  # noqa: E402
import guiones  # noqa: E402

# ------------------------------------------------------------------ bloques comunes (sección 3, literales)
POSITIVO = ("Documentary premium food photography at lunchtime inside the actual ORIGEN restaurant, Country Club de Villa, Chorrillos, Lima, Peru. "
            "Use the attached LOC and MESA images as mandatory spatial references: preserve their real architecture, furniture, table surfaces, "
            "linens, window placement and daylight direction. Use the attached authentic PLATO image as mandatory food reference: preserve the exact "
            "recipe appearance, portion, plating, plate shape, garnishes and sauce placement. Authentic natural daylight only, physically consistent "
            "shadows, true-to-life white balance, real tactile textures, subtle photographic imperfections, restrained color grading, credible camera "
            "perspective, editorial yet candid atmosphere. Composition and camera angle as specified in this shot brief. Vertical 4:5, 1080x1350. "
            "Leave the marked safe area uncluttered for typography to be added separately. No in-image text, no logos.")
NEGATIVO = ("Night, sunset dinner scene, candlelit dining, artificial nightclub lighting, fictional restaurant, invented ocean view, imaginary architecture, "
            "invented food ingredients or garnish, changed plating, exaggerated portion, waxy food, plastic gloss, CGI, 3D render, illustration, surreal "
            "steam, fake condensation, unrealistic bokeh, hard studio flash, heavy HDR, oversaturation, extra fingers, distorted hands, duplicated utensils "
            "or plates, floating objects, impossible shadows, gibberish typography, watermark, invented logo, copied reference photograph.")

SRC = json.load(open(os.path.join(HERE, "fuentes_verificadas.json"), encoding="utf-8"))
SITE_IMG = {x["key"]: x for x in SRC["site_images"]}
SITES = {x["id"]: x for x in SRC["sites"]}
LEG_PINS = {x["key"]: x for x in SRC["legacy_pins"]}
NEW_PINS = {x["pin_id"]: x for x in SRC["new_pins"]}
PERFIL_NOMBRE = {p[0]: p[1] for p in PERFILES}


def slug(k):
    return f"PLATO-{k}-01"


# ------------------------------------------------------------------ referencias REF-###
def build_refs():
    refs, index = [], {}
    n = 0
    for key in sorted(NOTAS_SITIO):
        visual, luz, principio, evitar, estado, tags = NOTAS_SITIO[key]
        img = SITE_IMG.get(key)
        if not img:
            continue
        site_id = key.split("_")[0]
        perfil = next((p for p in PERFILES if p[0].replace("B", "L") == site_id or p[0] == site_id), None)
        site = SITES.get(site_id, {})
        n += 1
        rid = f"REF-{n:03d}"
        nombre = perfil[1] if perfil else site.get("name", site_id)
        refs.append(dict(id=rid, clave=f"sitio:{key}", marca=nombre, plataforma="Sitio oficial", url=site.get("final_url") or site.get("url"),
                         imagen=img["url"], autor=nombre + " (titular del sitio)", publicado="no visible", revisado=FECHA,
                         formato="Imagen de sitio web", visual=visual, luz=luz, principio=principio, evitar=evitar, estado=estado,
                         tags=tags.split(";"), derechos="© del titular. Solo moodboard interno; no republicar ni recrear.",
                         objetivo_inferido="(inferencia) " + ("mostrar el lugar" if "salón" in tags or "lugar" in tags else "mostrar el producto o el oficio")))
        index[f"sitio:{key}"] = rid
    for key, p in LEG_PINS.items():
        visual, luz, principio, estado = NOTAS_PIN_LEGACY.get(key, ("(sin anotar)", "—", "—", "verificada"))
        n += 1
        rid = f"REF-{n:03d}"
        refs.append(dict(id=rid, clave=f"pin:{key}", marca=p["domain"] or "Pinterest", plataforma="Pinterest (heredado del HTML anterior)",
                         url=p["pin_url"], imagen=p["img_url"], autor=(p["pinner"] and "@" + p["pinner"]) or "no visible en la página",
                         fuente_original=p["source_link"], publicado="no visible", revisado=FECHA, formato="Pin",
                         visual=visual, luz=luz, principio=principio, evitar="El aspecto del plato y la composición exacta.", estado=estado,
                         tags=["pinterest", "legado"], titulo_pin=p["title"], derechos="© del autor original. Solo moodboard; no publicar.",
                         objetivo_inferido="(inferencia) inspiración de luz/encuadre"))
        index[f"pin:{key}"] = rid
    for pid, p in NEW_PINS.items():
        visual, luz, principio, estado = NOTAS_PIN_NUEVO.get(pid, ("(sin anotar)", "—", "—", "verificada"))
        n += 1
        rid = f"REF-{n:03d}"
        refs.append(dict(id=rid, clave=f"nuevo:{pid}", marca=p["domain"] or "Pinterest", plataforma="Pinterest (búsqueda 26-oct-2026)",
                         url=p["pin_url"], imagen=p["img_url"], autor=(p["pinner"] and "@" + p["pinner"]) or "no visible en la página",
                         fuente_original=p["source_link"], publicado="no visible", revisado=FECHA, formato="Pin",
                         visual=visual, luz=luz, principio=principio, evitar="Copiar la imagen.", estado=estado, tags=["pinterest", "nuevo"],
                         titulo_pin=p["title"], derechos="© del autor original. Solo moodboard; no publicar.",
                         objetivo_inferido="(inferencia) inspiración"))
        index[f"nuevo:{pid}"] = rid
    return refs, index


REFS, REF_INDEX = build_refs()
REF_BY_ID = {r["id"]: r for r in REFS}

# ------------------------------------------------------------------ banco
def parse_bank():
    ideas = []
    for line in BANCO.strip().splitlines():
        parts = line.split("|")
        if len(parts) != 13:
            raise SystemExit(f"Línea mal formada ({len(parts)} campos): {line[:60]}")
        (iid, titulo, est, o1, o2, segs, platos, extra, kpi, esf, mix, gancho, nota) = [p.strip() for p in parts]
        ideas.append(dict(id=iid, titulo=titulo, estructura=est, obj1=o1, obj2=o2 or None,
                          segmentos=[s for s in segs.split(";") if s], platos=[p for p in platos.split(";") if p],
                          extra=[e for e in extra.split(";") if e], kpi=kpi, esfuerzo=int(esf),
                          mezcla=[m for m in mix.split(";") if m], gancho=gancho, nota=nota))
    return ideas


def bloque_de(iid):
    num = int(iid[1:])
    for b in BLOQUES:
        if b[0][0] == iid[0] and int(b[3][1:]) <= num <= int(b[4][1:]):
            return b
    raise SystemExit(iid)


RARAS = {"documental", "pov", "recorrido", "diccionario", "album", "escenas", "oficio", "diptico", "negativo", "sobremesa", "tipo", "bodegon"}
VISUAL5 = {"hero", "macrop", "sobremesa", "macro", "texturas", "escena", "diptico", "dosplatos"}
VISUAL3 = {"preguntas", "diccionario", "tipo"}


def puntuar(i):
    ex = set(i["extra"])
    solapa = "Solapa" in i["nota"]
    orig = 3 + (1 if i["estructura"] in RARAS else 0) + (1 if "H" in i["mezcla"] and not solapa else 0) - (1 if solapa else 0)
    rel = 3 + (1 if set(i["segmentos"]) & {"S0", "S1", "S2", "S4"} else 0) + (1 if re.search(r"club|socio|famil|domingo|sobremesa", i["titulo"] + i["gancho"], re.I) else 0)
    real = 5 if "LOC" in ex else 4 if ex & {"MESA", "EQ", "COC"} else 3 if i["platos"] else 2
    strat = 5 if (i["obj1"] in ("O3", "O6") and i["kpi"] in ("guardados", "clics_contacto")) else 4 if i["obj1"] != "O1" else 3
    vis = 5 if i["estructura"] in VISUAL5 else 3 if i["estructura"] in VISUAL3 else 4
    fac = max(1, 6 - i["esfuerzo"])
    if ex & {"PER", "EQ", "COC", "NUEVA", "UGC"}:
        anc = 1
    elif i["platos"]:
        anc = 2 if len(i["platos"]) == 1 else 1
    elif "MARCA" in ex and not ex & {"LOC", "MESA"}:
        anc = 2
    else:
        anc = 3  # solo espacio: fotos recibidas, falta confirmar que son ORIGEN
    if "DATO" in ex:
        anc = min(anc, 2)
    dif = 3 if solapa else 4
    s = dict(originalidad=min(5, max(1, orig)), relevancia=min(5, rel), origen_real=real, estrategia=strat,
             deseabilidad=vis, facilidad=fac, anclas=anc, diferenciacion=dif)
    peso = dict(originalidad=.12, relevancia=.14, origen_real=.14, estrategia=.14, deseabilidad=.10, facilidad=.14, anclas=.14, diferenciacion=.08)
    pr = round(sum(s[k] * peso[k] for k in s) / 5 * 100)
    fuertes = [k for k in s if s[k] >= 5]
    debiles = [k for k in s if s[k] <= 2]
    nombres = dict(originalidad="originalidad", relevancia="relevancia para socios", origen_real="muestra ORIGEN real", estrategia="objetivo/KPI claro",
                   deseabilidad="deseabilidad visual", facilidad="facilidad", anclas="anclas disponibles", diferenciacion="diferenciación")
    expl = (f"{pr}/100 = suma ponderada (anclas, facilidad, ORIGEN real, estrategia y relevancia 14 % c/u; originalidad 12 %; deseabilidad 10 %; diferenciación 8 %). "
            + (("Suma por: " + ", ".join(nombres[k] for k in fuertes) + ". ") if fuertes else "")
            + (("Resta por: " + ", ".join(nombres[k] for k in debiles) + ".") if debiles else ""))
    return s, pr, expl


def anclas_de(i):
    ex = set(i["extra"])
    req = []
    if "LOC" in ex:
        req.append(dict(tipo="LOC", id="LOC-01", estado="recibida · confirmar que es ORIGEN"))
    if "MESA" in ex or (i["platos"] and "LOC" not in ex):
        req.append(dict(tipo="MESA", id="MESA-01", estado="recibida · confirmar que es ORIGEN"))
    for p in i["platos"]:
        req.append(dict(tipo="PLATO", id=slug(p), estado="PENDIENTE: no hay foto", plato=DISHES[p][0]))
    labels = dict(PER="Personas/manos con consentimiento escrito", EQ="Equipo de ORIGEN con autorización", COC="Acceso y autorización de cocina",
                  DATO="Dato operativo/comercial por confirmar", UGC="Respuestas de comunidad con permiso", MARCA="Logo y sistema gráfico aprobados",
                  NUEVA="Foto nueva de un espacio no cubierto por LOC-01..03")
    for e in ["PER", "EQ", "COC", "NUEVA", "UGC", "MARCA", "DATO"]:
        if e in ex:
            req.append(dict(tipo=e, id=e, estado="PENDIENTE", detalle=labels[e]))
    return req


def estado_de(i):
    if i["nota"].startswith("Bloqueado hasta"):
        return "BLOQUEADO"
    return "PARCIAL"


TAGS_POR_ESTRUCTURA = {
    "humano": ["manos", "mesa compartida"], "oficio": ["oficio"], "escena": ["salón"], "negativo": ["luz", "editorial"],
    "macrop": ["luz", "insumo"], "hero": ["plato", "luz"], "diptico": ["díptico"], "tipo": ["editorial"], "bodegon": ["bodegón"],
    "sobremesa": ["sobremesa", "postre"], "dosplatos": ["díptico", "plato"], "campana": ["salón", "editorial"],
    "guia": ["carta", "editorial"], "ab": ["díptico"], "documental": ["mesa compartida", "luz"], "servicio": ["gesto", "oficio"],
    "tecnica": ["insumo", "bodegón"], "pov": ["salón", "luz"], "recorrido": ["salón", "lugar"], "diccionario": ["carta", "editorial"],
    "texturas": ["luz", "plato"], "ruta": ["carta", "editorial"], "macro": ["luz", "insumo"], "album": ["detalle", "archivo"],
    "escenas": ["manos", "mesa compartida"], "preguntas": ["editorial", "díptico"], "carta": ["carta", "ilustración"],
}


def refs_para(i):
    want = TAGS_POR_ESTRUCTURA.get(i["estructura"], ["luz"])
    pool = [r for r in REFS if r["estado"] in ("verificada", "diseño") and r["plataforma"] == "Sitio oficial"]
    scored = sorted(pool, key=lambda r: (-len(set(r["tags"]) & set(want)), r["id"]))
    chosen = [r["id"] for r in scored if set(r["tags"]) & set(want)][:2]
    # un pin heredado de luz para cerrar la tríada
    luz = [r["id"] for r in REFS if r["clave"] in ("pin:blinds", "pin:leafshadow", "pin:roundsun", "pin:spag2", "pin:soup1", "pin:cake1")]
    chosen.append(luz[int(i["id"][1:]) % len(luz)])
    return chosen


# ------------------------------------------------------------------ fichas completas
def prompt_slide(fid, f, s):
    platos = s["platos"]
    plato_lines = [f"- PLATO: PENDIENTE: adjuntar {slug(p)} ({DISHES[p][0]}) — generación final BLOQUEADA hasta recibirla" for p in platos] or ["- PLATO: no aplica (toma sin comida)"]
    estado = "PARCIAL — LOC/MESA recibidas pero sin confirmar como ORIGEN" + ("; faltan fotos de plato" if platos else "; copy sin aprobar")
    refs = [(REF_INDEX[k], why) for k, why in f["refs"] if k in REF_INDEX]
    ref_lines = "".join(f"- REF: {rid} — {REF_BY_ID[rid]['url']} — {why} (no copiar la imagen)\n" for rid, why in refs)
    t = s["texto"]
    texto = " / ".join(x for x in (t["titular"], t["subtitulo"], t["micro"]) if x)
    return f"""PIEZA: {fid}-S{s['n']:02d}
NOMBRE: {s['nombre']}
ESTADO DE ANCLAS: {estado}
REFERENCIAS MANDATORIAS A ADJUNTAR AL MODELO VISUAL:
- LOC: {s['loc']} — salón clásico: boiserie oscura con cuadros, lámpara de bronce con pantallas negras, sillas de terciopelo burdeos, ventanales al fondo y a la derecha (archivo assets/loc/{s['loc']}.jpg)
- MESA: {s['mesa']} — mantel beige-taupe, copas de tallo y vasos bajos, platos de cerámica crema-gris con borde, servilletas blancas (archivo assets/mesa/{s['mesa']}.jpg)
""" + "\n".join(plato_lines) + f"""
- MARCA: no se usa en la foto; MARCA-01 solo para el diseño posterior
INSPIRACIÓN NO LITERAL:
{ref_lines}
OBJECTIVE: {s['objective']}
SCENE: {ESCENA_LOC[s['loc']]}; table: {ESCENA_MESA[s['mesa']]}.
FOOD LOCK: {s['food_lock']}
ACTION: {s['action']}
CAMERA: {s['camera']}
DAYLIGHT: {f['plan_visual']['luz']}
COMPOSITION: {s['composition']}
CONTINUITY: {f['plan_visual']['continuidad']}
REALISM: {POSITIVO}
NEGATIVE: {NEGATIVO}
EXPORT: 4:5 vertical, 1080x1350, no rendered text or logo.

TEXTO A SUPERPONER DESPUÉS: {texto}
INDICACIÓN DE MONTAJE: {s['montaje']}"""


CHECKLIST = [
    "¿Este plato existe literalmente en la carta y tiene la misma apariencia que su foto?",
    "¿La vajilla, arquitectura y luz corresponden al ambiente real adjunto?",
    "¿La escena es inequívocamente de día?",
    "¿La textura parece comida auténtica y no CGI?",
    "¿La foto cuenta algo distinto de otros diez conceptos?",
    "¿El formato tiene un objetivo estratégico y KPI justificado?",
    "¿Los textos son legibles, precisos y libres de promesas no confirmadas?",
    "¿La referencia se atribuye y no se plagia?",
    "¿Se respetaron permisos, privacidad y posibilidad real de producción?",
    "¿El botón de copia/descarga cumplió lo que dice?",
]


def build_ficha(fid, f):
    out = dict(f)
    out["refs"] = [dict(id=REF_INDEX.get(k), clave=k, uso=why, url=REF_BY_ID[REF_INDEX[k]]["url"] if k in REF_INDEX else None) for k, why in f["refs"]]
    out["platos_detalle"] = [dict(clave=p, nombre=DISHES[p][0], ancla=slug(p), carta=DISHES[p][3]) for p in f["platos"]]
    slides = []
    for s in f["slides"]:
        s2 = dict(s)
        s2["prompt"] = prompt_slide(fid, f, s)
        s2["estado"] = "PARCIAL"
        s2["ficha_minima"] = f"{fid} → {fid}-S{s['n']:02d} → {s['loc']} → {s['mesa']} → " + (", ".join(slug(p) for p in s["platos"]) or "sin plato") + \
            " → " + ", ".join(r["id"] for r in out["refs"] if r["id"]) + " → PARCIAL"
        slides.append(s2)
    out["slides"] = slides
    out["checklist"] = [dict(pregunta=q, estado="pendiente" if k in (0, 1, 3, 9) else "ok" if k in (2, 5, 7) else "revisar") for k, q in enumerate(CHECKLIST)]
    return out


IDEA_BY_ID = {}
ANCLA_EXTRA = dict(PER="Personas/manos con consentimiento escrito", EQ="Equipo de ORIGEN con autorización", COC="Foto real y autorización de cocina",
                   DATO="Dato operativo/comercial por confirmar", UGC="Respuestas de comunidad con permiso", MARCA="Logo y sistema gráfico aprobados",
                   NUEVA="Foto nueva de un espacio no cubierto por LOC-01..03")


def anclas_desde_slides(i):
    out, seen = [], set()
    for s in i["guion"]["slides"]:
        for a in s.get("anclas") or []:
            if a and a not in seen:
                seen.add(a)
                out.append(dict(tipo=a.split("-")[0], id=a, estado="recibida · confirmar que es ORIGEN"))
    for p in i["platos"]:
        out.append(dict(tipo="PLATO", id=slug(p), estado="PENDIENTE: no hay foto", plato=DISHES[p][0]))
    for e in ["PER", "EQ", "COC", "NUEVA", "UGC", "MARCA", "DATO"]:
        if e in i["extra"]:
            out.append(dict(tipo=e, id=e, estado="PENDIENTE", detalle=ANCLA_EXTRA[e]))
    return out


# ------------------------------------------------------------------ ensamblar
def main():
    ideas = parse_bank()
    assert len(ideas) == 240, len(ideas)
    IDEA_BY_ID.update({i["id"]: i for i in ideas})
    ids = [i["id"] for i in ideas]
    assert ids == [f"C{n:03d}" for n in range(1, 121)] + [f"P{n:03d}" for n in range(1, 121)], "numeración"
    overlaps = {}
    for L in LEGADO:
        for t in L[4].split(";"):
            overlaps.setdefault(t, []).append(L[0])
    G = guiones.leer()
    faltan = [x for x in ids if x not in G and x not in FICHAS]
    sobran = [x for x in G if x not in ids or x in FICHAS]
    assert not faltan and not sobran, (faltan, sobran)
    for i in ideas:
        g = G.get(i["id"])
        if not g:
            continue
        n = len(g["slides"])
        if i["id"].startswith("P"):
            assert n == 1, (i["id"], n)
        else:
            assert 5 <= n <= 7 or ("Excepción" in g["nota"] and 3 <= n <= 10), (i["id"], n)
        for sl in g["slides"]:
            for p in sl["platos"]:
                if p not in i["platos"]:
                    i["platos"].append(p)
            add = {"H": "PER", "S": "EQ", "K": "COC"}.get(sl["toma"])
            if add and add not in i["extra"]:
                i["extra"].append(add)
    for i in ideas:
        b = bloque_de(i["id"])
        i["bloque"] = b[0]
        i["formato"] = "Carrusel" if i["id"].startswith("C") else "Posteo"
        i["estructura_label"] = ESTRUCTURAS[i["estructura"]]
        s, pr, expl = puntuar(i)
        i["puntajes"], i["prioridad"], i["prioridad_explicacion"] = s, pr, expl
        i["anclas"] = anclas_de(i)
        i["estado"] = estado_de(i)
        if i["id"] in FICHAS:
            i["estado"] = FICHAS[i["id"]]["estado"]
        i["platos_nombres"] = [DISHES[p][0] for p in i["platos"]]
        i["kpi_label"] = KPI_LABEL[i["kpi"]]
        i["requiere"] = sorted({dict(PER="permiso", EQ="permiso", UGC="permiso", COC="cocina", NUEVA="nueva referencia").get(e) for e in i["extra"]} - {None}
                               | ({"cocina"} if i["platos"] else set()) | ({"fotógrafo"} if i["platos"] or i["esfuerzo"] >= 3 else set()))
        i["legado"] = overlaps.get(i["id"], [])
        i["refs"] = refs_para(i)
        refs_lines = [f"- REF: {r} — {REF_BY_ID[r]['url']} — {REF_BY_ID[r]['principio']} (no copiar la imagen)" for r in i["refs"]]
        if i["id"] in G:
            g = G[i["id"]]
            i["guion"] = dict(slides=guiones.armar(i, g, refs_lines, i["estado"]), caption=g["caption"], nota=g["nota"],
                              nivel="Guion v1 con prompt por slide")
            i["anclas"] = anclas_desde_slides(i)
        i["ficha"] = i["id"] in FICHAS
        for unknown in i["platos"]:
            assert unknown in DISHES, (i["id"], unknown)

    total = len(ideas)
    mix = {k: round(100 * sum(1 for i in ideas if k in i["mezcla"]) / total) for k in "HUKV"}
    est = {e: sum(1 for i in ideas if i["estado"] == e) for e in ("LISTO", "PARCIAL", "BLOQUEADO")}
    dishes_used = {}
    for i in ideas:
        for p in i["platos"]:
            dishes_used[p] = dishes_used.get(p, 0) + 1

    plato_assets = [dict(id=slug(k), tipo="PLATO", archivo=None, titulo=v[0], seccion=v[1], precio=v[2], carta=v[3],
                         estado="PENDIENTE", piezas=dishes_used.get(k, 0)) for k, v in DISHES.items()]

    fichas = {fid: build_ficha(fid, f) for fid, f in FICHAS.items()}
    for fid, f in fichas.items():
        for sl in f["slides"]:
            sl["prompt"] = sl["prompt"].replace(POSITIVO, guiones.TOK_POS).replace(NEGATIVO, guiones.TOK_NEG)
            sl["anclas"] = [sl["loc"], sl["mesa"]]
            sl["toma_nombre"] = "Según ficha"
        i = IDEA_BY_ID[fid]
        i["guion"] = dict(slides=f["slides"], caption=f["caption"], nota="", nivel="Ficha completa")
        i["anclas"] = anclas_desde_slides(i)
    for i in ideas:
        assert i.get("guion") and i["guion"]["slides"] and i["guion"]["caption"], i["id"]

    data = dict(
        meta=dict(proyecto="ORIGEN · Restaurante Gourmet", ubicacion="Country Club de Villa, Chorrillos, Lima, Perú", version="2.0",
                  generado=FECHA, total=total, carruseles=120, posteos=120, mezcla=mix, estados=est,
                  nota="Ninguna pieza está LISTA: faltan fotos de platos, confirmar qué espacios son ORIGEN y aprobar textos."),
        reglas=dict(positivo=POSITIVO, negativo=NEGATIVO, prioridad_anclas=["LOC y MESA", "PLATO", "MARCA", "REF", "instrucciones de texto"],
                    puertas={"LISTO": "Ambiente real + plato real + carta validada + objetivo y copy aprobados.",
                             "PARCIAL": "Hay investigación y brief, pero falta una o varias anclas: se redacta sin renderizar comida ni salón finales.",
                             "BLOQUEADO": "La propuesta exige algo que no existe o no puede verificarse: replantear."},
                    checklist=CHECKLIST),
        activos=ACTIVOS + plato_assets, pendientes=PENDIENTES_CLAVE,
        carta=dict(fuente=CARTA_FUENTE, secciones=SECCIONES,
                   platos=[dict(clave=k, nombre=v[0], seccion=v[1], precio=v[2], descripcion=v[3], piezas=dishes_used.get(k, 0)) for k, v in DISHES.items()],
                   discrepancias=DISCREPANCIAS),
        legado=dict(ideas=[dict(id=L[0], nombre=L[1], platos=[DISHES[p][0] for p in L[2].split(";")], formato=L[3], solapa=L[4].split(";"), problemas=L[5]) for L in LEGADO],
                    globales=LEGADO_GLOBAL),
        investigacion=dict(fecha=FECHA, aprendizajes=APRENDIZAJES,
                           perfiles=[dict(id=p[0], nombre=p[1], grupo=p[2], lugar=p[3], url=p[4], instagram=p[5], observado=p[6], principio=p[7],
                                          aplicar=p[8], evitar=p[9], analogia=p[10], revisado=FECHA) for p in PERFILES],
                           no_verificados=[dict(nombre=a, url=b, motivo=c) for a, b, c in PERFILES_NO_VERIFICADOS],
                           referencias=REFS, oportunidades=[dict(id=a, titulo=b, texto=c, certeza=d) for a, b, c, d in OPORTUNIDADES],
                           reglas=[dict(id=a, regla=b, fuente=c, porque=d, limite=e) for a, b, c, d, e in REGLAS_TRANSFERIBLES],
                           recomendaciones=[dict(prioridad=a, texto=b, certeza=c) for a, b, c in RECOMENDACIONES],
                           limites=["Instagram no se inspeccionó: requiere sesión. Los perfiles @ se tomaron de enlaces del propio sitio oficial.",
                                    "No se usaron endpoints internos de Pinterest: solo páginas públicas de pines.",
                                    "No hay métricas reales de competidores: no se publican públicamente."]),
        segmentos=dict(lista={k: dict(nombre=v[0], descripcion=v[1]) for k, v in SEGMENTOS.items()}, nota=SEGMENTOS_NOTA),
        objetivos={k: dict(nombre=v[0], kpi=v[1], porque=v[2]) for k, v in OBJETIVOS.items()},
        kpis=KPI_LABEL, estructuras=ESTRUCTURAS,
        bloques=[dict(id=b[0], tipo=b[1], nombre=b[2], desde=b[3], hasta=b[4]) for b in BLOQUES],
        ideas=ideas, fichas=fichas,
    )
    os.makedirs(OUT, exist_ok=True)
    js = json.dumps(data, ensure_ascii=False, indent=1)
    open(os.path.join(OUT, "origen-data.json"), "w", encoding="utf-8").write(js)
    open(os.path.join(OUT, "origen-data.js"), "w", encoding="utf-8").write("/* Generado por build/build_data.py — no editar a mano */\nwindow.ORIGEN_DATA = " + js + ";\n")
    with open(os.path.join(OUT, "banco-240.csv"), "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ID", "Bloque", "Formato", "Título", "Estructura", "Objetivo 1", "Objetivo 2", "Segmentos", "Platos", "Anclas pendientes",
                    "KPI", "Esfuerzo", "Prioridad", "Estado", "Mezcla", "Gancho", "Nota", "Legado", "Referencias", "Slides", "Caption"])
        for i in ideas:
            w.writerow([i["id"], i["bloque"], i["formato"], i["titulo"], i["estructura_label"], OBJETIVOS[i["obj1"]][0],
                        OBJETIVOS[i["obj2"]][0] if i["obj2"] else "", ";".join(i["segmentos"]), "; ".join(i["platos_nombres"]),
                        "; ".join(a["id"] for a in i["anclas"]), i["kpi_label"], i["esfuerzo"], i["prioridad"], i["estado"],
                        "".join(i["mezcla"]), i["gancho"], i["nota"], ";".join(i["legado"]), ";".join(i["refs"]),
                        len(i["guion"]["slides"]), i["guion"]["caption"]])
    with open(os.path.join(OUT, "referencias.csv"), "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["REF", "Marca/fuente", "Plataforma", "URL", "Imagen", "Autor", "Revisado", "Estado", "Luz", "Descripción observada", "Principio", "Evitar", "Derechos"])
        for r in REFS:
            w.writerow([r["id"], r["marca"], r["plataforma"], r["url"], r["imagen"], r["autor"], r["revisado"], r["estado"], r["luz"], r["visual"], r["principio"], r["evitar"], r["derechos"]])
    old = os.path.join(OUT, "prompts-C001-C002.txt")
    if os.path.exists(old):
        os.remove(old)
    nprompts = 0
    with open(os.path.join(OUT, "prompts-todos.txt"), "w", encoding="utf-8") as fh:
        for i in ideas:
            fh.write(f"######## {i['id']} · {i['titulo']} ({len(i['guion']['slides'])} slides) ########\n\n")
            for s in i["guion"]["slides"]:
                fh.write(s["prompt"].replace(guiones.TOK_POS, POSITIVO).replace(guiones.TOK_NEG, NEGATIVO) + "\n\n" + "=" * 80 + "\n\n")
                nprompts += 1
            fh.write("CAPTION:\n" + i["guion"]["caption"] + "\n\n\n")
    vr = sum(1 for r in REFS if r["estado"] in ("verificada", "diseño", "solo-composición"))
    print(f"ideas={total} estados={est} mezcla={mix} refs={len(REFS)} (utilizables={vr}) perfiles={len(PERFILES)} prompts={nprompts}")


if __name__ == "__main__":
    main()
