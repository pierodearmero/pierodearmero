# Banco maestro ORIGEN: 120 carruseles (C001–C120) + 120 posteos (P001–P120).
# Formato por línea:
# ID | título | estructura | obj1 | obj2 | segmentos | platos (claves de datos_carta) | anclas extra | KPI | esfuerzo 1-5 | mezcla | gancho | nota
# Anclas extra: LOC, MESA, PER (personas/manos con consentimiento), EQ (equipo con autorización),
#   COC (cocina con autorización), DATO (dato operativo/comercial por confirmar), UGC, MARCA, NUEVA (toma de espacio aún no fotografiado)
# Mezcla: H ambiente/mesa/servicio/personas · U utilidad (elegir/comparar/conocer) · K conversación/guardado/compartido · V conversión
# Los platos implican automáticamente el ancla PLATO-<clave>-01.

BLOQUES = [
    ("C1", "carrusel", "Elegir el almuerzo: descubrimiento y utilidad", "C001", "C015"),
    ("C2", "carrusel", "La mesa y las personas: club, familia y pertenencia", "C016", "C030"),
    ("C3", "carrusel", "Insumos, técnica y oficio culinario", "C031", "C045"),
    ("C4", "carrusel", "El lugar como experiencia: arquitectura y luz real", "C046", "C060"),
    ("C5", "carrusel", "Descubrimiento cruzado y construcción del ticket", "C061", "C075"),
    ("C6", "carrusel", "Cultura gastronómica y narrativa editorial", "C076", "C090"),
    ("C7", "carrusel", "Conversación, guardados e interacción", "C091", "C105"),
    ("C8", "carrusel", "Calendario, temporadas y campañas diurnas", "C106", "C120"),
    ("P1", "posteo", "Hero shot realista de platos", "P001", "P015"),
    ("P2", "posteo", "El salón real y la atmósfera de día", "P016", "P030"),
    ("P3", "posteo", "Servicio, gesto humano y hospitalidad", "P031", "P045"),
    ("P4", "posteo", "Postres, sobremesa y final del almuerzo", "P046", "P060"),
    ("P5", "posteo", "Insumos, formas y detalles culinarios", "P061", "P075"),
    ("P6", "posteo", "Ocasiones, identidad y estilo de vida diurno", "P076", "P090"),
    ("P7", "posteo", "Diseño editorial, curiosidad y conversación", "P091", "P105"),
    ("P8", "posteo", "Conversión elegante y campañas", "P106", "P120"),
]

ESTRUCTURAS = {
    # carrusel
    "guia": "Guía de elección", "ab": "Comparativa A/B", "documental": "Documental de una mesa",
    "servicio": "Secuencia de servicio", "tecnica": "Ingrediente / técnica", "pov": "POV de almuerzo",
    "recorrido": "Recorrido espacial verificado", "diccionario": "Minidiccionario culinario",
    "texturas": "Contraste de texturas", "ruta": "Elige tu ruta", "macro": "Macro → plano general",
    "album": "Álbum de sobremesa / detalles", "escenas": "Narración editorial por escenas",
    "preguntas": "Pregunta-respuesta", "carta": "Carta comentada",
    # posteo
    "hero": "Hero gastronómico", "escena": "Escena amplia de local", "humano": "Interacción humana",
    "macrop": "Macro físico", "oficio": "Retrato de oficio autorizado", "bodegon": "Bodegón real",
    "tipo": "Tipografía editorial mínima", "diptico": "Díptico en un lienzo", "negativo": "Foto con espacio negativo",
    "sobremesa": "Detalle de sobremesa", "dosplatos": "Composición de dos platos", "campana": "Campaña con CTA discreto",
}

BANCO = r"""
C001|Primera vez en ORIGEN: ruta de cinco decisiones.|ruta|O3|O6|S0|croq;ldt;lso;arm;cvo|LOC;MESA|guardados|3|H;U;V|Cinco decisiones, en el orden en que llegan a la mesa, para que el primer almuerzo en ORIGEN no dependa del azar.|Ficha completa desarrollada. Horario en arte bloqueado hasta confirmación.
C002|Si tienes poco tiempo para almorzar: opciones por verificar en operación.|guia|O3|O6|S1|lso;arm;spk;cae;bch|LOC;MESA;DATO|guardados|3|U;V|Platos que según la carta ya llegan completos: un solo pedido resuelve el almuerzo entre actividades, sin prometer tiempos.|Reencuadrado: no se promete rapidez. Tiempos reales y posibilidad de priorizar pedidos: validar con cocina y salón.
C003|Almuerzo ligero o contundente: dos caminos de carta.|ab|O3|O2|S5;S6|gar;thai;cae;rhl;lpi;lord||guardados|3|U;K|Dos caminos para el mismo mediodía: el que deja espacio para la tarde y el que se toma su tiempo.|Lo 'ligero' se define por ingredientes de la carta, no por calorías (no hay datos nutricionales).
C004|De entrada a postre: cómo armar una experiencia completa.|escenas|O3|O6|S3|croq;tir;fpl;tcm|LOC;MESA|guardados|3|H;U|Una experiencia completa contada en cuatro tiempos, con la misma mesa y la misma luz de principio a fin.|
C005|¿Tibio o fresco? Dos maneras de empezar.|ab|O3|O2|S7;S4|ldt;tir;sop;scr||comentarios|2|U;K|Fresco o tibio: la carta tiene las dos puertas de entrada y cada una cambia el ritmo del almuerzo.|Confirmar si las sopas se piden como entrada o como fondo.
C006|El mapa de las entradas para compartir.|carta|O3|O5|S3;S4|croq;teq;ali_s;spr;cho;cpar;cori;ebi||guardados|3|U;K|Los piqueos de la carta ordenados por cómo se comparten: con la mano, con tenedor o en su concha.|Validar con salón la forma real de servicio de cada piqueo.
C007|Tres formas reales de pedir pescado.|guia|O3|O2|S7|jcl;pem;amf||guardados|3|U|Frito, en salsa de mariscos o a tu manera: el pescado del día cambia por completo según la línea de la carta.|No nombrar especie: la carta dice 'pesca del día'.
C008|¿Pasta, arroz o salteado? Decide por antojo.|ruta|O3|O2|S2;S3|fpl;fto;smc;acm;chp;lso;rhl||guardados|3|U;K|Tres antojos, tres familias de la carta: elige la textura que buscas hoy y el carrusel te lleva al plato.|
C009|Cómo elegir entre makis de la carta, sin inventar niveles de picante.|guia|O3|O5|S7|acv;kat;fuji;chili;drag;salmo;tuna;hot||guardados|3|U;K|Ocho makis descritos por lo que la carta dice que llevan —crocante, cremoso, flameado o ahumado— sin escalas de picante inventadas.|'Spicy' solo donde la carta lo dice (Chili Spicy, Tuna Tartare).
C010|Del primer bocado al último: orden de mesa.|servicio|O4|O3|S3|croq;cev;lso;cvo|LOC;MESA;PER|deslizamientos|3|H;U|El orden en que una mesa vive el almuerzo: qué llega primero, qué se comparte y qué se guarda para el final.|
C011|Dos acompañamientos, una decisión personal.|ruta|O3|O5|S5;S6|arm;g_pur;g_arr;g_pap;g_ver||comentarios|2|U;K|Cuatro acompañamientos posibles en Ármalo a Tu Manera: cómo cambia el mismo plato con cada par.|Confirmar reglas exactas de combinación (si se puede repetir acompañamiento, recargos).
C012|Para quien prefiere pollo: mapa de opciones.|carta|O3|O2|S2;S5|cpo;cae;thai;cpk;chp;fto;amp;sop||guardados|3|U|Ocho maneras en que el pollo aparece en la carta, de la causa a la sopita, para quien siempre pide 'algo con pollo'.|
C013|Para quien busca mariscos: entradas y fondos.|guia|O3|O2|S7|cho;cpar;cmx;acm;chm;jmx;smc;pem||guardados|3|U|Mariscos de principio a fin: qué entradas y qué fondos los llevan, según la carta, para armar un almuerzo de mar completo.|Solapa con L005 (Mar adentro): aquí la función es mapa, no selección de fondos.
C014|Elegir postre según el antojo del día.|ruta|O2|O3|S8|cvo;tcm;chb;cny;hel;pie||guardados|2|U;K|Seis postres, cuatro antojos —cremoso, chocolate, frutal u horneado— y una respuesta por slide.|Ver discrepancia D06 (fudge o manjar).
C015|Tu almuerzo ideal en cinco preguntas.|preguntas|O3|O5|S0|croq;cev;lso;ajs;cvo||guardados|3|U;K|Cinco preguntas —hambre, compañía, mar o tierra, ganas de compartir, postre— y una recomendación de carta al final.|
C016|Cinco momentos de un almuerzo compartido.|escenas|O4|O5|S4;S3|croq;lso;cvo|LOC;MESA;PER|compartidos|4|H;K|Cinco momentos que se repiten en cualquier almuerzo compartido, fotografiados sin pose y sin rostros identificables.|
C017|La mesa antes de que lleguen todos.|documental|O4|O1|S0||LOC;MESA|guardados|2|H|Antes del ruido: la mesa puesta, la luz de mediodía y las sillas esperando a quienes todavía están en camino.|Solo necesita anclas de espacio: candidato a producción inmediata.
C018|Un almuerzo entre generaciones.|escenas|O1|O5|S4|cvo;sop;lso;kids|LOC;MESA;PER|compartidos|4|H;K|Abuelos, padres y nietos en la misma mesa: cada generación pide distinto y todos terminan probando del plato del otro.|Consentimiento escrito de todos; menores sin rostro.
C019|POV: llegas del club y te sientas a la mesa.|pov|O1|O6|S1|cae;lso|LOC;MESA|alcance|3|H;V|Llegas del club con la tarde por delante: así se ve la mesa desde tu silla, en primera persona.|No mostrar actividades del club que no estén fotografiadas.
C020|Pedir al centro cambia la conversación.|documental|O5|O3|S3;S4|croq;cpar;ali_s;teq|MESA;PER|compartidos|3|H;K|Cuando los platos van al centro, la mesa conversa distinto: un carrusel sobre pedir para compartir.|
C021|El pequeño ritual de elegir juntos.|escenas|O5|O3|S3;S4||MESA;PER;DATO|comentarios|3|H;K|La carta pasa de mano en mano: el ritual de decidir juntos contado en manos, dedos que señalan y miradas fuera de cuadro.|Confirmar formato de carta física en mesa (impresa, QR o ambas).
C022|Almuerzo familiar sin que todos pidan lo mismo.|ruta|O3|O5|S2|kids;fpl;cev;cae|LOC;MESA|guardados|3|H;U|Una familia, cuatro pedidos distintos y una sola mesa: la carta resuelve que cada uno coma lo suyo.|Menú Kids según carta vigente (D05).
C023|Lo que pasa mientras llega el primer plato.|escenas|O4|O5|S3||MESA;PER|alcance|3|H|Lo que pasa entre el pedido y el primer plato: servilletas que se despliegan, vasos que se llenan, conversación que arranca.|No agregar pan ni aperitivos de cortesía si no se sirven.
C024|Un domingo que merece sobremesa.|album|O4|O6|S4|cvo;tcm|LOC;MESA;PER|guardados|3|H;V|El domingo sin apuro: un carrusel que empieza en el fondo y termina con la última cucharada de postre.|Respetar horario real de cierre del servicio.
C025|Cuando alguien dice «probemos un poquito de todo».|macro|O2|O5|S3|croq;teq;ali_b;cho;cpar|MESA|compartidos|3|K|'Probemos un poquito de todo': la frase que convierte la mesa en un mapa de piqueos.|
C026|Una visita, tres generaciones, varios gustos.|escenas|O5|O1|S4|cpo;mac;ajs;cvo|LOC;MESA;PER|compartidos|4|H;K|Una visita, tres generaciones: la carta como punto de encuentro entre la causa clásica y el mac & cheese.|Diferencia con C018: foco en la carta, no en el retrato familiar.
C027|El encuentro que empieza con un piqueo.|escenas|O5|O6|S3|spr;ebi;cho|MESA;PER|compartidos|3|H;K|Todo encuentro tiene un primer bocado: piqueos que abren la conversación antes de que alguien abra la carta.|
C028|Pequeños gestos de hospitalidad auténtica.|servicio|O4|O1|S0||LOC;MESA;EQ|alcance|4|H|Gestos reales del servicio —acercar, servir, retirar— fotografiados con autorización del equipo.|
C029|De la conversación al postre.|escenas|O2|O6|S8|tcm;cny;cvo|MESA;PER|guardados|3|H|La conversación sigue y el postre llega: cuatro escenas del momento en que nadie quiere levantarse.|
C030|La mesa que se disfruta sin apuro.|documental|O4|O1|S4|lso;cpo|LOC;MESA|alcance|3|H|Sin reloj a la vista: la mesa que se disfruta despacio, con luz de primeras horas de la tarde y platos que se comparten.|
C031|Del ají amarillo a una preparación real de la carta.|tecnica|O3|O2|S7|cpo;tir;rhl||guardados|3|U|El ají amarillo aparece en tres platos de la carta con tres funciones: espejo, leche de tigre y risotto.|
C032|La textura crocante contada sin trucos visuales.|texturas|O2|O3|S6|croq;ebi;teq;jcl||alcance|3|U|Quinua, panko y masa: tres crocantes de la carta tal como salen, sin brillos agregados ni migas de utilería.|
C033|El antes y después verdadero de un plato en servicio.|servicio|O4|O1|S0|lso|COC;EQ;MESA|deslizamientos|4|H|El plato al salir del pase y el mismo plato en la mesa: un antes y después sin retoque que lo cambie.|Requiere autorización de cocina.
C034|El recorrido del arroz: preparaciones contrastantes.|carta|O3|O2|S6|acm;rhl;lpi;chp;lso;cha||guardados|3|U|Cremoso, arbóreo, al wok o con choclo: el arroz cambia de idioma según la línea de la carta.|
C035|Cómo cambia un langostino según su preparación.|tecnica|O3|O2|S7|ebi;cca;acv;fuji;drag||guardados|3|U|Del panko a la causa: el langostino cambia de textura y de papel en cinco preparaciones de la carta.|
C036|El color y la textura del anticucho del Pulpito.|macro|O2|O3|S7|pul||alcance|2|U|El anticucho llevado al pulpo: color, brillo y textura de la salsa anticuchera, de cerca y luego en la mesa.|Solapa con L004: aquí se trabaja solo textura/color, no la historia del plato.
C037|Técnica visible: el punto del lomo.|tecnica|O2|O3|S6|lso;aml;lpi;fpl|COC;DATO|guardados|3|U|Cuatro platos con lomo y una pregunta honesta: cómo se ve el punto que la cocina sirve, sin exagerar el rosado.|Confirmar punto estándar y si se ofrece término a pedido.
C038|Salsa y plato: una relación real, no decorativa.|tecnica|O3|O2|S7|cpo;cca;pul;pem||guardados|3|U|Espejo, reducción, salsa anticuchera y salsa de mariscos: cada salsa de la carta cumple una función que se ve en el plato.|
C039|Los distintos lenguajes del ají en la carta.|diccionario|O3|O5|S7|cpo;hot;spr;cev;ali_s||guardados|3|U;K|Amarillo, panca, rocoto, limo y 'ajíes peruanos': los ajíes que nombra la carta y en qué plato vive cada uno.|
C040|Empanizado, gratinado, plancha: tres texturas.|texturas|O2|O3|S6|fuji;cpar;amp||alcance|2|U|Empanizado, gratinado y plancha: tres técnicas de la carta, tres superficies distintas al primer corte.|
C041|El oficio del emplatado, fotografiado de verdad.|servicio|O4|O1|S0|cca|COC;EQ|alcance|4|H|El emplatado fotografiado de verdad: manos del equipo, pausas y un plato que no se parece a un render.|
C042|Qué hace reconocible a una causa de ORIGEN.|tecnica|O3|O2|S7|cpo;cca||guardados|3|U|Masa, relleno, palta y espejo: lo que hace reconocibles a las dos causas de ORIGEN, capa por capa.|Solapa con L002 (Dos causas): aquí es anatomía, no votación.
C043|El ingrediente que conecta dos secciones de carta.|tecnica|O3|O5|S7|cpo;acv;gar;spk;cnk||guardados|3|U|La palta conecta entradas, makis, ensaladas y bowls: un hilo verde que atraviesa la carta.|
C044|El wok y el movimiento, solo con evidencia real.|tecnica|O2|O4|S6|lso;chc;cha|COC|alcance|4|H|Wok y movimiento, solo si la cocina permite fotografiarlo: el salteado contado con evidencia real, no con fuego de efectos.|Bloqueado para imagen final hasta foto real de cocina y permiso.
C045|Un plato explicado por sus componentes auténticos.|tecnica|O3|O2|S6|lso||guardados|2|U|El Lomo Saltado Origen anotado en el diseño —salteado al wok, papas amarillas crocantes, arroz con choclo— sin desarmarlo en cocina.|
C046|La primera impresión al entrar, con fotos verificadas.|recorrido|O4|O1|S0||LOC;NUEVA|alcance|3|H|La primera impresión al entrar, contada solo con fotos verificadas: madera oscura, bronce y mantel claro.|Falta foto de la entrada (NUEVA).
C047|La ruta real desde la entrada a una mesa.|recorrido|O4|O6|S0||LOC;NUEVA|deslizamientos|3|H;V|De la puerta a la mesa en pasos fotografiados: ningún pasillo ni vista que no exista.|Falta foto del recorrido (NUEVA).
C048|La luz diurna sobre una mesa concreta.|macro|O4|O1|S0||MESA|guardados|2|H|La luz de mediodía sobre una misma mesa: cómo cambian el cristal, el mantel y la sombra durante el servicio.|Sesión con tres horas fijas dentro del horario.
C049|Cinco detalles reales del interior de ORIGEN.|album|O4|O1|S0||LOC;MESA|guardados|2|H|Cinco detalles verificados del interior —bronce de las lámparas, terciopelo, fotos en blanco y negro, orquídea y cristal— uno por slide.|Todos observados en LOC-01, LOC-02 y MESA-01.
C050|Una misma mesa desde tres encuadres.|macro|O4|O1|S0||MESA|guardados|2|H|Una misma mesa desde tres alturas: cenital, a la altura del comensal y desde el pasillo.|
C051|Plato protagonista, espacio coprotagonista.|escenas|O4|O2|S0|pul;lso;cvo|LOC;MESA|alcance|3|H|El plato ocupa un tercio del encuadre y el salón respira alrededor: comida y espacio en la misma foto.|
C052|Los colores reales del salón y la carta.|album|O4|O1|S0||LOC;MESA;MARCA|guardados|2|H|Taupe, oliva, ocre y café de la carta conversan con la madera, el bronce y el terciopelo del salón.|Colores de carta observados; no reemplazan una guía de marca aprobada.
C053|Qué ve realmente un comensal sentado.|pov|O4|O6|S0||MESA|alcance|2|H;V|Lo que realmente ve un comensal sentado: altura de ojos, copas en primer plano y el salón detrás, sin lentes que deformen.|
C054|La pausa visual entre plato y plato.|escenas|O4|O2|S3|croq|MESA|alcance|3|H|La pausa entre plato y plato: mesa a medio servir, servilletas usadas y una luz que ya se movió.|
C055|Un rincón real, tres maneras de fotografiarlo.|macro|O4|O1|S0||LOC|guardados|2|H|Un rincón verificado —la orquídea blanca en maceta de bronce sobre el mueble de madera— en plano, detalle y contexto.|Rincón observado en LOC-01 y LOC-02.
C056|La vajilla como parte de la identidad visual.|album|O4|O3|S0||MESA|guardados|2|H|La vajilla como identidad: el borde del plato, el peso del vaso y el doblez de la servilleta, tal como están en la mesa.|MESA-01 y MESA-02 muestran vajillas distintas: confirmar cuál es de ORIGEN.
C057|Luz de almuerzo: sombra, mesa, textura.|macro|O4|O1|S0||MESA|guardados|2|H|Luz de almuerzo en tres fotografías sin filtros que alteren el blanco del mantel.|
C058|Un álbum de detalles del servicio diurno.|album|O4|O1|S0||EQ;MESA|alcance|3|H|Bandejas, copas que se ordenan y el equipo de espaldas: un álbum del servicio de día, con autorización.|LOC-02 muestra personal: no publicar sin permiso.
C059|La perspectiva desde la mesa compartida.|pov|O4|O5|S3;S4|croq;lso|MESA;PER|compartidos|3|H;K|La perspectiva desde la mesa compartida: platos que se cruzan, brazos que alcanzan, nadie posando.|
C060|Un recorrido fotográfico honesto por ORIGEN.|recorrido|O4|O1|S0||LOC;MESA;NUEVA|alcance|3|H|Lo que hay, como se ve a mediodía, sin vistas inventadas ni grandes angulares exagerados.|
C061|Entrada y fondo que dialogan por sabor, sin imponer maridaje.|ruta|O3|O2|S3|cpo;lso;ldt;jcl;croq;fpl||guardados|3|U|Entradas y fondos que dialogan —ácido con frito, cremoso con salteado— propuestos como ideas, no como reglas.|Sin maridaje de bebidas. Validar con cocina.
C062|Un plato conocido abre la puerta a otro menos pedido.|ruta|O3|O6|S0|lso;rhl;cev;cnk||guardados|2|U;V|Si siempre pides Lomo Saltado Origen, la carta tiene un plato que lo lleva a otro lugar: el Risotto Huancaíno con Lomo Saltado.|'Menos pedido' solo con dato de ventas; si no, decir 'menos conocido'.
C063|Dos formas de empezar, dos de continuar.|ruta|O3|O5|S3|cpo;ldt;lso;ajs||comentarios|2|U;K|Dos formas de empezar y dos de continuar: cuatro combinaciones, una por slide, para decidir en pareja.|
C064|Menú de quienes aman lo crocante.|carta|O2|O3|S6|croq;teq;ebi;fpl;lso;acv||guardados|3|U;K|Quinua crocante, sábana de lomo crocante, papas crocantes: una palabra que se repite en la carta, convertida en menú.|
C065|De la costa al wok, con platos existentes.|ruta|O3|O2|S7|cev;chm;cha||guardados|2|U|De la costa al wok sin salir de la carta: ceviche para empezar y chaufa nikkei de mariscos para continuar.|
C066|Piqueos para tres tipos de mesa.|guia|O3|O5|S3;S4;S2|croq;teq;ali_a;spr;cpar|DATO|guardados|3|U;K|Piqueos para la mesa de dos, la de amigos y la familiar, con cantidades validadas con el equipo de salón.|Confirmar número de piezas por porción.
C067|De salado a dulce: la transición del almuerzo.|escenas|O2|O6|S8|lso;cvo|MESA;PER|guardados|3|H|De salado a dulce: el momento en que la mesa se despeja y llegan los postres.|
C068|Pedidos para quienes prefieren lo clásico.|guia|O3|O2|S4|scr;lso;jcl;cev;cvo||guardados|2|U|Para quien no quiere sorpresas: los clásicos limeños de la carta, presentados con el respeto que piden.|
C069|Opciones para explorar la propuesta nikkei.|guia|O3|O2|S7|cnk;cori;ebi;chm;acv;spk||guardados|3|U|Seis puertas a la propuesta nikkei, de la conchita con batayaqui al ceviche con palta flameada.|
C070|Del maki a un fondo: sabores que se conectan.|ruta|O3|O5|S7|hot;scr;acv;cnk;kat;lso||guardados|3|U|Del maki a un fondo: ingredientes que se repiten —ají panca, salsa acevichada, flameado— y conectan un pedido con el siguiente.|
C071|Una mesa con diferentes niveles de antojo.|ruta|O3|O5|S4|gar;cpk;lpi||comentarios|2|U;K|Una mesa, tres niveles de hambre: un plato ligero, uno intermedio y uno contundente que conviven sin problema.|
C072|Elige una base y dos acompañamientos reales.|ruta|O3|O5|S5;S6|amp;aml;amf;g_pur;g_ver||comentarios|2|U;K|Una base y dos acompañamientos: el carrusel como formulario para armar tu plato antes de llegar.|Solapa con L012: aquí se ilustra cada combinación con foto real.
C073|Piqueo más conversación: protagonismo compartido.|escenas|O5|O2|S3|spr;cho;cpar|MESA;PER|compartidos|3|H;K|El piqueo y la conversación comparten protagonismo: la mano que alcanza importa tanto como el plato.|
C074|La segunda visita: pide algo distinto.|guia|O3|O6|S0|pul;cha;ajs;cori||guardados|2|U;V|Si la primera vez pediste lo seguro, estas son las líneas de la carta que todavía no has abierto.|
C075|Combinaciones editoriales sujetas a validación culinaria.|carta|O3|O5|S3|croq;tir;rhl;tcm|DATO|guardados|2|U|Combinaciones propuestas por el equipo editorial y aprobadas —o corregidas— por la cocina antes de publicarse.|Requiere visto bueno de cocina.
C076|Un mini diccionario de la carta de ORIGEN.|diccionario|O3|O5|S7|tir;cori;acv;fuji;drag||guardados|3|U;K|Chalaquita, batayaqui, furai, tare, kawa karaage: un mini diccionario para leer la carta sin preguntar.|Definiciones validadas por cocina.
C077|Tradición limeña en preparaciones actuales.|escenas|O1|O3|S4|cpo;scr;cev;jcl;cvo||alcance|3|U|Platos que cualquier abuela limeña reconoce, servidos con la precisión de hoy.|Sin fechas ni orígenes históricos no citados.
C078|Lo criollo y lo nikkei, sin estereotipos.|ab|O3|O1|S7|cev;cnk;cpar;cori;lso;chc||comentarios|3|U;K|Lo criollo y lo nikkei, plato contra plato: la misma idea resuelta con dos acentos, sin caricaturas.|
C079|La historia detrás del nombre de un plato, solo si se verifica.|escenas|O1|O5|S0|cvo|DATO|compartidos|2|U;K|La historia detrás de un nombre, contada solo cuando el equipo la confirme: ¿quién es la abuela de la Crema Volteada?|Bloqueado hasta tener la historia verificada.
C080|Una palabra del menú y lo que significa.|diccionario|O3|O5|S7|tir;cho||guardados|2|U;K|Una sola palabra de la carta y todo lo que dice: 'chalaco', de la zarza chalaca al Tiradito Chalaco.|
C081|El arte del contraste: ácido, crocante, cremoso.|texturas|O2|O3|S0|cev;ebi;acm||alcance|2|U|Ácido, crocante, cremoso: tres sensaciones que la carta reparte entre entradas y fondos, una por slide.|
C082|Cinco ingredientes que aparecen en distintos platos.|carta|O3|O2|S7|cpo;cpar;acv;lso;cev||guardados|3|U|Palta, langostino, parmesano, ají amarillo y choclo: cinco ingredientes que cambian de papel en distintos platos.|
C083|Una lectura editorial de las guarniciones.|carta|O3|O2|S5|g_ens;g_pap;g_pur;g_arr;g_ver||guardados|2|U|Lo que acompaña también tiene textura, color y una razón de estar: las cinco guarniciones especiales.|
C084|De Huacho al Callao: nombres y referencias gastronómicas.|carta|O1|O3|S7|croq;cho;jcl;tir||compartidos|2|U;K|Los lugares que nombra la carta —Huacho, Callao, el muelle— y lo que cada nombre anticipa del plato.|Solapa con L006: aquí el eje es geografía, no piqueos.
C085|Qué hace diferente a dos versiones de una técnica.|ab|O3|O2|S7|jcl;jmx||comentarios|2|U;K|Jalea Clásica del Callao y Jalea Mixta de Mar Adentro, lado a lado: qué cambia cuando entran los mariscos.|
C086|La carta vista como mapa cultural.|carta|O1|O3|S0|cev;chp;fpl;cvo||guardados|2|U|Costa, wok, pasta y casa de la abuela: la carta leída como un mapa de influencias.|
C087|El lenguaje visual de las salsas reales.|macro|O2|O3|S7|pul;acv;fuji;cori||alcance|3|U|Color, viscosidad y brillo de las salsas reales, sin gotas dibujadas en postproducción.|
C088|Una preparación, tres planos narrativos.|macro|O2|O4|S7|cnk|LOC;MESA|alcance|2|H|Una preparación, tres planos: el detalle, el plato en la mesa y la mesa en el salón.|
C089|Contrastes de forma, color y textura de la carta.|texturas|O2|O1|S0|tir;pul;spk;cvo||alcance|2|U|Redondo y alargado, verde y ámbar, liso y crocante: contrastes que ya están en los platos.|
C090|ORIGEN en diez detalles comestibles y espaciales.|album|O1|O4|S0|croq;cpo;pul;lso;cvo|LOC;MESA|guardados|3|H|ORIGEN en diez detalles: cinco que se comen y cinco que se ven desde la mesa.|
C091|Arma tu mesa ideal: elige una opción por slide.|ruta|O5|O3|S0|croq;cev;lso;cvo||comentarios|2|U;K|Arma tu mesa eligiendo una opción por slide y comenta tu combinación final con cuatro letras.|
C092|¿Qué plato presentarías a alguien nuevo en ORIGEN?|preguntas|O5|O1|S0|lso;cca;pul;cnk;acm;cvo||comentarios|2|K|¿Qué plato pedirías para alguien que viene por primera vez? Seis candidatos, una sola respuesta.|
C093|Reto visual: adivina el plato por textura.|preguntas|O5|O2|S0|croq;cpar;acv;tcm||comentarios|3|K|Adivina el plato por su textura: un macro por slide y la respuesta al final, sin trucos de edición.|
C094|A o B: dos entradas, dos personalidades.|ab|O5|O3|S7|ldt;tir||comentarios|2|U;K|Leche de Tigre o Tiradito Chalaco: dos entradas frías, dos personalidades, una votación en comentarios.|
C095|Tu orden de postres, de primero a último.|preguntas|O5|O2|S8|cvo;tcm;chb;cny;hel;pie||comentarios|2|K|Ordena los seis postres del primero al último y cuéntanos tu ranking; no hay respuesta oficial.|
C096|Bingo de almuerzo en el club, sin atribuir hábitos reales.|preguntas|O5|O1|S0||MARCA|compartidos|2|K|Un bingo de mesa y carta con casillas genéricas, sin atribuir hábitos reales a los socios.|Pieza gráfica; foto de fondo de LOC/MESA.
C097|¿Con quién compartirías esta mesa?|preguntas|O5|O6|S3;S4|croq;lso|MESA|etiquetas|2|H;K|¿Con quién compartirías esta mesa? Un carrusel pensado para etiquetar a la persona correcta.|
C098|Elige una salsa y descubre el plato real.|preguntas|O5|O3|S7|pul;acv;fuji;cori||comentarios|2|U;K|Elige una salsa —anticuchera, acevichada, tare, batayaqui— y desliza para descubrir en qué plato vive.|
C099|Una encuesta visual para elegir makis.|ab|O5|O3|S7|acv;fuji;drag;salmo||comentarios|2|K|Una encuesta entre makis, dos por slide: la comunidad elige y el resultado real se publica después.|Resultados solo con datos reales.
C100|Completa la frase: «mi almuerzo empieza con…».|preguntas|O5|O1|S0|croq;ldt;cpo;spr||comentarios|1|K|'Mi almuerzo empieza con…': cuatro finales posibles y espacio para que el socio escriba el suyo.|
C101|Dos rutas de carta para dos estados de ánimo.|ruta|O3|O5|S3|gar;spk;lord;cny||guardados|2|U;K|Dos rutas de carta para dos ánimos: día de celebrar y día de cuidarse.|
C102|¿Cuál acercamiento revela más apetito?|preguntas|O5|O2|S0|lso||comentarios|2|K|El mismo plato en tres encuadres —cenital, 45° y a la altura de la mesa— y tú votas cuál abre más el apetito.|
C103|Adivina el postre antes del plano final.|preguntas|O5|O2|S8|tcm||comentarios|2|K|Textura, color, cuchara y, al final, el plato completo: adivina el postre antes del último slide.|
C104|Tu combinación del menú Ármalo a Tu Manera.|preguntas|O5|O3|S5;S6|arm;g_pur;g_arr;g_ver||comentarios|2|U;K|Tu combinación de Ármalo a Tu Manera en comentarios: proteína más dos acompañamientos.|Solapa con L012: aquí el eje es la respuesta de la comunidad.
C105|Las respuestas de la comunidad, solo con permiso y datos reales.|album|O5|O1|S0||UGC|compartidos|3|K|Las respuestas de la comunidad convertidas en carrusel, solo con permiso expreso y datos reales de la encuesta previa.|Bloqueado hasta tener respuestas reales y permisos.
C106|La luz de una semana de almuerzos.|album|O4|O1|S0||MESA|guardados|3|H|Una semana de almuerzos en la misma mesa: cómo cambia la luz de lunes a domingo, sin cambiar nada más.|
C107|Una guía de opciones para días de garúa.|guia|O3|O2|S0|sop;scr;min||guardados|2|U|Días de garúa, luz gris pero clara: las tres sopas de la carta para los mediodías de invierno.|Solapa con L011: invierno (jun–sep). Escena diurna obligatoria.
C108|Días soleados, platos frescos.|guia|O3|O2|S5|cev;tir;thai;gar;spk||guardados|2|U|Lo más fresco de la carta para el mediodía de verano en Chorrillos.|
C109|Un domingo para quedarse a sobremesa.|escenas|O4|O6|S4|cvo|LOC;MESA;PER|guardados|3|H;V|Almuerzo, postre y una sobremesa que no mira el reloj, dentro del horario de servicio.|Diferencia con C024: aquí se cierra con CTA de visita.
C110|Campaña de día familiar, previa validación comercial.|escenas|O6|O5|S2|kids|DATO|clics_contacto|3|V|Día familiar en ORIGEN: campaña que solo se activa si existe una propuesta comercial validada (fecha, condiciones, aforo).|Bloqueado hasta tener propuesta comercial aprobada.
C111|Una secuencia editorial para el próximo feriado.|guia|O6|O1|S0|lso;cev|DATO|clics_contacto|2|U;V|Qué pedir, con quién ir y a qué hora llegar en el próximo feriado, con horario confirmado.|Confirmar apertura y horario en feriado.
C112|Una carta para comenzar la temporada, sin oferta inventada.|carta|O3|O1|S0|ajs;min;pie||guardados|2|U|Para empezar la temporada: lo que conviene probar primero de la carta nueva, sin ofertas inventadas.|Depende de que Ají Salmón, Minestrone y Pie ya estén en servicio (D03).
C113|Semana de descubrimiento de platos de mar.|carta|O3|O2|S7|cho;tir;pem;jmx;acm||guardados|3|U|Cinco días, cinco líneas de mar de la carta, del chorito al arroz con mariscos.|
C114|Semana del arroz: distintos lenguajes de la carta.|carta|O3|O2|S6|acm;rhl;chp;g_arr;cha||guardados|3|U|Arroz con mariscos, risotto, chaufa, arroz con choclo y arroz al wok: uno por día.|Diferencia con C034: serie semanal, no carrusel único.
C115|Una estación, tres texturas del menú.|texturas|O2|O3|S0|ebi;acm;tir||alcance|2|U|Lo crocante, lo cremoso y lo fresco que mejor acompañan el mediodía de esta estación.|
C116|Especial editorial del almuerzo dominical.|escenas|O4|O6|S4|cev;lso;cvo|LOC;MESA;PER|guardados|4|H;V|Retrato de una mesa familiar de domingo de principio a fin, con autorización de quienes aparecen.|
C117|Campaña de postres de sobremesa.|album|O2|O6|S8|cvo;tcm;chb;cny;hel;pie|MESA|guardados|3|H;V|Un postre por semana, siempre con la mesa real de fondo y la cuchara en mano.|
C118|Un homenaje visual a la cocina peruana sin claims históricos falsos.|escenas|O1|O5|S0|cev;lso;cpo;scr||compartidos|3|U;K|Un homenaje a la cocina peruana desde la carta de ORIGEN, sin fechas ni orígenes que no podamos citar.|
C119|Regreso a ORIGEN: motivos gastronómicos para repetir.|guia|O6|O3|S0|pul;cha;ajs;cvo||guardados|2|U;V|Lo que la carta guarda para la segunda, tercera y cuarta visita.|
C120|Los mejores momentos diurnos del mes, con contenido producido.|album|O1|O5|S0||LOC;MESA;PER|compartidos|3|H;K|Los mejores momentos diurnos del mes, solo con fotos producidas en el mes y personas que autorizaron aparecer.|
P001|Lomo Saltado Origen: el plato y la mesa.|hero|O2|O6|S6|lso|LOC;MESA|guardados|2|H;V|El Lomo Saltado Origen en primer plano y el salón real detrás, sin agrandar la porción.|
P002|Causa de Camarones: precisión de emplatado.|hero|O2|O3|S7|cca|MESA|guardados|2||A 45°, con el espejo de reducción de camarones visible y nítido.|
P003|Pulpito Olio Anticuchero: textura auténtica.|hero|O2|O3|S7|pul|MESA|alcance|2||Bordes dorados reales, papas andinas y salsa anticuchera sin brillos agregados.|
P004|Risotto Huancaíno con Lomo Saltado: contraste de colores reales.|hero|O2|O3|S6|rhl|MESA|guardados|2||Amarillo de ají y café del lomo al wok: el contraste que el plato ya trae, sin saturación.|
P005|Ají Salmón: luz sobre el plato auténtico.|hero|O2|O3|S7|ajs|MESA|alcance|2||Luz de ventana sobre puré, tomates confitados y salmón al ajillo, con sombra física coherente.|Plato nuevo en carta sep 2026 (D03).
P006|Conchitas a la Parmesana: gratinado verdadero.|hero|O2|O3|S7|cpar|MESA|alcance|2||El dorado real del parmesano sobre las conchas de abanico, fotografiado recién salido.|
P007|Ebi Nikkei: crocante sin exageración.|hero|O2|O3|S7|ebi|MESA|alcance|2||Langostinos al panko con chutney de maracuyá y papas crocantes, tal cual se sirven.|
P008|Tiradito Chalaco: frescura real.|hero|O2|O3|S7|tir|MESA|guardados|2||Leche de tigre al ají amarillo y chalaquita, sin condensación falsa.|
P009|Fetuccini al Pesto con Lomo: perspectiva de mesa.|hero|O2|O6|S6|fpl|MESA|alcance|2|H|Visto desde la silla del comensal, con la sábana de lomo crocante a la vista.|
P010|Jalea Mixta de Mar Adentro: abundancia fiel.|hero|O2|O5|S7;S3|jmx|MESA|compartidos|2||La jalea con su yuca y su zarza, en la cantidad exacta que sale de cocina.|
P011|Croquetas de Huacho: macro documental.|macrop|O2|O3|S3|croq||alcance|2||Costra de quinua, interior de bechamel y la mayonesa de sauco al lado, en macro.|
P012|Burger Cheddar: apilado real y escala.|hero|O2|O3|S2;S6|bch|MESA|alcance|2||La Burger Cheddar en pan brioche junto a sus papas fritas, con una mano como referencia de escala.|
P013|Sake Poké Bowl: cenital de ingredientes auténticos.|hero|O2|O3|S5|spk|MESA|guardados|2|U|Cada ingrediente de la carta en su lugar: shari, palta, jengibre, zanahoria, kiuri y wantán.|
P014|Conchitas Oriental: plato de autor, sin inventos.|hero|O2|O3|S7|cori|MESA|alcance|2||Salsa batayaqui y parmesano con toque nikkei, sin guarniciones de autor inventadas.|
P015|Crema Volteada de la Abuela: caramelo y sobremesa.|hero|O2|O6|S8|cvo|MESA|guardados|2||El caramelo de la Crema Volteada en luz de sobremesa: brillo real, corte limpio, cuchara cerca.|
P016|Mesa lista para un almuerzo.|escena|O4|O6|S0||MESA|guardados|1|H;V|Copas, vasos, servilleta doblada y luz de mediodía antes del primer comensal.|MESA-01 ya muestra exactamente esta escena: candidato inmediato si se confirma el espacio.
P017|La luz real sobre el mantel.|negativo|O4|O1|S0||MESA|guardados|1|H|El borde de sombra que dibuja la ventana sobre el mantel, sin un solo objeto agregado.|
P018|Una silla esperando a alguien.|negativo|O4|O1|S0||LOC|alcance|1|H|Una silla de terciopelo burdeos sola en el encuadre: la pieza de mobiliario más reconocible del salón.|Sillas observadas en LOC-01.
P019|Perspectiva desde una mesa ocupada, autorizada.|humano|O4|O5|S3|lso|MESA;PER|alcance|2|H|Desde una mesa ocupada, con autorización de quienes aparecen o encuadre sin rostros.|
P020|Un rincón del salón con profundidad.|escena|O4|O1|S0||LOC|alcance|1|H|Primer plano de mesa, segundo plano de columnas de madera, fondo de ventanales.|
P021|El detalle material más propio de ORIGEN.|macrop|O4|O1|S0||LOC|guardados|1|H|La boiserie oscura y el bronce de las lámparas, de cerca.|
P022|Plato pequeño, espacio amplio y verdadero.|negativo|O4|O2|S0|cvo|LOC;MESA|alcance|2|H|Plato pequeño en el encuadre y salón real alrededor: la escala correcta del lugar.|
P023|Reflejo de mediodía en la vajilla.|macrop|O4|O1|S0||MESA|alcance|1|H|Un brillo físico sobre el borde del plato, sin destellos artificiales.|
P024|Una composición con dos mesas reales.|escena|O4|O1|S0||LOC|alcance|2|H|Dos mesas reales en una misma composición: la que está lista y la que acaba de vaciarse.|
P025|El camino visual hacia la mesa, si está fotografiado.|escena|O4|O6|S0||LOC;NUEVA|alcance|2|H;V|El camino hacia la mesa, solo si ese recorrido está fotografiado y autorizado.|
P026|El color del salón en una sola foto.|escena|O4|O1|S0||LOC|guardados|1|H|Madera, terciopelo burdeos, mantel claro y bronce en una sola fotografía.|
P027|Texturas honestas de mantel, madera y cristal.|macrop|O4|O1|S0||MESA|guardados|1|H|Mantel, madera y cristal en un encuadre cerrado, con grano fino y foco natural.|
P028|Un ángulo real desde el asiento del comensal.|negativo|O4|O6|S0||MESA|alcance|1|H;V|Lo que se ve con el codo apoyado en la mesa.|
P029|La pausa del espacio antes del servicio.|escena|O4|O1|S0||LOC;DATO|alcance|1|H|El salón en silencio minutos antes de abrir, sin gente y sin efectos.|Hora de apertura por confirmar (D09).
P030|Postal diurna del restaurante, sin vistas inventadas.|escena|O4|O1|S0||LOC|alcance|2|H|Un plano general honesto, sin vistas al mar inventadas ni cielos reemplazados.|
P031|Mano real que sirve un plato.|humano|O4|O2|S0|lso|EQ;MESA|alcance|2|H|Mano del equipo sirviendo: uniforme, gesto y vajilla verdaderos, rostro fuera de cuadro.|
P032|El gesto de acercar una silla, si se produce realmente.|humano|O4|O1|S0||EQ;LOC|alcance|2|H|El gesto de acercar una silla, publicado solo si ocurre en servicio y se fotografía con permiso.|
P033|Dos manos compartiendo un piqueo.|humano|O5|O2|S3|teq|MESA;PER|compartidos|2|H;K|La Trilogía de Tequeños al centro y dos manos que alcanzan, nadie posando.|
P034|Una servilleta desplegada sobre mesa real.|humano|O4|O1|S0||MESA;PER|alcance|1|H|Una servilleta que se despliega: el primer gesto del almuerzo.|
P035|La llegada auténtica del primer plato.|humano|O4|O2|S0|croq|EQ;MESA|alcance|2|H|Bandeja, mano y mesa en un solo instante: la llegada del primer plato.|
P036|El instante de apoyar la vajilla.|humano|O4|O2|S0|cpo|EQ;MESA|alcance|2|H|El plato a dos centímetros del mantel.|
P037|Un pedido compartido visto desde arriba.|humano|O5|O2|S3;S4|croq;cpar;cho|MESA;PER|guardados|2|H;K|Platos, manos y cubiertos en orden natural, vistos desde arriba.|
P038|El oficio de acomodar una mesa.|oficio|O4|O1|S0||EQ;MESA|alcance|2|H|Alinear cubiertos, girar la copa, doblar la servilleta.|
P039|Una cuchara entrando en un postre.|humano|O2|O6|S8|chb|MESA;PER|guardados|2|H|Una cuchara entrando en el Cheesecake del Bosque, justo antes de que se rompa la forma.|
P040|El cruce natural de cubiertos y conversación.|humano|O5|O4|S3|fpl;cev|MESA;PER|alcance|2|H|Cubiertos que se cruzan mientras la conversación sigue: dos platos, dos manos, una mesa.|
P041|Un gesto de atención del equipo, con autorización.|oficio|O4|O1|S0||EQ|alcance|2|H|Un gesto de atención del equipo, con nombre y autorización, o anónimo si así lo prefieren.|
P042|Dos personas que eligen su almuerzo, sin rostros inventados.|humano|O3|O5|S3||MESA;PER;DATO|comentarios|2|H;K|La carta en manos, rostros fuera de cuadro: dos personas eligen su almuerzo.|Confirmar formato de carta física.
P043|La última porción compartida.|humano|O5|O2|S3|ebi|MESA;PER|compartidos|2|H;K|El tenedor que duda y la mano que ofrece la última porción.|
P044|Manos reales, proporciones y piel realistas.|humano|O4|O1|S0|spk|PER|alcance|2|H|Manos reales —piel, uñas, proporción— como prueba de que la imagen no es generada.|
P045|El momento después de servir, antes del primer bocado.|negativo|O2|O4|S0|lso;cpo|MESA|alcance|1|H|Todo quieto, todo listo: el segundo después de servir.|
P046|Torta de Chocomanjar junto a una mesa luminosa.|hero|O2|O6|S8|tcm|LOC;MESA|guardados|2|H|Capas visibles de la torta y el salón suavemente desenfocado detrás.|
P047|Cheesecake del Bosque: textura fiel.|hero|O2|O3|S8|chb|MESA|guardados|2||La cobertura tal como se sirve, sin frutas agregadas.|
P048|Cheesecake New York & Chocolate: detalle real.|macrop|O2|O3|S8|cny||alcance|2||El corte, la base y el chocolate, sin derretidos artificiales.|
P049|Pie de Manzana: postre y cucharita.|hero|O2|O3|S8|pie|MESA;DATO|guardados|2||Masa, relleno y la opción que realmente se sirve, confirmada con cocina.|Discrepancia D06.
P050|Copa de Helados Artesanales: composición sin fusión artificial.|hero|O2|O3|S2;S8|hel|MESA;DATO|alcance|2||Fotografiada en el primer minuto, con la condensación que realmente aparece.|Discrepancia D06.
P051|Crema Volteada: encuadre editorial centrado.|negativo|O2|O1|S8|cvo||guardados|1||Encuadre simétrico: caramelo y plato, nada más.|Diferencia con P015: composición gráfica, no escena.
P052|La cuchara justo antes del bocado.|humano|O2|O6|S8|tcm|PER|guardados|2|H|El postre aún intacto y la intención en la mano.|
P053|Por qué reservar espacio para el postre.|tipo|O2|O6|S8|cvo;tcm;chb;cny;hel;pie|MESA|guardados|2|U;V|Una línea de texto sobre una foto real de los seis postres de la carta.|
P054|Manos y postre en luz de tarde diurna.|humano|O2|O4|S8|cny|PER;MESA|guardados|2|H|Sombra suave, piel natural y la cuchara de la casa, a primeras horas de la tarde.|
P055|Una mesa de sobremesa que parece vivida.|sobremesa|O4|O5|S8||MESA|guardados|1|H|Vasos a medio terminar, servilletas sueltas, sin desorden escenografiado.|No agregar tazas de café si no se sirven.
P056|Dos postres reales dentro de un mismo lienzo.|diptico|O2|O3|S8|tcm;cvo||comentarios|2|K|Torta de Chocomanjar y Crema Volteada lado a lado.|
P057|El último detalle dulce del almuerzo.|sobremesa|O2|O4|S8|cvo|MESA|alcance|1|H|Un borde de caramelo en el plato casi vacío.|
P058|Un postre con arquitectura real de fondo.|hero|O4|O2|S8|chb|LOC|alcance|2|H|Boiserie, bronce y la porción en primer plano.|
P059|La textura frente a la porción completa.|diptico|O2|O3|S8|pie||guardados|2|U|Díptico: macro del Pie de Manzana y la porción entera.|
P060|Un titular mínimo: «Nos quedamos un rato más».|tipo|O4|O6|S8||MESA|guardados|1|H;V|'Nos quedamos un rato más' sobre una sobremesa real.|
P061|El ají amarillo en una preparación real.|macrop|O3|O2|S7|cpo||guardados|1|U|La crema de ají amarillo bajo la Causa de pollo, en macro y luz lateral.|
P062|Un contraste de crocancia auténtica.|diptico|O2|O3|S6|croq;ebi||alcance|2||La quinua de la croqueta junto al panko del Ebi Nikkei.|
P063|Un arroz con textura visible y fiel.|macrop|O2|O3|S7|acm||alcance|1||El Arroz con Mariscos cremoso, con el parmesano tal como se sirve.|
P064|El detalle de la salsa anticuchera real.|macrop|O2|O3|S7|pul||alcance|1||Color, brillo contenido y el borde del pulpo entrando al encuadre.|
P065|El punto de gratinado de una conchita.|macrop|O2|O3|S7|cpar||alcance|1||Macro del parmesano dorado sobre la concha de abanico.|
P066|Un elemento característico de un maki existente.|macrop|O2|O3|S7|acv||alcance|1||Los hilos de camote crocante del maki ACV, en macro.|
P067|Una guarnición como textura protagonista.|macrop|O3|O2|S5|g_pur||alcance|1|U|El Puré de Papa Amarilla con su textura real.|
P068|Corte real de un plato, si la cocina lo autoriza.|oficio|O2|O3|S7|cca|COC|guardados|2|H|La Causa de Camarones cortada al medio en cocina, solo con autorización.|
P069|Tres ingredientes auténticos, un cuadro editorial.|bodegon|O3|O1|S7|cpo|COC;DATO|guardados|2|U|Tres insumos que la cocina confirme que usa en la causa, en un bodegón diurno.|
P070|El brillo físico y moderado de una salsa.|macrop|O2|O3|S7|acv||alcance|1||La salsa acevichada del maki ACV, sin gotas pintadas.|
P071|El contraste entre un fondo y su acompañamiento.|diptico|O3|O2|S5|aml;g_ver||guardados|2|U|Lomo al grill y Verduras al Vapor con Aceite de Oliva en el mismo lienzo.|
P072|Una capa verdadera de una causa.|macrop|O2|O3|S7|cpo|MESA|alcance|1||El corte lateral en mesa, con el tenedor, que muestra masa, relleno y palta.|Diferencia con P068: corte en mesa, no en cocina.
P073|El crocante de un piqueo recién servido.|macrop|O2|O3|S3|teq|MESA|alcance|1||Los tequeños en los primeros segundos sobre la mesa.|
P074|Un plano abierto que dé escala al detalle.|negativo|O4|O2|S0|croq|MESA;LOC|alcance|1|H|El plato pequeño sobre la mesa completa.|
P075|La huella de la cocina en la presentación real.|macrop|O2|O4|S0|aml|COC|alcance|2||Marcas de grill, bordes dorados y gotas que quedaron, sin limpiar en postproducción.|
P076|«Nos vemos para almorzar».|tipo|O6|O5|S0||MESA|compartidos|1|H;K;V|Tres palabras sobre la mesa real lista, para enviar a quien corresponde.|
P077|Una mesa de domingo, sin escena ficticia.|escena|O4|O6|S4|cev;lso|MESA;PER|guardados|2|H|Una mesa de domingo fotografiada un domingo real, con quienes autorizaron estar.|
P078|Dos platos, dos formas de disfrutar.|dosplatos|O3|O5|S3|cev;lso||comentarios|2|U;K|El Ceviche Clásico y el Lomo Saltado Origen en el mismo lienzo.|
P079|La conversación también es parte del almuerzo.|humano|O4|O5|S3||MESA;PER|alcance|2|H|Manos y vasos mientras alguien cuenta algo.|
P080|Un encuentro familiar en un plano discreto.|humano|O4|O5|S2;S4|kids;lso|MESA;PER|compartidos|2|H;K|Espaldas, manos y platos, sin rostros identificables.|Menores sin rostro.
P081|El gusto de detener el ritmo a mediodía.|negativo|O4|O1|S1|cae|MESA|alcance|1|H|Una mesa individual con luz lateral y nada que apure.|
P082|Compartir algo antes de pedir el fondo.|humano|O5|O3|S3|spr|MESA;PER|compartidos|2|H;K|El piqueo al centro y la carta todavía abierta.|
P083|Una visita que se vuelve sobremesa.|sobremesa|O4|O6|S4||MESA|guardados|1|H|La mesa después del fondo, sin desorden fabricado.|
P084|El placer de pedir el favorito habitual.|hero|O2|O5|S0|lso|MESA;DATO|comentarios|2|K|El plato que el equipo confirme como clásico de la casa, sin fingir rankings.|Requiere dato de ventas o criterio del equipo.
P085|La invitación a descubrir algo distinto.|hero|O3|O2|S7|cha|MESA|guardados|2|U|El Chanchito Oriental con Arroz al Wok, cocido por ocho horas según la carta.|
P086|«La mesa ya está lista».|tipo|O6|O4|S0||MESA|guardados|1|H;V|Un post de bienvenida sobre la mesa real puesta.|
P087|Una comida entre actividades, sin mostrar actividades no verificadas.|negativo|O3|O6|S1|cpk|MESA|alcance|1|H|Una comida entre actividades del club contada solo desde la mesa: el plato completo y una tarde implícita en el texto.|
P088|El lujo cotidiano de un buen almuerzo.|escena|O4|O2|S0|lpi|LOC;MESA|alcance|2|H|Mantel, cristal y un plato bien servido, sin ostentación.|
P089|Un momento de club que sí pueda documentarse.|escena|O1|O5|S0||PER;DATO|compartidos|3|H;K|Un evento o domingo real del club, fotografiado ese día y con permisos.|
P090|«Aquí empieza la sobremesa».|tipo|O4|O6|S8|cvo|MESA|guardados|1|H|'Aquí empieza la sobremesa' sobre la mesa después del postre.|
P091|¿Cuál elegirías hoy? Una foto con dos platos.|dosplatos|O5|O3|S7|pul;tir||comentarios|2|K|Pulpito Olio Anticuchero o Tiradito Chalaco, en una sola foto.|
P092|El nombre de un plato como titular editorial.|tipo|O1|O2|S4|scr||alcance|1||'Sopa Criolla del Recuerdo' como titular sobre su foto real.|
P093|Tres palabras que describen una textura real.|tipo|O2|O5|S7|pul||alcance|1|K|'Dorado, tierno, anticuchero' sobre el pulpo.|
P094|Un «dato de la carta» verificado sobre el plato.|tipo|O3|O2|S6|cha||guardados|1|U|'Cocido por ocho horas': el único dato de proceso que la carta declara, sobre el Chanchito Oriental.|
P095|Pregunta breve: ¿entrada o postre primero?|diptico|O5|O1|S0|cpo;cvo||comentarios|1|K|¿Entrada o postre primero? Una pregunta breve sobre un díptico real.|
P096|Una palabra protagonista: «Sobremesa».|tipo|O1|O4|S8||MESA|guardados|1|H|'Sobremesa' con mucho aire y una foto real pequeña.|
P097|Una fotografía, dos caminos de menú.|diptico|O3|O5|S5;S6|gar;lord||comentarios|2|U;K|La misma mesa leída como ruta ligera o ruta contundente.|
P098|Adivina el plato por un detalle real.|macrop|O5|O2|S7|ebi||comentarios|1|K|Macro del chutney de maracuyá: ¿de qué plato es?|
P099|Tipografía pequeña, fotografía con aire.|negativo|O1|O2|S0|cev||alcance|1||El plato ocupa un cuarto del lienzo y el texto es mínimo.|
P100|Portada de revista gastronómica, diseño original.|tipo|O1|O4|S0|rhl|MESA;MARCA|compartidos|2|K|ORIGEN como cabecera de una portada original, con una foto real como portada.|No imitar cabeceras de revistas existentes.
P101|Un díptico diurno dentro de un posteo.|diptico|O4|O1|S0||MESA|guardados|1|H|La mesa a las 12:00 y la misma mesa al final del servicio.|
P102|Un encuadre casi vacío que sugiera compañía.|negativo|O4|O5|S3||MESA|alcance|1|H|Dos copas y una silla corrida, sin personas.|
P103|Un favorito de la carta, sin fingir rankings de venta.|hero|O2|O5|S0|cnk|DATO|comentarios|2|K|'El que más recomendamos' solo si el equipo lo respalda.|
P104|«¿Lo compartirías?» sobre fotografía autorizada.|tipo|O5|O2|S3|jmx||compartidos|1|K|'¿Lo compartirías?' sobre la Jalea Mixta de Mar Adentro.|
P105|Un titular que deje espacio a la imagen.|tipo|O2|O1|S7|cca||alcance|1||Cinco palabras como máximo sobre la Causa de Camarones.|
P106|Invitación al almuerzo sin oferta inventada.|campana|O6|O4|S0||MESA;DATO|clics_contacto|1|H;V|Mesa real, horario confirmado y nada más.|Horario D09.
P107|Destacar un fondo de carta para descubrirlo.|hero|O3|O6|S6|lpi|MESA|guardados|2|V|El Lomo a la Pimienta y Risotto Mediterráneo, con su risotto de queso y azafrán.|
P108|Post de reserva con canal validado.|campana|O6|O4|S0||MESA;DATO|clics_contacto|1|V|El canal que el restaurante confirme (la web del club publica el 922 863 592) y el horario oficial vigente.|Confirmar si el número atiende WhatsApp.
P109|Presentar menú kids sin prometer condiciones no confirmadas.|campana|O6|O3|S2|kids|MESA;DATO|clics_contacto|2|U;V|Menú Kids tal como está en la carta vigente: S/25, hasta 10 años, cuatro alternativas.|D05: la carta pública aún muestra la versión anterior.
P110|Hoy puede ser día de una entrada distinta.|hero|O3|O6|S7|cori|MESA|guardados|2|V|Las Conchitas Oriental, para quien siempre pide la parmesana.|
P111|Un almuerzo de fin de semana en una sola escena.|escena|O6|O4|S4|cev;lso;cvo|LOC;MESA;PER|guardados|2|H;V|Mesa, platos, manos y luz de primeras horas de la tarde.|
P112|La experiencia completa resumida en una foto.|escena|O6|O3|S0|cpo;lso;cvo|LOC;MESA|guardados|2|H;V|Entrada, fondo y postre en la misma mesa, con el salón detrás.|
P113|Post temático de cocina de mar.|hero|O3|O2|S7|cmx|MESA|guardados|2|U|Ceviche Mixto en primer plano y la línea de mar resumida en el caption.|
P114|Post temático de la propuesta nikkei.|hero|O3|O2|S7|cnk|MESA|guardados|2|U|El Ceviche Nikkei con su palta flameada y nori, con titular mínimo.|
P115|Post temático de clásicos criollos.|hero|O3|O2|S4|scr|MESA|guardados|2|U|La Sopa Criolla del Recuerdo como portada del lado más casero de la carta.|
P116|El plato menos comunicado merece su portada.|hero|O3|O2|S0|min|DATO|guardados|2|U|El plato que el registro de publicaciones muestre como menos comunicado; candidato provisional: Minestrone Ítalo-peruano.|Basado en el banco legacy, no en ventas.
P117|Un cierre mensual con foto auténtica.|escena|O1|O5|S0||LOC;MESA|compartidos|1|H;K|La mejor imagen producida en el mes y un agradecimiento sin cifras inventadas.|
P118|Una invitación a repetir la visita.|campana|O6|O3|S0|pul|MESA|guardados|1|V|'La próxima vez, pide…' sobre un plato que no salió en publicaciones anteriores.|
P119|La promesa de marca apoyada en hechos observables.|tipo|O1|O4|S0||MESA|compartidos|1|H|La frase de bienvenida de la carta sobre una mesa real puesta.|Texto verificado en la carta.
P120|Una campaña visual de almuerzo diurno para ORIGEN.|campana|O6|O1|S0|lso|LOC;MESA|alcance|3|H;V|La pieza madre del sistema: día, mesa real y plato real en una sola imagen.|
"""
