# -*- coding: utf-8 -*-
# Contenido del moodboard GUDCUK. Fuente única para la página HTML y el MOODBOARD.md.

BRAND = {
    "name": "GUDCUK Catering",
    "logo_text": "GUD CUK · CATERING",
    "instagram": "https://www.instagram.com/gudcukcatering/",
    "tagline": "Hacemos de tu evento algo memorable.",
}

TITLE = "GUDCUK — WEDDING PLANNERS | CINEMATIC AD MOODBOARD | 25s"

FILES = [
    ("video_1.mp4", "Video de referencia", "Analizado", "27,8 s · 720×1280 · 30 fps · H.264 + audio AAC. Se extrajeron 16 fotogramas, uno por plano."),
    ("GUD CUCK _ Almuerzos y Cenas _ PDF Comercial.pdf", "PDF · 5 págs.", "Analizado", "Selección Corporativa, Selección Social y Menú Kids."),
    ("GUD CUCK _ Buffets Temáticos _ PDF Comercial.pdf", "PDF · 6 págs.", "Analizado", "Buffets Criollo, Oriental, Italiano e Internacional."),
    ("GUD CUCK _ Cócteles _ PDF Comercial.pdf", "PDF · 4 págs.", "Analizado", "Formatos de cóctel, bocaditos salados y dulces."),
    ("GUD CUCK _ Desayunos_ PDF Comercial.pdf", "PDF · 7 págs.", "Analizado", "Línea corporativa. Solo se usó la página Servicio y logística."),
    ("GUD CUCK _ Mesa de Postres _ PDF Comercial.pdf", "PDF", "No recibido", "No se subió a la sesión. No se cita ningún producto de este catálogo."),
    ("GUD CUCK _ Mesas Saladas _ PDF Comercial.pdf", "PDF", "No recibido", "No se subió a la sesión. No se cita ningún producto de este catálogo."),
    ("instagram.com/gudcukcatering", "Perfil de Instagram", "No verificable", "Instagram exige iniciar sesión; no se pudo leer el perfil."),
]

BRIEF = {
    "objective": "Que un wedding planner vea a GUDCUK como un proveedor de catering confiable para sus próximos matrimonios y le escriba por WhatsApp para cotizar.",
    "audience": "Wedding planners y organizadores de matrimonios que contratan y responden por el catering frente a los novios.",
    "insight": "El planner diseña el matrimonio y responde por cada proveedor. Del catering espera tres cosas: que se vea a la altura de la ambientación, que cada tiempo salga cuando debe y que el equipo no le genere problemas.",
    "concept": "A la altura de tu diseño",
    "concept_line": "Tú diseñas el matrimonio. GUDCUK hace que lo que se sirve esté a la altura: del cóctel al último plato, servido a tiempo.",
    "positioning": "Catering que se integra a la ambientación del evento y se ejecuta con precisión. Atributos documentados en los PDFs: presentación cuidada, montajes impecables, equipo profesional, puntualidad garantizada, logística eficiente y propuesta personalizada.",
    "not_this": "No es un anuncio de decoración ni de locación. Desde el segundo 3, cada plano tiene comida, bebida o servicio como sujeto principal.",
    "format": "25 s · vertical 9:16 · 1080×1920 · Reels y pauta vertical · textos en español añadidos en edición · prompts en inglés.",
    "cta": "Cotiza por WhatsApp (CTA que usan los 4 PDFs). El número no figura en los documentos: pendiente.",
    "copy": [
        ("E1", "Diseñas matrimonios inolvidables."),
        ("E2", "Cuidas cada detalle."),
        ("E3", "Nosotros también. Desde el cóctel…"),
        ("E4", "…hasta el último plato."),
        ("E5", "Servido a tiempo, por un equipo profesional."),
        ("E6", "Tus novios disfrutan. Tu evento fluye."),
        ("E7", "GUDCUK Catering · Catering para matrimonios · Cotiza por WhatsApp"),
    ],
}

VIDEO_SPECS = [
    ("Duración", "27,8 s"),
    ("Resolución", "720×1280 (9:16)"),
    ("Cuadros", "30 fps, H.264"),
    ("Audio", "AAC estéreo 44,1 kHz. No pude escucharlo: no confirmo si hay voz en off o música."),
    ("Planos", "15 cortes detectados = 15 planos + placa final"),
    ("Duración media", "1,7 s por plano (0–25 s)"),
    ("Texto", "Subtítulos blancos pequeños, centrados a media altura"),
]

# (fotograma, inicio, fin, descripción observada, texto en pantalla, cámara observada, función narrativa)
SHOTS = [
    ("shot01", "00:00.0", "00:01.9", "PP: una mano toma un crostini con pesto de una bandeja blanca.", "¿Te casas? / Entonces hablemos de la comida.", "Casi fija, foco corto", "Gancho: pregunta directa y comida en el primer cuadro"),
    ("shot02", "00:01.9", "00:02.9", "PM: mesero cruza con bandeja entre invitados; copas y follaje en primer término.", "Entonces hablemos de la comida.", "Lateral leve, primer término desenfocado", "Sitúa al espectador en el matrimonio"),
    ("shot03", "00:02.9", "00:04.1", "PG en picado: buffet con ollas de barro.", "¿Un buffet criollo?", "Avance leve", "Catálogo: Buffet Criollo"),
    ("shot04", "00:04.1", "00:05.3", "PM: bandejas de pasta en un buffet.", "¿Italiano?", "Casi fija", "Catálogo: Buffet Italiano"),
    ("shot05", "00:05.3", "00:06.8", "PP: sartén de cobre, pinzas sirviendo.", "¿Oriental?", "Fija; la acción la hacen las pinzas", "Catálogo: Buffet Oriental"),
    ("shot06", "00:06.8", "00:08.0", "PM: makis y bocados con flores blancas y jarrones dorados.", "¿Nikkei?", "Avance leve", "Catálogo: nikkei"),
    ("shot07", "00:08.0", "00:09.1", "PM: mesa de quesos y charcutería al aire libre.", "¿Mesa de quesos?", "Avance leve", "Catálogo: mesa salada"),
    ("shot08", "00:09.1", "00:10.3", "PM: personal con pinzas monta mini postres en pedestales blancos.", "¿y postres?", "Fija", "Catálogo: postres + mano de obra"),
    ("shot09", "00:10.3", "00:11.8", "PM: una persona del equipo ordena bocaditos en una mesa bajo carpa.", "Porque una experiencia así", "Fija", "Bisagra: del menú al proceso"),
    ("shot10", "00:11.8", "00:14.4", "POV tras un mesero con bandeja de pizarra hacia el salón.", "no se improvisa. / Cada detalle cuenta,", "Seguimiento (travelling)", "Servicio en marcha; el plano más largo hasta aquí"),
    ("shot11", "00:14.4", "00:16.7", "PP: cocina, chefs de negro, manos con guantes emplatando.", "cada plato llega en su momento.", "Avance a ras de plato con cambio de foco", "Backstage: prueba de profesionalismo"),
    ("shot12", "00:16.7", "00:18.5", "PM: manos de mesero llevando tres platos.", "Detrás, un equipo hace que todo fluya. Para que ustedes", "Seguimiento lateral", "Servicio"),
    ("shot13", "00:18.5", "00:20.0", "PP: vieira sobre salsa oscura con microhojas; entra una mano.", "(continúa el texto anterior)", "Fija, foco corto", "Plato héroe"),
    ("shot14", "00:20.0", "00:22.8", "PM: mesa de panes, jamón y aceitunas; invitados detrás.", "solo tengan que disfrutar. / De lo demás, / nos encargamos nosotros.", "Avance lento", "Abundancia + invitados"),
    ("shot15", "00:22.8", "00:25.1", "PM: novios riendo en la mesa, plato en primer término.", "¿Ya tienes fecha? / Hablemos.", "Fija", "Emoción + CTA verbal"),
    ("shot16", "00:25.1", "00:27.8", "Placa negra con el logo GUD CUK CATERING en blanco.", "(sin texto)", "Fija", "Cierre de marca, 2,7 s"),
]

VIDEO_READING = [
    "Estructura en cuatro tiempos: gancho con pregunta (0–2 s), catálogo rápido de seis opciones (2–10 s), argumento de proceso y equipo (10–20 s) y resolución emocional con CTA (20–25 s), más la placa de logo.",
    "Ritmo: la primera mitad corta cada ~1,2 s y la segunda se alarga a 1,8–2,8 s. Acelera para mostrar variedad y frena para dar confianza.",
    "Color: dominante cálido (hora dorada, carpas, velas). La cocina (00:14.4) rompe la continuidad con un tono frío y verdoso.",
    "Habla a los novios (¿Te casas?, Para que ustedes…). No le habla al wedding planner.",
]

KEEP = [
    "Comida en el primer fotograma y una pregunta como gancho.",
    "Primeros términos desenfocados (copas, follaje, platos) que dan profundidad.",
    "Backstage de cocina y meseros: es justo lo que el planner necesita ver.",
    "Cerrar con personas felices y un plato en primer término.",
]

IMPROVE = [
    "Cambiar de público: hablarle al wedding planner, no a la pareja.",
    "Seis opciones en 7 s se leen como lista. Mostrar menos productos, más tiempo en pantalla y solo los documentados (Mesa de quesos y vieiras no aparecen en los 4 PDFs recibidos).",
    "Unificar el etalonaje cálido: algunos planos tienen saturación y texturas de IA y la cocina sale fría.",
    "Subtítulos más grandes y dentro de la zona segura de Reels.",
    "La placa final no tiene CTA ni contacto, y la marca no aparece hasta el segundo 25.",
]

IDENTITY = {
    "palette": [
        ("Vino GUDCUK", "#43080A", "Títulos, bandas de CTA, placa final"),
        ("Oro viejo", "#B07A27", "Precios, sellos, acentos y CTA"),
        ("Marfil", "#F4ECE2", "Fondos, texto sobre vino"),
        ("Negro café", "#1E1E1E", "Línea Desayunos y textos"),
    ],
    "observed": [
        "Logotipo: GUD / CUK apilado dentro de un cuadrado con marcas de corte y CATERING debajo. Vino sobre marfil (Almuerzos, Buffets, Cócteles), negro sobre blanco (Desayunos) y blanco sobre negro (placa del video).",
        "Tipografía: display condensada alta en mayúsculas para títulos, sans geométrica para texto y un script dorado de acento en Desayunos.",
        "Imágenes de los PDFs: luz cálida de velas, flores blancas (rosas, lirios), copas de vino, mantel marfil, cubiertos dorados y fondo en bokeh.",
        "Frase de marca: Hacemos de tu evento algo memorable.",
    ],
    "direction": [
        ("Luz", "De hora azul a luz de velas, 2700–3200 K. Contraluces suaves, sin flash."),
        ("Paleta del anuncio", "Marfil, oro viejo y vino con verde follaje. La comida aporta el amarillo del ají y el rojo del atún."),
        ("Composición", "Vertical con el sujeto en el tercio central y aire arriba y abajo para los textos. Primer término desenfocado (copas, velas, flores)."),
        ("Ópticas", "35 mm para generales, 50 mm para medios y 85–100 mm macro para comida. f/1.8–2.8."),
        ("Movimiento", "Uno solo por plano, lento y motivado: push-in, travelling lateral o rack focus."),
        ("Textura", "Grano fino de película y halación suave en las luces. Nada de look plástico."),
        ("Etalonaje", "Altas luces cálidas, negros apenas levantados y piel natural. Un mismo LUT para todo el corte."),
    ],
}

# Inventario documentado (resumen) — página del PDF y folio impreso
OFFER = [
    ("Almuerzos y Cenas", "Selección Social", "S/75 por persona · entrada + fondo + postre servidos", "PDF p.4 (folio 03)", "Mayor valor gastronómico. Pensada para celebraciones, cenas privadas y eventos donde la comida también forma parte de la experiencia."),
    ("Almuerzos y Cenas", "Selección Corporativa", "S/70 por persona", "PDF p.3 (folio 02)", "Reuniones y eventos corporativos."),
    ("Almuerzos y Cenas", "Menú Kids", "S/40 por niño", "PDF p.5 (folio 04)", "Complemento para eventos con niños."),
    ("Buffets Temáticos", "Criollo · Oriental · Italiano · Internacional", "S/110 · S/98 · S/120 · S/110 por persona · mínimo 35", "PDF p.2–6", "Italiano marcado como experiencia más gastronómica."),
    ("Cócteles", "Completo · Equilibrado · Ligero", "S/105 · S/85 · S/65 por persona · mínimo 30", "PDF p.2 (folio 02)", "El Completo incluye brindis con espumante, 1 ronda de cóctel, 4 fríos, 4 calientes y 2 dulces."),
    ("Cócteles", "Bocaditos salados y dulces", "6 familias saladas y 6 dulces", "PDF p.3–4", "Incluye Causas y bocados Nikkei, Bocados criollos y especiales y Postres en vasito."),
    ("Desayunos", "Servicio y logística", "Atributos de servicio", "PDF p.6 (folio 06)", "Atención personalizada, equipo capacitado, puntualidad garantizada, montajes impecables, logística eficiente."),
]

OFFER_NOTES = [
    "Ningún PDF usa las palabras matrimonio o boda. Hablan de celebraciones sociales, eventos sociales y eventos especiales. El enfoque en matrimonios sale del brief y del video de referencia: hay que validarlo con la marca.",
    "Todos los precios son por persona y no incluyen IGV.",
    "Las fotos de los PDFs parecen generadas por IA (tazas y termos con logo, platos idénticos). No sirven como prueba de cómo se ve el producto real.",
]

# Productos seleccionados: (nombre, fuente, cita del PDF, escena, por qué; puntajes visual, presentación, matrimonio, cine, premium)
PRODUCTS = [
    ("Brindis con espumante", "Cócteles · PDF p.2 (Cóctel Completo)", "Brindis con espumante", "E2", "Es un ritual de matrimonio y abre la experiencia gastronómica. Burbujas y vertido dan movimiento natural a la IA.", (5, 4, 5, 5, 5)),
    ("Bocaditos en bandeja (formato cóctel)", "Cócteles · PDF p.1–2", "Formato ágil. Ideal para eventos donde los invitados circulan y conversan.", "E3", "Muestra servicio y comida a la vez: el momento del cóctel es donde un planner más nota a un buen catering.", (4, 4, 5, 4, 4)),
    ("Tartar de atún oriental", "Cócteles · PDF p.3 (familia 3: Causas y bocados Nikkei)", "Tartar de atún oriental", "E3", "Rojo intenso, textura brillante y formato bocado. Lee premium en macro.", (5, 5, 4, 5, 5)),
    ("Mini causa de atún nikkei", "Cócteles · PDF p.3 (familia 3)", "Mini causa de atún nikkei", "E3 (alternativa)", "Identidad peruana y amarillo de causa que conecta con la paleta. Alternativa al tartar.", (4, 4, 4, 4, 4)),
    ("Tiradito de ají amarillo", "Almuerzos y Cenas · PDF p.4 (Selección Social, entrada)", "Finas láminas de pescado, leche de tigre de ají amarillo, zarza chalaca e hilos de camote.", "E4", "Plato emblemático peruano con salsa amarilla intensa. El vertido de leche de tigre es la acción del plano.", (5, 5, 5, 5, 5)),
    ("Pescado anticuchero", "Almuerzos y Cenas · PDF p.4 (Selección Social, fondo)", "Filete de pescado a la parrilla con salsa anticuchera y risotto huancaíno.", "E4", "Fondo de cena de gala: marcas de parrilla, glaseado y risotto cremoso. Vapor = vida en el plano.", (5, 4, 5, 4, 4)),
    ("Servicio de mesa y montaje", "Almuerzos y Cenas · PDF p.1 · Desayunos · PDF p.6", "Nosotros lo servimos: presentación cuidada y atención profesional. Montajes impecables. Puntualidad garantizada.", "E5", "Es el argumento B2B: precisión, sincronía y equipo.", (4, 5, 5, 4, 5)),
    ("Tiramisú de café", "Cócteles · PDF p.4 (Postres en vasito) · Buffets · PDF p.4 (Italiano)", "Tiramisú de café", "E6", "Capas visibles en vasito; la cuchara crea la acción. Cierra la cena.", (5, 4, 4, 5, 4)),
]

PRODUCT_ALTS = [
    ("Tres leches de chocolate", "Almuerzos y Cenas · PDF p.4", "…ganache de chocolate, con tulipa de chocolate orgánico. Alternativa de postre plato."),
    ("Suspiro limeño en shot", "Buffets · PDF p.2 (Criollo)", "Alternativa peruana de postre en vasito."),
    ("Trufitas de chocolate", "Cócteles · PDF p.4", "Alternativa de bocadito dulce."),
    ("Buffet Italiano (antipasto)", "Buffets · PDF p.4", "Ensalada Roma con prosciutto, laminado de verduras. Estación de buffet si el cliente prefiere ese formato."),
    ("Langostinos pasional con togarashi y maracuyá", "Cócteles · PDF p.3 (familia 5)", "Alternativa de bocadito caliente."),
]

EXCLUDED = [
    "Desayunos, Coffee Breaks y Tea Times: línea corporativa, no encaja con matrimonio.",
    "Menú Kids: útil para el planner, pero no aporta imagen premium.",
    "Mesa de quesos, mesas saladas y mesa de postres: sus PDFs no se recibieron, no hay respaldo documental.",
    "Vieiras (video original, 00:18.5): no aparecen en los PDFs recibidos.",
]

# Pins: id -> datos curados
PINS = {
    "1103100502517478668": dict(scene="E1", role="principal", what="Mesas largas de madera bajo un techo de luces colgantes, velas encendidas, hora azul.", why="Establece en 1 s un matrimonio de nivel con la mesa ya puesta: el catering llegó antes que los invitados.", move="Push-in lento a lo largo de la mesa.", risk="700×1072: hace falta reescalar a 1080×1920. Sillas y luces pueden deformarse con movimientos rápidos."),
    "194640015136235347": dict(scene="E1", role="alternativa", what="Mesa larga en invernadero, guirnalda verde y velas.", why="Misma intención con luz de día cálida.", move="Travelling lateral lento.", risk="Muchas copas: riesgo de deformación."),
    "563018699987638": dict(scene="E1", role="alternativa", what="Mesa larga junto a una casona de piedra al anochecer, candelabros colgantes.", why="Más sobria; buena si la locación es una casa hacienda.", move="Push-in desde el pasto.", risk="Cielo plano; sin personas."),
    "235172411767956567": dict(scene="E2", role="principal", what="Puesto de mesa con velas, candelabros plateados, bajo plato de cristal y servilleta verde.", why="Detalle de montaje: dice cuidado sin necesidad de texto.", move="Rack focus de la llama al plato.", risk="Reflejos en cristal pueden parpadear."),
    "250935010475507002": dict(scene="E2", role="principal", what="Torre de copas coupé; el espumante cae en cascada.", why="Brindis con espumante del Cóctel Completo; el líquido da movimiento natural.", move="Tilt up lento siguiendo el chorro.", risk="500×721 (baja resolución). La física de líquidos en IA falla a menudo: generar varias variantes."),
    "343047696645677574": dict(scene="E2", role="alternativa", what="Mesa marfil con rosas, velas y bajo plato dorado.", why="Referencia de estilo para el montaje.", move="Push-in suave.", risk="Firma MEYLEMON visible y posible imagen generada por IA."),
    "667799451024906745": dict(scene="E2 / E6", role="alternativa", what="Invitados brindan de pie en una mesa larga al atardecer.", why="Brindis colectivo: une comida, invitados y celebración.", move="Push-in por el eje de la mesa.", risk="Muchas manos y rostros: alto riesgo de anatomía incorrecta."),
    "810155420513882963": dict(scene="E3", role="principal", what="Mesero con delantal negro ofrece una bandeja de bocaditos sobre cama de frijoles.", why="Comida y servicio en el mismo cuadro: el cóctel en acción.", move="Dolly back mientras el mesero avanza; entra la mano de un invitado.", risk="Logo de otra empresa (Inside Out Eventz) en el delantal: retirarlo antes de animar o usar solo como referencia."),
    "77687162324098652": dict(scene="E3", role="principal", what="Tartar de atún sobre chips de nori en pizarra, cenital.", why="Referencia visual del Tartar de atún oriental documentado.", move="Rotación lenta de 5° + descenso suave.", risk="Bajo riesgo; la mezcla de cubos puede cambiar de forma."),
    "422564377565455217": dict(scene="E3", role="alternativa", what="Bocaditos en base de tres pisos con invitados de matrimonio desenfocados detrás.", why="Contexto de matrimonio con la comida en primer término.", move="Rack focus de la comida a los invitados.", risk="Posible imagen generada por IA; pocillos de aluminio poco premium."),
    "548735535867295793": dict(scene="E3", role="alternativa", what="Causa limeña de atún en molde redondo.", why="Referencia de forma y color para la mini causa de atún nikkei.", move="Push-in macro.", risk="Formato plato, no bocadito: reducir escala en el prompt."),
    "687502699428178549": dict(scene="E3", role="alternativa", what="Tartar de atún en conos de sésamo y miso.", why="Bocado de autor, muy cinematográfico.", move="Macro con rack focus.", risk="La imagen trae una franja de texto de interfaz arriba: recortar."),
    "521010250662396060": dict(scene="E4", role="principal", what="Tiradito con leche de tigre de ají amarillo en bowl oscuro.", why="Encuadre y luz ideales para el Tiradito de ají amarillo.", move="Push-in 10% + vertido de leche de tigre.", risk="La referencia usa salmón, naranja y palta; GUDCUK lleva zarza chalaca e hilos de camote. Ajustar la imagen base."),
    "45247171229006990": dict(scene="E4", role="principal", what="Filete de pescado a la parrilla sobre risotto amarillo.", why="Analogía directa del Pescado anticuchero con risotto huancaíno.", move="Órbita lateral de 10° con vapor sutil.", risk="Horizontal 736×552: recortar a 9:16 o extender (outpaint) antes de animar."),
    "423127327464116103": dict(scene="E4", role="alternativa", what="Tiradito de pejerrey en salsa de ají amarillo.", why="El más fiel a un tiradito peruano.", move="Cenital con vertido.", risk="Horizontal 736×434: baja resolución vertical."),
    "468726273735139214": dict(scene="E4", role="alternativa", what="Tiradito de pescado (Peru for Less).", why="Referencia de producto auténtica.", move="Push-in.", risk="Horizontal 735×386."),
    "736760820272359912": dict(scene="E5", role="principal", what="Mesa larga con entradas idénticas servidas, velas y guirnalda.", why="Sincronía y precisión: cuarenta platos iguales a la vez.", move="Travelling lateral; manos con guantes colocan el último plato.", risk="Foto de otro catering (Infinity Events & Catering): solo referencia de composición."),
    "250372060510338947": dict(scene="E5", role="principal", what="Mesero de frac y guantes blancos con bandeja de copas, luz de velas.", why="Hospitalidad formal: el equipo es parte de la experiencia.", move="Seguimiento lateral.", risk="426×640 (baja resolución). Persona identificable: no usar su rostro en pauta."),
    "319544536073697181": dict(scene="E5", role="alternativa", what="Salón con árbol floral blanco y servicio de guante blanco (The Astorian).", why="Escala de evento de lujo.", move="Push-in amplio.", risk="Domina la decoración, no el catering."),
    "11540542788741874": dict(scene="E6", role="principal", what="Tiramisú en frascos de vidrio con cacao y bizcochos.", why="Referencia del Tiramisú de café documentado; capas visibles.", move="Una cuchara saca una porción; micro push-in.", risk="Bajo riesgo; cuidar que la crema no se derrita."),
    "267471665365495378": dict(scene="E6", role="principal", what="Novios riendo durante los discursos, velas y flores en primer término (Love My Dress).", why="Novios felices: el resultado que un planner vende.", move="Push-in muy lento.", risk="Personas reales identificables: usar solo como referencia y generar personas nuevas."),
    "14636767513578664": dict(scene="E6", role="alternativa", what="Mini tiramisús en vasito en una mesa de postres de matrimonio.", why="Contexto de matrimonio para el postre.", move="Travelling lateral.", risk="Horizontal 640×427."),
    "8092474323192784": dict(scene="E6", role="alternativa", what="Estación italiana con aceites, aceitunas y quesos en jardín.", why="Si se quiere mostrar el Buffet Italiano.", move="Push-in lateral.", risk="Botellas con marca visible."),
    "479351954111219891": dict(scene="E6", role="alternativa", what="Novio riendo a carcajadas en la recepción, blanco y negro.", why="Emoción espontánea.", move="Push-in.", risk="Blanco y negro: no encaja en la paleta; persona identificable."),
}

DISCARDED_PINS = [
    ("573997915031663894", "Marca de agua de TikTok."),
    ("637470522238340579", "Foto de stock con marca de agua (Dreamstime)."),
    ("717620521861605141", "Foto de stock con marca de agua (Shutterstock)."),
    ("496733033921995254", "Cartel con texto y logo de otra empresa."),
    ("338121884543794333", "Cerveza y mini hamburguesas: no corresponde a la oferta elegida."),
    ("427630927140360730", "Texto superpuesto en la imagen."),
]

NEG = "no text, no logos, no watermarks, no extra people, no morphing or melting food, no warped glassware or cutlery, no flicker, no sudden camera moves"

# Escenas del storyboard
SCENES = [
    dict(
        id="E1", start="00:00.0", end="00:03.0", dur="3,0 s", title="La recepción espera",
        objective="En un segundo el planner reconoce su mundo: un montaje de matrimonio cuidado a la hora azul. Las mesas ya están puestas, así que el catering llegó antes que los invitados. Le dice que este proveedor trabaja a este nivel antes de mostrar un plato.",
        refs=[("1103100502517478668", "Toma única · 3,0 s")],
        alts=["194640015136235347", "563018699987638"],
        cine=[("Plano", "General, a la altura de los ojos (1,5 m), desde la cabecera de la mesa larga"),
              ("Composición", "La mesa como línea de fuga hacia el centro del 9:16; luces colgantes en el tercio superior"),
              ("Protagonista", "La mesa puesta con velas encendidas"),
              ("Luz y color", "Velas a 2800 K contra el cielo azul del anochecer: contraste cálido y frío"),
              ("Profundidad", "f/2.8; primer término nítido, fondo suave"),
              ("Cámara", "Dolly in continuo de ~1 m en 3 s, velocidad constante, sin rotación")],
        action="La cámara avanza por la mesa. Las llamas parpadean, las luces titilan y el camino de mesa se mueve con la brisa.",
        transition="Entra en corte seco desde negro, con el texto a los 0,2 s. Sale con match de luz: del bokeh de las luces colgantes a la llama de vela en primer plano de E2.",
        audio="Ambiente exterior suave (murmullo lejano, grillos) y primer acorde de la música. Tintineo de copa en el corte.",
        text="Diseñas matrimonios inolvidables.",
        prompts=[("P1", "1103100502517478668", "Cinematic vertical 9:16 shot of an outdoor wedding reception at blue hour. Long wooden banquet tables with a white linen runner, wooden cross-back chairs, glass holders with lit candles, a canopy of warm string lights above, lawn and trees in the background. Slow, steady dolly-in along the length of the table at eye level, constant speed, no rotation. Candle flames flicker gently, the string lights twinkle softly, the fabric runner moves slightly in a light breeze. Warm 2800K candlelight against a deep blue dusk sky, shallow depth of field, fine film grain, photorealistic editorial wedding photography. Keep the table layout, chairs, glassware and light canopy stable and unchanged.")],
        higgs="Image-to-video con una imagen inicial. Generar 5 s y usar 3,0 s.",
        approval="El avance se siente como un dolly real: el primer término se mueve más que el fondo. Sillas, copas y luces no cambian de forma ni de lugar.",
    ),
    dict(
        id="E2", start="00:03.0", end="00:06.5", dur="3,5 s", title="Detalle y brindis",
        objective="Pasa de la ambientación al primer gesto de servicio: el brindis con espumante del Cóctel Completo. Al planner le dice que GUDCUK cuida el detalle de la mesa y sabe ejecutar los rituales del matrimonio.",
        refs=[("235172411767956567", "Toma A · 1,5 s"), ("250935010475507002", "Toma B · 2,0 s")],
        alts=["343047696645677574", "667799451024906745"],
        cine=[("Plano A", "PP en 3/4, levemente picado, 85 mm f/1.8"),
              ("Cámara A", "Rack focus de la llama (primer término) al puesto de mesa en 1,2 s"),
              ("Plano B", "PM frontal desde abajo"),
              ("Cámara B", "Tilt up lento siguiendo el chorro; sensación de cámara lenta"),
              ("Luz y color", "Velas cálidas y fondo oscuro en A; luz lateral cálida y fondo neutro en B"),
              ("Protagonista", "La vajilla del montaje en A; el espumante en B")],
        action="A: el foco viaja de la vela al plato. B: el espumante cae desde la botella y llena la torre piso por piso.",
        transition="A→B: corte en el destello (de la llama al brillo del espumante). Salida a E3: corte por dirección de movimiento, la copa se llena hacia abajo y entra la mano que toma un bocadito.",
        audio="Vertido y burbujeo realzados y cristal suave. La música sube.",
        text="Cuidas cada detalle.",
        prompts=[("P2", "235172411767956567", "Cinematic vertical 9:16 close-up of an elegant wedding place setting at night: tall white taper candles in silver candlesticks, a crystal-beaded glass charger plate, a folded dark green napkin, silver cutlery and small white flowers. Slow rack focus from the nearest candle flame to the place setting; the camera is nearly static with a very subtle push-in. Candle flames flicker naturally, soft warm 2700K candlelight, deep shadows, 85mm lens look, shallow depth of field, fine film grain, photorealistic. Keep plates, cutlery and candlesticks perfectly stable in shape and position."),
                 ("P3", "250935010475507002", "Cinematic vertical 9:16 shot of a champagne coupe tower on a round metal tray. Sparkling wine pours from a bottle at the top and cascades smoothly into each level of coupes, the glasses filling progressively, fine bubbles rising, a gentle overflow trickling over the rims. Static camera with a slow, subtle tilt up following the stream. Soft warm side light, warm neutral plaster background, slow-motion feel, realistic liquid physics. Keep the glasses' shape, stems and tower structure stable; only the liquid moves.")],
        higgs="Dos generaciones independientes de image-to-video. Para B generar 3–4 variantes: los líquidos fallan a menudo.",
        approval="A: el cambio de foco es suave y ningún cubierto se deforma. B: el líquido baja por gravedad, llena las copas sin atravesar el vidrio y la torre no se mueve.",
    ),
    dict(
        id="E3", start="00:06.5", end="00:10.5", dur="4,0 s", title="Cóctel de bienvenida",
        objective="Primera experiencia gastronómica: bocaditos que circulan en bandeja entre invitados. Para el planner es el momento que sostiene a los invitados mientras los novios se hacen fotos, y donde más se nota un buen catering.",
        refs=[("810155420513882963", "Toma A · 2,0 s"), ("77687162324098652", "Toma B · 2,0 s")],
        alts=["422564377565455217", "548735535867295793", "687502699428178549"],
        cine=[("Plano A", "PM a la altura de la bandeja, 50 mm f/2"),
              ("Cámara A", "Dolly back mientras el mesero avanza; la mano de un invitado entra por abajo a la derecha"),
              ("Plano B", "Cenital, 100 mm macro"),
              ("Cámara B", "Rotación horaria de 5° + descenso suave hacia el bocado central"),
              ("Luz y color", "Contraluz cálido en A; luz lateral suave sobre pizarra oscura en B"),
              ("Protagonista", "Los bocaditos")],
        action="A: el mesero ofrece la bandeja y una mano toma un bocadito. B: el macro se acerca al tartar brillante.",
        transition="A→B: match cut, la mano toma el bocado y se corta a ese tipo de bocado en macro. Salida a E4: corte por color y forma, del rojo del atún a las láminas de pescado del tiradito.",
        audio="Murmullo de cóctel, risas suaves y cristal.",
        text="Nosotros también. Desde el cóctel…",
        prompts=[("P4", "810155420513882963", "Cinematic vertical 9:16 medium shot at a wedding cocktail hour: a waiter in a plain black apron and white shirt holds a wooden tray of elegant canapés arranged on a bed of white beans: small croquettes, salmon bites with roe and cured meat rolls. The waiter steps slowly toward the camera while the camera tracks backward smoothly. A guest's hand enters from the lower right and gently picks up one canapé. Warm indoor light, shallow depth of field, photorealistic food, 50mm lens look, fine film grain. The apron has no logo or text. Keep the canapés' shapes and the tray stable; natural hand anatomy with five fingers."),
                 ("P5", "77687162324098652", "Cinematic vertical 9:16 overhead macro shot of tuna tartare canapés on crisp nori chips arranged on a dark slate surface: diced glossy raw tuna with small fruit cubes and chopped chives. Very slow clockwise rotation of about five degrees combined with a gentle crane-down toward the central canapé. Soft directional side light, glistening tuna texture, 100mm macro look, shallow depth of field, photorealistic. Keep each canapé's shape, position and toppings stable; no melting or morphing.")],
        higgs="Dos generaciones independientes. Retirar el logo del delantal en la imagen de A antes de subirla.",
        approval="La mano del invitado tiene cinco dedos y un agarre natural. Los bocaditos no cambian de forma y el atún se ve fresco y brillante.",
    ),
    dict(
        id="E4", start="00:10.5", end="00:14.5", dur="4,0 s", title="La cena, plato protagonista",
        objective="El catering como protagonista absoluto: dos platos de la Selección Social, la propuesta más elaborada, en primerísimo primer plano. Al planner le dice que la cena puede ser el recuerdo central del matrimonio, no un trámite.",
        refs=[("521010250662396060", "Toma A · 2,0 s · Tiradito de ají amarillo"), ("45247171229006990", "Toma B · 2,0 s · Pescado anticuchero")],
        alts=["423127327464116103", "468726273735139214"],
        cine=[("Plano A", "PPP en 3/4, picado a 45°, 100 mm"),
              ("Cámara A", "Push-in lento del 10%; el vertido entra desde arriba a la izquierda"),
              ("Plano B", "PP a 30°, casi a ras de mesa"),
              ("Cámara B", "Órbita lateral lenta de 10° alrededor del plato"),
              ("Luz y color", "Luz lateral cálida y fondo oscuro en A; mesa de matrimonio con velas en bokeh detrás en B"),
              ("Protagonista", "La salsa amarilla en A; el filete glaseado en B")],
        action="A: un hilo de leche de tigre de ají amarillo cae sobre las láminas de pescado. B: sube un vapor sutil del filete mientras la cámara rodea el plato.",
        transition="A→B: corte por color, del amarillo de la leche de tigre al amarillo del risotto huancaíno. Salida a E5: la toma B termina en pull back y se corta a la mesa larga con platos idénticos, de un plato a cuarenta.",
        audio="Vertido sutil y cuchara contra cerámica. La música sigue a media intensidad.",
        text="…hasta el último plato.",
        prompts=[("P6", "521010250662396060", "Cinematic vertical 9:16 close-up of a Peruvian tiradito in a dark speckled ceramic bowl: thin slices of raw white fish fanned out, bright yellow ají amarillo leche de tigre pooled beside them, thin red onion strips and fine crispy sweet potato threads on top. A thin stream of yellow sauce is poured slowly from a small spoon at the upper left onto the fish slices. Slow push-in of about ten percent. Warm directional side light, deep dark background, glossy realistic sauce, 100mm macro look, shallow depth of field, photorealistic food photography. Keep the bowl, fish slices and garnish stable; the only motion is the sauce pour and the camera."),
                 ("P7", "45247171229006990", "Cinematic vertical 9:16 close-up of a grilled white fish fillet with visible grill marks and a glossy dark anticucho-style glaze, resting on creamy yellow risotto on a white plate, set on a wedding dinner table with soft candlelight bokeh behind it. Slow lateral orbit of about ten degrees around the plate at table height. A faint wisp of steam rises from the fish. Warm 2800K light, shallow depth of field, photorealistic, appetizing texture. Keep the fillet, risotto and plate stable in shape; no morphing of food.")],
        higgs="Dos generaciones independientes. Antes de animar: en A, cambiar la guarnición de la imagen base a zarza chalaca e hilos de camote; en B, recortar o extender (outpaint) la foto horizontal a 9:16.",
        approval="La salsa fluye con física real y no deforma el pescado. El risotto conserva la textura de grano y los platos no se deforman.",
    ),
    dict(
        id="E5", start="00:14.5", end="00:18.0", dur="3,5 s", title="El servicio, a tiempo",
        objective="Es el argumento B2B central: precisión y sincronía, todos los platos iguales y a la vez. Es lo que el planner necesita: que el servicio no se atrase ni se desordene. Documentado: Equipo profesional, Puntualidad garantizada y Montajes impecables (Desayunos p.6); Nosotros lo servimos (Almuerzos p.1).",
        refs=[("736760820272359912", "Toma A · 2,0 s"), ("250372060510338947", "Toma B · 1,5 s")],
        alts=["319544536073697181"],
        cine=[("Plano A", "PM en picado de 30°, 35 mm"),
              ("Cámara A", "Travelling lateral constante de izquierda a derecha; unas manos con guantes colocan el último plato en primer término"),
              ("Plano B", "PM de perfil, 50 mm"),
              ("Cámara B", "Truck lateral que acompaña al mesero con un leve retraso"),
              ("Luz y color", "Luz suave cálida en A; contraluz ámbar de pared en B"),
              ("Protagonista", "La repetición de platos idénticos en A; el gesto del mesero en B")],
        action="A: la cámara recorre la mesa servida y el último plato se apoya en línea con los demás. B: el mesero cruza el salón con la bandeja de copas.",
        transition="A→B: la misma dirección de movimiento (izquierda a derecha) une las dos tomas. Salida a E6: salto fuerte de escala, de plano medio a macro del postre, que marca el último tiempo de la cena.",
        audio="Foley de vajilla apoyándose en sincronía y pasos suaves. La música mantiene el pulso.",
        text="Servido a tiempo, por un equipo profesional.",
        prompts=[("P8", "736760820272359912", "Cinematic vertical 9:16 shot of a long wedding dinner table with white linen, identical plated starters at every seat, water glasses, white pillar candles and a eucalyptus garland runner. Smooth lateral tracking shot from left to right along the table at a slightly high angle, constant speed. In the foreground, a server's hands in white gloves gently set down the last plate in line with the others. Soft warm light, shallow depth of field, photorealistic, elegant and orderly. Keep all plates identical, evenly spaced and stable; natural hand anatomy; no objects appearing or disappearing."),
                 ("P9", "250372060510338947", "Cinematic vertical 9:16 medium shot of a formal waiter in a black tailcoat and white gloves carrying a silver tray of wine glasses through a warmly lit wedding venue, walking slowly from left to right. The camera trucks alongside him with a slight delay. Warm candlelight and amber wall light, soft shadows, shallow depth of field, photorealistic, dignified and calm. Keep the glasses upright and stable on the tray, a consistent face and posture, natural walking motion.")],
        higgs="Dos generaciones independientes. Reescalar B (426×640) antes de animar.",
        approval="Los platos siguen idénticos y alineados durante todo el travelling. Las copas no se inclinan ni se funden con la bandeja y el andar del mesero es natural.",
    ),
    dict(
        id="E6", start="00:18.0", end="00:22.0", dur="4,0 s", title="La celebración",
        objective="Cierra el círculo: la comida forma parte del recuerdo. Postre como último tiempo y emoción de los novios. Al planner le recuerda que novios felices significan recomendaciones y nuevos clientes.",
        refs=[("11540542788741874", "Toma A · 1,5 s · Tiramisú de café"), ("267471665365495378", "Toma B · 2,5 s")],
        alts=["14636767513578664", "8092474323192784", "479351954111219891", "667799451024906745"],
        cine=[("Plano A", "PP en 3/4, 85 mm"),
              ("Cámara A", "Casi fija con micro push-in; la cuchara entra desde arriba a la derecha"),
              ("Plano B", "PM, 85 mm, velas y flores desenfocadas en primer término"),
              ("Cámara B", "Push-in muy lento"),
              ("Luz y color", "Luz natural lateral en A; noche cálida de velas en B"),
              ("Protagonista", "Las capas del tiramisú en A; la risa de los novios en B")],
        action="A: la cuchara saca una porción y deja ver las capas. B: los novios ríen; él la mira a ella.",
        transition="A→B: corte por acción, la cuchara sube y aparece la risa de la novia. Salida a E7: fundido a vino de 8 cuadros en el pico de la risa, cuando resuelve la música.",
        audio="Cuchara contra vidrio, risas y aplausos lejanos. La música llega al clímax.",
        text="Tus novios disfrutan. Tu evento fluye.",
        prompts=[("P10", "11540542788741874", "Cinematic vertical 9:16 close-up of individual tiramisu desserts in clear glass jars on a silver tray: layers of mascarpone cream and coffee-soaked ladyfingers dusted with cocoa, coffee beans on top. A small silver spoon enters from the upper right and lifts a spoonful from the front jar, revealing the layers. Camera nearly static with a very slow push-in. Soft natural side light, shallow depth of field, photorealistic dessert texture. Keep the jars, tray and layers stable; natural spoon motion; no melting."),
                 ("P11", "267471665365495378", "Cinematic vertical 9:16 medium shot of a bride and groom laughing together at their wedding reception table, candles and white flowers softly out of focus in the foreground, warm evening light. Very slow push-in. Natural, spontaneous laughter with subtle head and shoulder movement; the groom glances at the bride. Warm film tones, shallow depth of field, fine film grain, photorealistic. Keep both faces consistent and natural, with correct hands and eyes and no exaggerated expressions.")],
        higgs="A: image-to-video. B: no animar la foto de Love My Dress en una pieza publicada. Primero generar una imagen nueva de novios (text-to-image con el mismo encuadre) y animar esa.",
        approval="A: las capas del postre se ven definidas y la cuchara no atraviesa el vidrio. B: los rostros se mantienen estables y la risa no se ve forzada.",
    ),
    dict(
        id="E7", start="00:22.0", end="00:25.0", dur="3,0 s", title="Cierre de marca",
        objective="Que el planner recuerde el nombre y sepa cómo cotizar. Se reservan 3 s en lugar de 1 s porque nombre + CTA necesitan al menos 2–2,5 s de lectura en Reels.",
        refs=[],
        alts=[],
        cine=[("Fondo", "Vino #43080A, o el último cuadro de E6 desenfocado con viñeta vino"),
              ("Logo", "GUD CUK / CATERING en marfil #F4ECE2, centrado en el tercio medio"),
              ("Texto", "Catering para matrimonios (marfil) · Cotiza por WhatsApp (oro #B07A27) · @gudcukcatering"),
              ("Animación", "El logo entra con fundido y escala de 102% a 100% en 0,4 s; el CTA entra 0,3 s después y queda 2 s"),
              ("Zona segura", "Márgenes de 108 px a los lados, 220 px arriba y 250 px abajo en 1080×1920")],
        action="Placa de marca hecha en postproducción (After Effects, Premiere o CapCut), no en Higgsfield.",
        transition="Entra con fundido desde E6. Corta a negro en el último cuadro.",
        audio="Acorde final y un tintineo de copa sincronizado con la aparición del logo.",
        text="GUDCUK Catering · Catering para matrimonios · Cotiza por WhatsApp · @gudcukcatering",
        prompts=[("P12 (opcional)", None, "Abstract vertical 9:16 close-up of a single candle flame and warm golden bokeh on a deep wine-red background, extremely slow drift, soft and elegant, no text, no logos.")],
        higgs="Solo si se quiere un fondo en movimiento: text-to-video con P12. El logo y los textos se montan encima en edición.",
        approval="Logo y CTA legibles en el móvil a tamaño real, con contraste AA y dentro de la zona segura.",
    ),
]

TIMELINE_COMPARE = [
    ("Introducción visual", "00:00–00:04", "00:00.0–00:03.0", "Gancho más rápido"),
    ("Ambientación y detalles", "00:04–00:08", "00:03.0–00:06.5", "Incluye el brindis"),
    ("Primera experiencia gastronómica", "00:08–00:12", "00:06.5–00:10.5", "Cóctel de bienvenida"),
    ("Protagonismo gastronómico", "00:12–00:16", "00:10.5–00:14.5", "Tiradito + pescado"),
    ("Experiencia de servicio", "00:16–00:20", "00:14.5–00:18.0", "Sincronía del servicio"),
    ("Experiencia integral", "00:20–00:24", "00:18.0–00:22.0", "Postre + novios"),
    ("Cierre de marca", "00:24–00:25", "00:22.0–00:25.0", "3 s legibles en vez de 1 s"),
]

EDIT = [
    ("1", "E1", "P1", "00:00.0", "3,0 s", "Corte seco desde negro", "Ambiente + primer acorde"),
    ("2", "E2-A", "P2", "00:03.0", "1,5 s", "Corte en el destello de luz", "Cristal suave"),
    ("3", "E2-B", "P3", "00:04.5", "2,0 s", "Corte seco", "Vertido de espumante"),
    ("4", "E3-A", "P4", "00:06.5", "2,0 s", "Corte por dirección de movimiento", "Murmullo de cóctel"),
    ("5", "E3-B", "P5", "00:08.5", "2,0 s", "Match cut de la mano al macro", "Cristal, risas"),
    ("6", "E4-A", "P6", "00:10.5", "2,0 s", "Corte por color y forma", "Vertido de salsa"),
    ("7", "E4-B", "P7", "00:12.5", "2,0 s", "Corte por color (amarillo)", "Cuchara y cerámica"),
    ("8", "E5-A", "P8", "00:14.5", "2,0 s", "Corte de escala (de uno a cuarenta)", "Vajilla en sincronía"),
    ("9", "E5-B", "P9", "00:16.5", "1,5 s", "Misma dirección de movimiento", "Pasos suaves"),
    ("10", "E6-A", "P10", "00:18.0", "1,5 s", "Salto de escala a macro", "Cuchara en vidrio"),
    ("11", "E6-B", "P11", "00:19.5", "2,5 s", "Corte por acción", "Risas + clímax musical"),
    ("12", "E7", "P12 + gráfica", "00:22.0", "3,0 s", "Fundido a vino de 8 cuadros", "Acorde final + tintineo"),
]

EDIT_NOTES = [
    "Las duraciones suman 25,0 s: 3,0 + 3,5 + 4,0 + 4,0 + 3,5 + 4,0 + 3,0.",
    "Proyecto en 1080×1920 a 30 fps, igual que el video original. Exportar en H.264.",
    "Música de librería con licencia comercial, 90–100 BPM, con los cortes sobre el pulso. No se propone una pista concreta.",
    "Textos en la tipografía condensada de la marca, mínimo ~56 px de alto de letra a 1080 de ancho, en marfil con sombra suave. Siempre dentro de la zona segura.",
    "Un solo LUT cálido para todos los clips. Corregir aparte cualquier clip que salga frío.",
    "Si un clip falla el criterio de aprobación, regenerarlo. No tapar el defecto con transiciones.",
]

CHECKLIST = {
    "Pendientes de la marca": [
        "Confirmar que GUDCUK atiende matrimonios: los PDFs hablan de celebraciones sociales y no mencionan bodas.",
        "Enviar los PDFs Mesa de Postres y Mesas Saladas, que no llegaron a la sesión.",
        "Número de WhatsApp para el CTA.",
        "Fotos reales de los platos elegidos (tiradito, pescado anticuchero, bocaditos nikkei, tiramisú) para usarlas como imagen base. Las imágenes de los PDFs parecen generadas por IA.",
        "Confirmar que el Tiramisú de café y el Tartar de atún oriental pueden servirse en un matrimonio fuera de sus formatos (Cóctel y Buffet Italiano).",
    ],
    "Derechos e imagen": [
        "Todas las imágenes de Pinterest son de terceros y no se verificaron sus derechos: son referencias. No usarlas como imagen base de un anuncio publicado sin licencia; regenerar o fotografiar.",
        "Personas identificables (E3-A, E5-B, E6-B): no publicar sus rostros. Generar personas nuevas.",
        "Logos de terceros: delantal Inside Out Eventz (E3-A), firma MEYLEMON (alternativa E2), marcas de botellas (alternativa E6).",
        "Música y efectos con licencia comercial.",
    ],
    "Producción en Higgsfield": [
        "Confirmar en tu plan qué modelos, duraciones y funciones hay. Start & End Frames se lanzó en mayo de 2025 para planes Pro y Ultimate; no pude confirmar que siga igual.",
        "Reescalar las imágenes base de baja resolución: E1 (700×1072), E2-B (500×721), E5-B (426×640).",
        "Pasar a vertical las referencias horizontales antes de animar: E4-B (736×552).",
        "Generar entre 2 y 4 variantes por prompt y elegir con el criterio de aprobación de cada escena.",
    ],
    "Calidad": [
        "Comida sin deformaciones en ningún cuadro.",
        "Manos con cinco dedos; copas y cubiertos rígidos.",
        "Etalonaje cálido continuo de E1 a E6.",
        "Textos legibles en el móvil y dentro de la zona segura.",
        "Duración final exacta de 25,0 s.",
    ],
    "Miro": [
        "El tablero no se creó: el conector de Miro de esta sesión solo tiene herramientas de lectura. Hay que habilitar la creación de tableros y la escritura de contenido en claude.ai/customize/connectors.",
    ],
}

VALIDATION = [
    ("ok", "Se analizaron el video y 4 de los 6 PDFs."),
    ("ok", "Los platos elegidos están en los PDFs, con página citada."),
    ("ok", "Las {n_pins} referencias de Pinterest abren una página de pin real con imagen. Se comprobaron el 26-10-2026."),
    ("ok", "Las duraciones suman 25,0 s."),
    ("ok", "Hay un prompt para cada imagen base, con su ID de pin."),
    ("warn", "Faltan 2 PDFs (Mesa de Postres, Mesas Saladas)."),
    ("warn", "El enfoque en matrimonios no aparece en los PDFs: hay que validarlo con la marca."),
    ("warn", "Instagram no es legible sin iniciar sesión."),
    ("warn", "No hay fotos reales de producto: las referencias son de terceros."),
    ("no", "Tablero de Miro no creado: faltan las herramientas de escritura del conector."),
    ("no", "Los prompts no se probaron en Higgsfield: no hay acceso desde esta sesión."),
]
