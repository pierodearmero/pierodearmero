"""Lee los guiones (guiones_*.py), los valida y arma el prompt de cada slide con la plantilla de la sección 11.

Los prompts se guardan con dos marcadores, {{REALISMO}} y {{NEGATIVO}}, que la página y las exportaciones
reemplazan por los bloques comunes literales. Así cada slide no repite 1,6 KB de texto idéntico.
"""
import re

from datos_carta import DISHES
from datos_fichas import ESCENA_LOC, ESCENA_MESA, LUZ_C001
import guiones_c1_c2, guiones_c3_c4, guiones_c5_c6, guiones_c7_c8, guiones_p

TOK_POS, TOK_NEG = "{{REALISMO}}", "{{NEGATIVO}}"

# código: (cámara, composición, ¿usa mesa por defecto?, montaje)
TOMAS = {
    "E": ("Seated eye level (about 110 cm), 1-1.2 m from the near table edge, 35 mm equivalent, verticals straight.",
          "Table in the lower 60 %, the room softly behind, top 22 % calm for the title.", True,
          "Titular en el 22 % superior sobre zona calma; nunca sobre platos ni copas."),
    "T": ("Top-down, camera level about 70 cm above the tabletop, 35-50 mm equivalent, no distortion.",
          "Subject centered slightly low, real table edges and cutlery at the frame borders, top 22 % plain tablecloth for text.", True,
          "Titular arriba sobre el mantel; no tapar ningún plato."),
    "F": ("45-degree view from the diner's side, 50-60 cm from the plate, 50 mm equivalent, focus on the front edge of the food.",
          "Plate in the lower two thirds, a hint of the second cover behind, top 22 % calm.", True,
          "Titular arriba a la izquierda y descripción en 20-22 px; nunca sobre la comida."),
    "M": ("Close macro at 25-35 cm, 70-100 mm equivalent, natural shallow depth of field.",
          "Texture fills most of the frame with the real plate or table edge visible, top 20 % soft for text.", True,
          "Texto mínimo o ninguno; si lo hay, en la franja superior."),
    "H": ("Seated eye level or slightly above, 60-80 cm, 50 mm equivalent; only hands, forearms and torsos of consenting people, faces out of frame.",
          "Hands and food interacting in the lower half, top 22 % calm.", True,
          "Texto mínimo; no tapar manos ni comida."),
    "S": ("Eye level of the server, 1-1.5 m, 35-50 mm equivalent; staff member from the shoulders down or from behind, with written consent.",
          "The service gesture centered, table and plate visible, top 22 % calm.", True,
          "Texto mínimo; no tapar el gesto."),
    "W": ("Standing eye level from an aisle, 2.5-3.5 m back, 28-35 mm equivalent, verticals straight, no ultra-wide distortion.",
          "Room depth readable, real windows and fixtures exactly as in the LOC anchor, top 22 % calm.", False,
          "Titular sobre la zona calma de techo o pared; respetar las verticales."),
    "D": ("Close detail, 40-60 cm, 50-70 mm equivalent.",
          "One real material or object fills the frame, soft background, top 22 % calm.", False,
          "Texto breve en una esquina calma."),
    "G": ("Seated eye level, about 1 m, 50 mm equivalent, deliberately soft focus.",
          "Calm, low-detail crop of the real table and room used as background for a typographic slide; keep the upper two thirds free of detail.", True,
          "Slide tipográfico: titular grande centrado y subtítulo debajo; la foto es solo fondo."),
    "X": ("Two frames shot from the identical position, height, lens and light.",
          "Vertical split canvas 50/50; both halves aligned on the same table line; top 22 % calm for a shared title.", True,
          "Titular compartido arriba; etiqueta corta en cada mitad."),
    "N": ("Seated eye level, 1-1.5 m, 35-50 mm equivalent.",
          "Subject small in the lower third, generous negative space above for text, nothing else competing.", True,
          "Titular en el espacio negativo superior."),
    "K": ("Eye level in the real ORIGEN kitchen or pass, 1-1.5 m, 35 mm equivalent, only with written kitchen authorization; staff from the shoulders down.",
          "Work surface and hands in the lower two thirds; no flames, smoke or steam beyond what really happens.", False,
          "Texto mínimo; no tapar las manos del equipo."),
}
TOMA_NOMBRE = dict(E="Mesa a la altura del comensal", T="Cenital", F="Plato a 45°", M="Macro", H="Manos (con consentimiento)",
                   S="Gesto de servicio (equipo autorizado)", W="Plano amplio del salón", D="Detalle de material", G="Fondo para slide tipográfico",
                   X="Díptico", N="Espacio negativo", K="Cocina (autorización)")
LUZ = {
    "LOC-01": LUZ_C001,
    "LOC-02": ("Midday daylight from the windows at the far right of the bar, as in LOC-02; the interior stays darker; "
               "the black ceiling lamps only as accents. Neutral white balance."),
    "LOC-03": ("Bright late-morning sun through the floor-to-ceiling glass, as in LOC-03, clear sky; soft reflected light on the "
               "navy linens; shadows consistent with the glass wall."),
    "K": "The real light of the ORIGEN kitchen during lunch service; photograph it as it is, never simulate daylight that is not there.",
}
DESC_LOC = {"LOC-01": "salón clásico: boiserie oscura con cuadros, lámpara de bronce con pantallas negras, sillas de terciopelo burdeos, ventanales al fondo y a la derecha",
            "LOC-02": "barra: frente oscuro, taburetes negros, listones de madera con fotos antiguas en blanco y negro, orquídea en maceta de bronce",
            "LOC-03": "salón azul: techo de listones claros, columnas graníticas, ventanal con monograma y vista a la piscina"}
DESC_MESA = {"MESA-01": "mantel beige-taupe, copas de tallo y vasos bajos, platos de cerámica crema-gris con borde, servilletas blancas",
             "MESA-02": "mantel azul marino, plato oscuro con borde marrón, servilleta blanca, vasos bajos"}


def leer():
    textos = [m.GUIONES for m in (guiones_c1_c2, guiones_c3_c4, guiones_c5_c6, guiones_c7_c8, guiones_p)]
    out, cur = {}, None
    for line in "\n".join(textos).splitlines():
        line = line.rstrip()
        if not line:
            continue
        if line.startswith("@"):
            cur = line[1:].strip()
            if cur in out:
                raise SystemExit(f"Guion duplicado: {cur}")
            out[cur] = dict(slides=[], caption="", nota="")
        elif line.startswith("S|"):
            parts = line.split("|")
            if len(parts) != 6:
                raise SystemExit(f"{cur}: slide con {len(parts)} campos: {line[:70]}")
            _, toma, platos, accion, tit, sub = parts
            code, _, over = toma.partition("@")
            if code not in TOMAS:
                raise SystemExit(f"{cur}: código de toma desconocido {code}")
            anclas = over.split("+") if over else None
            pl = [p for p in platos.split(";") if p]
            for p in pl:
                if p not in DISHES:
                    raise SystemExit(f"{cur}: plato desconocido {p}")
            out[cur]["slides"].append(dict(toma=code, anclas_override=anclas, platos=pl, accion=accion.strip(), titular=tit.strip(), sub=sub.strip()))
        elif line.startswith("CAP|"):
            out[cur]["caption"] = line[4:].replace("\\n", "\n")
        elif line.startswith("NOTA|"):
            out[cur]["nota"] = line[5:]
        else:
            raise SystemExit(f"{cur}: línea no reconocida: {line[:60]}")
    return out


def _texto(s):
    pl = s["platos"]
    tit, sub = s["titular"], s["sub"]
    if tit == "=":
        tit = " · ".join(DISHES[p][0] for p in pl)
    if sub == "=":
        sub = DISHES[pl[0]][3] if len(pl) == 1 else " · ".join(DISHES[p][0] for p in pl)
    return tit, sub


def armar(idea, g, refs_lines, estado_idea):
    """Devuelve la lista de slides con prompt y ficha mínima para una idea."""
    n_total = len(g["slides"])
    es_car = idea["id"].startswith("C")
    slides = []
    for n, s in enumerate(g["slides"], 1):
        cam, comp, usa_mesa, montaje = TOMAS[s["toma"]]
        if s["anclas_override"]:
            anc = s["anclas_override"]
        elif s["toma"] == "K":
            anc = []
        else:
            anc = ["LOC-01"] + (["MESA-01"] if usa_mesa else [])
        for a in anc:
            if a not in DESC_LOC and a not in DESC_MESA:
                raise SystemExit(f"{idea['id']}: ancla desconocida {a}")
        loc = next((a for a in anc if a.startswith("LOC")), None)
        mesa = next((a for a in anc if a.startswith("MESA")), None)
        tit, sub = _texto(s)
        pend = []
        if loc or mesa:
            pend.append("LOC/MESA recibidas pero sin confirmar como ORIGEN")
        if s["platos"]:
            pend.append("faltan fotos de plato")
        if s["toma"] in ("H",):
            pend.append("falta consentimiento de las personas")
        if s["toma"] == "S":
            pend.append("falta autorización del equipo")
        if s["toma"] == "K":
            pend.append("falta foto real y autorización de cocina")
        if "new photo required" in s["accion"] or "only if photographed" in s["accion"]:
            pend.append("falta foto nueva de este espacio")
        estado = "BLOQUEADO" if estado_idea == "BLOQUEADO" else "PARCIAL"
        lineas = []
        if loc:
            lineas.append(f"- LOC: {loc} — {DESC_LOC[loc]} (archivo assets/loc/{loc}.jpg · provisional)")
        elif s["toma"] == "K":
            lineas.append("- LOC: PENDIENTE: no hay foto de la cocina de ORIGEN — generación final BLOQUEADA hasta recibirla")
        if mesa:
            lineas.append(f"- MESA: {mesa} — {DESC_MESA[mesa]} (archivo assets/mesa/{mesa}.jpg · provisional)")
        for p in s["platos"]:
            lineas.append(f"- PLATO: PENDIENTE: adjuntar PLATO-{p}-01 ({DISHES[p][0]}) — generación final BLOQUEADA hasta recibirla")
        if not s["platos"]:
            lineas.append("- PLATO: no aplica (toma sin comida)")
        if s["toma"] == "H":
            lineas.append("- PERSONAS: consentimiento escrito de quienes aparecen; sin rostros identificables (menores, solo con permiso de sus padres)")
        if s["toma"] == "S":
            lineas.append("- EQUIPO: autorización escrita del miembro del equipo que aparece")
        lineas.append("- MARCA: no se usa en la foto; MARCA-01 solo en el diseño posterior")
        scene = (ESCENA_LOC[loc] if loc else "the real ORIGEN kitchen or pass (no anchor yet)") + (f"; table: {ESCENA_MESA[mesa]}" if mesa else "")
        if s["platos"]:
            food = " ".join(f"{DISHES[p][0]} exactly as in PLATO-{p}-01: preserve portion, number of pieces, plating, plate, garnish and sauce placement"
                            f" (carta: \"{DISHES[p][3]}\"); add nothing." for p in s["platos"])
        else:
            food = "No food in this shot."
        luz = LUZ["K"] if s["toma"] == "K" else LUZ.get(loc or "LOC-01")
        msg = tit + (f" — {sub}" if sub else "")
        objective = (f"Slide {n} of {n_total} of the carousel \"{idea['titulo']}\": the image must support the on-image message «{msg}»."
                     if es_car else f"Single feed post \"{idea['titulo']}\": " + (f"the image must support the on-image message «{msg}»." if tit != "—" else "the image must carry the idea alone, with no text on it."))
        continuity = (f"Same table setting, linens, tableware, wood tone, window direction and color temperature across all {n_total} slides of {idea['id']}; "
                      "repeat the camera position wherever the action says 'same'." if es_car else
                      "Match the tableware, linens, wood tone and light of the attached anchors exactly.")
        texto = "Sin texto en la imagen (el mensaje va en el caption)" if tit == "—" else " / ".join(x for x in (tit, sub) if x)
        pieza = f"{idea['id']}-S{n:02d}" if es_car else idea["id"]
        prompt = "\n".join([
            f"PIEZA: {pieza}",
            f"NOMBRE: {idea['titulo']}" + (f" · slide {n}/{n_total}" if es_car else ""),
            f"TOMA: {TOMA_NOMBRE[s['toma']]}",
            f"ESTADO DE ANCLAS: {estado} — " + "; ".join(pend or ["copy sin aprobar"]),
            "REFERENCIAS MANDATORIAS A ADJUNTAR AL MODELO VISUAL:",
            *lineas,
            "INSPIRACIÓN NO LITERAL:",
            *refs_lines,
            "",
            f"OBJECTIVE: {objective}",
            f"SCENE: {scene}. Do not add any element that is not visible in the attached anchors.",
            f"FOOD LOCK: {food}",
            f"ACTION: {s['accion']} Nothing else is staged.",
            f"CAMERA: {cam}",
            f"DAYLIGHT: {luz}",
            f"COMPOSITION: {comp}",
            f"CONTINUITY: {continuity}",
            f"REALISM: {TOK_POS}",
            f"NEGATIVE: {TOK_NEG}",
            "EXPORT: 4:5 vertical, 1080x1350, no rendered text or logo.",
            "",
            f"TEXTO A SUPERPONER DESPUÉS: {texto}",
            f"INDICACIÓN DE MONTAJE: {montaje}",
        ])
        plato_ids = [f"PLATO-{p}-01" for p in s["platos"]]
        slides.append(dict(n=n, toma=s["toma"], toma_nombre=TOMA_NOMBRE[s["toma"]], anclas=anc, platos=s["platos"],
                           platos_nombres=[DISHES[p][0] for p in s["platos"]], accion=s["accion"],
                           texto=dict(titular=tit, subtitulo=sub, micro=""), montaje=montaje, estado=estado, pendientes=pend,
                           ficha_minima=f"{idea['id']} → {pieza} → {loc or '—'} → {mesa or '—'} → " + (", ".join(plato_ids) or "sin plato") + f" → {estado}",
                           prompt=prompt))
    return slides
