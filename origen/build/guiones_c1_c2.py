# Guiones de carrusel C003–C030 (C001 y C002 tienen ficha completa en datos_fichas.py).
#
# Formato:
#   @ID                       inicia una pieza
#   S|toma[@anclas]|platos|acción (EN)|titular|subtítulo
#   CAP|caption (\n = salto de línea)
#
# Toma: E mesa a la altura del comensal · T cenital · F 45° plato · M macro · H manos (consentimiento)
#       S gesto de servicio (equipo, autorización) · W plano amplio de salón · D detalle de material
#       G fondo calmo para slide tipográfico · X díptico · N espacio negativo · K cocina (autorización)
# Anclas por defecto: LOC-01 + MESA-01 (provisionales). Se cambian con @LOC-02, @LOC-03+MESA-02, etc.
# "=" en titular → nombre del plato; "=" en subtítulo → descripción literal de la carta del primer plato.

GUIONES = r"""
@C003
S|E||Two covers set facing each other on the same table, nothing served yet, napkins folded.|Ligero o contundente|Dos caminos para el mismo mediodía
S|F|gar|The Garden salad on the near cover, fork resting on the side plate, untouched.|Camino ligero|=
S|F|thai|The Thai salad on the near cover, same position and angle as the previous slide.|Camino ligero|=
S|F|lpi|Lomo a la Pimienta y Risotto Mediterráneo on the far cover, seen across the table.|Camino contundente|=
S|F|rhl|Risotto Huancaíno con Lomo Saltado on the far cover, same framing as the previous slide.|Camino contundente|=
S|G||Calm, soft crop of the tablecloth between both covers.|¿Qué camino tomas hoy?|Guárdalo para decidir en la mesa
CAP|Dos caminos para el mismo mediodía.\n\nLigero: Ensalada Garden o Thai, para seguir la tarde con energía.\nContundente: Lomo a la Pimienta con Risotto Mediterráneo o Risotto Huancaíno con Lomo Saltado.\n\n¿Qué camino tomas hoy? Guárdalo para decidir en la mesa.

@C004
S|E||The table set for two at midday, nothing served, chairs slightly pulled out.|Una experiencia completa|De la entrada al postre, en la misma mesa
S|F|croq|Croquetas de Huacho placed in the center between both covers, just served.|1 · Para empezar|=
S|F|tir|Tiradito Chalaco on the near cover, spoon beside it.|2 · Algo fresco|=
S|F|fpl|Fetuccini al Pesto con Lomo in front of the far cover, seen across the table.|3 · El fondo|=
S|F|tcm|A slice of Torta de Chocomanjar on the near cover, dessert fork resting on the plate.|4 · El cierre|=
S|E|tcm|Same camera as slide 1 after lunch: napkins loosened, glasses partly full, dessert plate almost empty.|Cuatro tiempos, una mesa|Guárdalo para tu próximo almuerzo
CAP|De la entrada al postre, en cuatro tiempos:\n\nCroquetas de Huacho al centro para empezar.\nTiradito Chalaco, fresco.\nFetuccini al Pesto con Lomo de fondo.\nTorta de Chocomanjar para cerrar.\n\nUna misma mesa, sin apuro. Guárdalo para tu próximo almuerzo en ORIGEN.

@C005
S|X|ldt;sop|Diptych: Leche de Tigre on the left half, Sopita de Pollo on the right half, same table, height and light.|¿Tibio o fresco?|Dos maneras de empezar
S|F|ldt|Leche de Tigre on the near cover with its spoon, light passing through the liquid naturally.|Fresco|=
S|F|tir|Tiradito Chalaco on the near cover, same position as the previous slide.|Fresco|=
S|F|sop|Sopita de Pollo in its bowl on the near cover, spoon resting on the underplate.|Tibio|=
S|F|scr|Sopa Criolla del Recuerdo on the near cover, same framing as the previous slide.|Tibio|=
S|G||Calm crop of the table between two covers.|¿Con cuál empiezas?|Cuéntanos en comentarios
CAP|¿Tibio o fresco? Dos maneras de empezar el almuerzo.\n\nFresco: Leche de Tigre o Tiradito Chalaco.\nTibio: Sopita de Pollo o Sopa Criolla del Recuerdo.\n\n¿Con cuál empiezas tú?

@C006
S|T|croq;teq;cpar|Top-down of three sharing plates in the middle of a table for four, no hands.|Para compartir|Los piqueos de la carta, según cómo se comen
S|H|teq|A consenting hand takes one tequeño from the plate; face out of frame.|Con la mano|Trilogía de Tequeños · jamón y queso, queso o lomo saltado
S|H|ali_s|A hand lifts one wing from the plate; fries and blue cheese exactly as served.|Con la mano|Trilogía de Alitas · Spicy Origen, Blue BBQ o Acevichadas
S|F|croq;spr|Croquetas de Huacho and Spring Rolls Criollos side by side, small forks set beside the plates.|Con tenedor|Croquetas de Huacho · Spring Rolls Criollos
S|F|ebi|Ebi Nikkei plate with a fork resting on the side plate.|Con tenedor|=
S|T|cho;cpar;cori|Top-down of the three shell-served starters exactly as plated by ORIGEN.|En su concha|Choritos del Callao · Conchitas a la Parmesana · Conchitas Oriental
S|G||Calm crop of the empty center of the table.|¿Cuál pides al centro?|Guárdalo para tu próxima mesa
CAP|Ocho piqueos para compartir, ordenados por cómo se comen:\n\nCon la mano: Trilogía de Tequeños y Trilogía de Alitas.\nCon tenedor: Croquetas de Huacho, Spring Rolls Criollos y Ebi Nikkei.\nEn su concha: Choritos del Callao, Conchitas a la Parmesana y Conchitas Oriental.\n\n¿Cuál pides al centro? Guárdalo para tu próxima mesa.

@C007
S|G||Calm crop of the tablecloth and a clean cover.|El pescado del día|Tres formas reales de pedirlo
S|F|jcl|Jalea Clásica del Callao on the near cover, yuca and zarza exactly as served.|1 · Frito|=
S|F|pem|Pesca en el Muelle on the near cover, same framing as the previous slide.|2 · En salsa de mariscos|=
S|F|amf;g_arr;g_ver|Ármalo plate with pesca del día, arroz con choclo and verduras al vapor as plated by the kitchen.|3 · A tu manera|Pesca del día + dos acompañamientos a elección
S|T|jcl;pem;amf|Top-down of the three fish plates in a row on one table.|¿Frito, en salsa o a tu manera?|La especie depende de la pesca del día
CAP|El pescado del día, en tres formas reales:\n\nFrito, en la Jalea Clásica del Callao, con yuca y zarza.\nEn salsa de mariscos, en la Pesca en el Muelle, con yucas encurtidas.\nA tu manera, en Ármalo: pesca del día con dos acompañamientos.\n\n¿Cómo lo pides tú?

@C008
S|G||Calm crop of a set table.|¿Pasta, arroz o salteado?|Decide por antojo
S|T|fpl;fto;smc|Top-down of the three pastas in a row on the same table.|Si se te antoja pasta|Fetuccini al Pesto con Lomo · Fetuccini a la Toscana · Spaghetti a lo Macho
S|T|acm;chp|Top-down of Arroz con Mariscos and Chaufa Nikkei de Pollo side by side.|Si se te antoja arroz|Arroz con Mariscos · Chaufas Nikkei
S|F|lso|Lomo Saltado Origen on the near cover.|Si se te antoja salteado|=
S|F|rhl|Risotto Huancaíno con Lomo Saltado on the near cover.|O las dos cosas a la vez|=
S|G||Calm crop of the table after the plates were cleared.|¿Qué antojo tienes hoy?|Comenta: pasta, arroz o salteado
CAP|¿Pasta, arroz o salteado? Decide por antojo.\n\nPasta: Fetuccini al Pesto con Lomo, Fetuccini a la Toscana o Spaghetti a lo Macho.\nArroz: Arroz con Mariscos o un Chaufa Nikkei.\nSalteado: Lomo Saltado Origen.\nY si quieres las dos cosas: Risotto Huancaíno con Lomo Saltado.\n\n¿Qué antojo tienes hoy?

@C009
S|T|acv;fuji;drag|Top-down of three maki plates on the table, no hands.|Ocho makis|Cómo elegir según lo que dice la carta
S|F|acv;chili|Maki ACV and Maki Chili Spicy side by side, focus on the crispy camote threads.|Si buscas crocante|ACV y Chili Spicy · con hilos de camote
S|F|fuji|Maki Fuji on the near cover, focus on the quinoa pop.|Si buscas crocante|=
S|F|drag;salmo|Maki Dragon and Maki Salmo Limo side by side.|Si buscas cremoso|Dragon y Salmo Limo · con queso crema
S|F|kat;hot|Maki Katsuo Parrillero and Maki Hotate Smoked Panka side by side.|Flameado o ahumado|Katsuo Parrillero: pescado flambeado · Hotate Smoked Panka: ají panca
S|F|tuna|Maki Tuna Tartare on the near cover.|Donde la carta dice 'spicy'|Tuna Tartare: mayonesa spicy · Chili Spicy: tartar spicy
S|G||Calm crop of the table with only the real cutlery.|¿Cuál es el tuyo?|Guárdalo para tu próximo pedido
CAP|Ocho makis, elegidos por lo que realmente llevan:\n\nCrocante: ACV y Chili Spicy (hilos de camote), Fuji (quinoa pop).\nCremoso: Dragon y Salmo Limo (queso crema).\nFlameado o ahumado: Katsuo Parrillero y Hotate Smoked Panka.\nCon 'spicy' en la carta: Tuna Tartare y Chili Spicy.\n\n¿Cuál es el tuyo?

@C010
S|E||Table for four set, chairs pulled in, no food yet.|Del primer bocado al último|El orden en que se vive el almuerzo
S|H|croq|Two consenting hands reach toward Croquetas de Huacho placed in the center; faces out of frame.|Primero, al centro|=
S|H|cev|One hand holds a spoon over the Ceviche Clásico in front of a cover.|Luego, algo fresco|=
S|F|lso|Lomo Saltado Origen just placed in front of a cover, cutlery at rest.|El fondo llega|=
S|H|cvo|Two spoons approach one Crema Volteada placed between two covers.|El final se comparte|=
S|E||Same camera as slide 1 after lunch: napkins loosened, glasses partly full.|¿Tu mesa sigue este orden?|Cuéntanos cómo pides tú
CAP|Del primer bocado al último:\n\nAl centro, unas Croquetas de Huacho.\nAlgo fresco, un Ceviche Clásico.\nEl fondo, Lomo Saltado Origen.\nY una Crema Volteada para compartir.\n\n¿Tu mesa sigue este orden o empieza por el postre?

@C011
S|T|g_pur;g_arr;g_pap;g_ver|Top-down of the four Ármalo side dishes in their real vessels, arranged in a 2x2 grid.|Dos acompañamientos|Una decisión personal
S|F|aml;g_pur;g_ver|Ármalo plate: lomo al grill with puré de papas amarillas and verduras al vapor, as plated.|Puré + verduras|Lomo al grill con puré de papas amarillas y verduras al vapor
S|F|aml;g_arr;g_pap|Ármalo plate: lomo al grill with arroz con choclo and papas fritas, same framing.|Arroz + papas|Lomo al grill con arroz con choclo y papas fritas
S|F|amp;g_ver;g_arr|Ármalo plate: pollo a la plancha with verduras al vapor and arroz con choclo.|Verduras + arroz|Pollo a la plancha con verduras al vapor y arroz con choclo
S|G||Calm crop of the tablecloth.|¿Cuál es tu par?|Escríbelo: proteína + dos
CAP|Ármalo a Tu Manera: una proteína y dos acompañamientos.\n\nPuré de papas amarillas, arroz con choclo, papas fritas o verduras al vapor. Cada par cambia el plato.\n\n¿Cuál es tu par? Escríbelo en comentarios.

@C012
S|G||Calm crop of a set cover.|Para quien prefiere pollo|Ocho maneras en la carta
S|F|cpo|Causa de pollo on the near cover, its ají amarillo mirror visible.|Como entrada|=
S|T|cae;thai|Top-down of Ensalada Caesar's and Ensalada Thai side by side.|En ensalada|Caesar's: pollo a la plancha · Thai: pollo ahumado
S|F|cpk|Chicken Pop Poké Bowl on the near cover.|En bowl|=
S|T|chp;fto|Top-down of Chaufa Nikkei de Pollo and Fetuccini a la Toscana side by side.|De fondo|Chaufa Nikkei de Pollo · Fetuccini a la Toscana con pollito dorado
S|X|sop;amp|Diptych: Sopita de Pollo on the left, Ármalo pollo a la plancha on the right.|Lo más simple|Sopita de Pollo · Pollo a la plancha con dos acompañamientos
S|G||Calm crop of the table.|¿Cuál es tu pollo?|Guárdalo para quien siempre pide pollo
CAP|Para quien siempre pide "algo con pollo", la carta tiene ocho caminos:\n\nCausa de pollo · Caesar's · Thai · Chicken Pop Poké Bowl · Chaufa Nikkei de Pollo · Fetuccini a la Toscana · Sopita de Pollo · Pollo a la plancha en Ármalo.\n\nEtiqueta a quien lo necesita.

@C013
S|T|cho;cpar|Top-down of Choritos del Callao and Conchitas a la Parmesana on a table for two.|Mariscos de principio a fin|Entradas y fondos de la carta
S|F|cho|Choritos del Callao exactly as served.|Para empezar|=
S|F|cmx|Ceviche Mixto on the near cover.|Para empezar|=
S|T|acm;chm|Top-down of Arroz con Mariscos and Chaufa Nikkei de Mariscos.|De fondo, con arroz|Arroz con Mariscos · Chaufa Nikkei de Mariscos
S|F|jmx|Jalea Mixta de Mar Adentro on the center of the table.|De fondo, frito|=
S|T|smc;pem|Top-down of Spaghetti a lo Macho and Pesca en el Muelle.|De fondo, en salsa|Spaghetti a lo Macho · Pesca en el Muelle
S|G||Calm crop of the table.|Un almuerzo de mar completo|Guárdalo
CAP|Mariscos de principio a fin, según la carta:\n\nPara empezar: Choritos del Callao, Conchitas a la Parmesana, Ceviche Mixto.\nDe fondo: Arroz con Mariscos, Chaufa Nikkei de Mariscos, Jalea Mixta de Mar Adentro, Spaghetti a lo Macho, Pesca en el Muelle.\n\nGuárdalo para tu próximo almuerzo de mar.

@C014
S|T|cvo;tcm;chb;cny;hel;pie|Top-down of the six desserts on one table, spaced evenly, no hands.|Seis postres|Elige según el antojo del día
S|F|cvo|Crema Volteada de la Abuela with a spoon beside it.|Clásico de casa|=
S|X|tcm;cny|Diptych: Torta de Chocomanjar left, Cheesecake New York & Chocolate right.|Chocolate|Torta de Chocomanjar · Cheesecake New York & Chocolate
S|F|chb|Cheesecake del Bosque with a dessert fork resting.|Cheesecake|=
S|F|pie|Pie de Manzana with its spoon, served exactly as the kitchen confirms.|Horneado|=
S|F|hel|Copa de Helados Artesanales photographed within the first minute after serving.|Helado|=
S|G||Calm crop of a cleared table.|¿Cuál es el de hoy?|Guárdalo para la sobremesa
CAP|Seis postres para el antojo del día:\n\nClásico de casa: Crema Volteada de la Abuela.\nChocolate: Torta de Chocomanjar o Cheesecake New York & Chocolate.\nCheesecake: del Bosque.\nHorneado: Pie de Manzana.\nHelado: Copa de Helados Artesanales.\n\n¿Cuál es el de hoy?

@C015
S|G||Calm crop of a set table for two.|Tu almuerzo ideal|En cinco preguntas
S|X|croq;cev|Diptych: Croquetas de Huacho left, Ceviche Clásico right, same angle.|1 · ¿Compartes o cada uno lo suyo?|Al centro: Croquetas de Huacho · Para ti: Ceviche Clásico
S|X|lso;ajs|Diptych: Lomo Saltado Origen left, Ají Salmón right.|2 · ¿Tierra o mar?|Lomo Saltado Origen · Ají Salmón
S|F|lso|Lomo Saltado Origen on the near cover, full plate.|3 · ¿Vienes con hambre?|Un fondo completo: papas amarillas y arroz con choclo
S|E|croq|Table for four with one sharing plate in the center and hands out of frame.|4 · ¿Con quién vienes?|En grupo, empieza por un piqueo al centro
S|F|cvo|Crema Volteada de la Abuela with a spoon.|5 · ¿Hay espacio para postre?|=
CAP|Tu almuerzo ideal en cinco preguntas:\n\n¿Compartes o cada uno lo suyo? ¿Tierra o mar? ¿Vienes con hambre? ¿Con quién vienes? ¿Hay espacio para postre?\n\nResponde las cinco en comentarios y te decimos qué pedir.

@C016
S|E||Table for four set at midday, nobody seated yet.|Cinco momentos|De un almuerzo compartido
S|H|croq|Hands of different ages reach toward Croquetas de Huacho in the center; faces out of frame.|Uno · Alguien pide al centro|=
S|H||Two hands unfold white napkins over the laps, glasses being moved aside; no food.|Dos · La mesa se acomoda|
S|H|lso|A hand passes the Lomo Saltado Origen plate across the table to another hand.|Tres · Se prueba del plato del otro|=
S|H|cvo|Several spoons around one Crema Volteada.|Cuatro · El postre se comparte|=
S|E||The same table after lunch, chairs slightly turned toward each other, no faces.|Cinco · Nadie se levanta|Así se ve un almuerzo compartido
CAP|Cinco momentos que se repiten en cualquier almuerzo compartido:\n\nAlguien pide al centro. La mesa se acomoda. Se prueba del plato del otro. El postre se comparte. Y nadie se quiere levantar.\n\n¿Con quién vives estos cinco momentos?

@C017
S|E||A table set for four at 12:00, chairs empty and slightly pulled out, no people.|La mesa antes de que lleguen todos|
S|D||Close detail of one stemmed glass and one tumbler on the tablecloth, window light crossing them.|Las copas, en su sitio|
S|D||Close detail of a folded white napkin on the stoneware plate.|La servilleta, esperando|
S|W||Wide view of the room with the set table in the lower third and the brass chandeliers above.|El salón, en silencio|
S|E||Same frame as slide 1, one chair now turned as if someone just arrived; no person visible.|Ya llega alguien|Te esperamos para almorzar
CAP|Antes del primer saludo, la mesa ya está lista: copas en su sitio, servilletas dobladas y la luz de mediodía entrando por los ventanales.\n\nTe esperamos para almorzar en ORIGEN.

@C018
S|E||Table for six set at midday, nobody seated.|Un almuerzo entre generaciones|Cada uno pide lo suyo
S|H|cvo|An older consenting hand holds a dessert spoon next to Crema Volteada de la Abuela.|La abuela pide lo de siempre|=
S|H|lso|An adult hand cuts into Lomo Saltado Origen.|Los padres van por el fondo|=
S|H|kids|A child's hand (parental consent, no face) next to the Menú Kids plate.|Los chicos tienen su menú|Menú Kids · hasta 10 años
S|H|lso;cvo|Hands crossing over the table: someone tastes from another's plate.|Y todos prueban de todo|
S|E||The table after lunch, chairs turned toward each other, no faces.|Tres generaciones, una mesa|
CAP|Abuelos, padres y nietos en la misma mesa: cada uno pide lo suyo y todos terminan probando del plato del otro.\n\nLa Crema Volteada de la Abuela, el Lomo Saltado Origen y un Menú Kids para los más chicos.\n\n¿Quién es el que siempre prueba de todos los platos?

@C019
S|E||First-person view from a chair: the table edge, a set cover, the room ahead; no people.|POV|Llegas del club y te sientas
S|D||First-person view: a hand sets a phone face down beside the cover (no screen visible).|Dejas el teléfono a un lado|
S|F|cae|First-person view: Ensalada Caesar's placed in front of you.|Algo fresco para empezar|=
S|F|lso|First-person view: Lomo Saltado Origen arrives in front of you.|O directo al fondo|=
S|E||First-person view after lunch: plate finished, napkin on the table, the room calm.|La tarde sigue|Pero el almuerzo fue tuyo
CAP|POV: llegas del club con la tarde por delante y te sientas a la mesa.\n\nDejas el teléfono a un lado. Una Caesar's para empezar o un Lomo Saltado Origen directo. La tarde sigue, pero el almuerzo fue tuyo.

@C020
S|T|croq;cpar;ali_s;teq|Top-down of four sharing plates in the middle of a table for four, no hands.|Pedir al centro|cambia la conversación
S|H|croq|Two hands reach for Croquetas de Huacho at the same moment.|Alguien empieza|=
S|H|cpar|A hand takes one Conchita a la Parmesana by its shell.|Otro sigue|=
S|H|ali_s;teq|Several hands around the alitas and tequeños; faces out of frame.|Y la mesa conversa|Trilogía de Alitas · Trilogía de Tequeños
S|T|croq;cpar;ali_s;teq|Same top-down as slide 1, plates now half empty.|¿Qué pides al centro?|Etiqueta a tu mesa
CAP|Cuando los platos van al centro, la mesa conversa distinto.\n\nCroquetas de Huacho, Conchitas a la Parmesana, alitas y tequeños: nadie pide solo para sí.\n\nEtiqueta a quien siempre pide para todos.

@C021
S|H||Two pairs of hands hold the menu open over the table; faces out of frame.|El pequeño ritual|de elegir juntos
S|H||A finger points at a line of the menu while another hand rests on the table.|Alguien señala|
S|H||The menu passes from one hand to another across the table.|Pasa de mano en mano|
S|E||The menu closed on the table edge, napkins unfolded, waiting for the order.|Y se decide|
S|G||Calm crop of the table.|¿Quién decide en tu mesa?|Cuéntanos
CAP|La carta pasa de mano en mano, alguien señala, alguien duda, alguien decide por todos.\n\n¿Quién decide en tu mesa?

@C022
S|E||Table for four set for a family, nobody seated.|Una familia|cuatro pedidos distintos
S|F|kids|Menú Kids plate on a child's cover, exactly as served.|Para el más chico|Menú Kids · hasta 10 años
S|F|fpl|Fetuccini al Pesto con Lomo on another cover.|Para quien quiere pasta|=
S|F|cev|Ceviche Clásico on another cover.|Para quien quiere mar|=
S|F|cae|Ensalada Caesar's on the last cover.|Para quien quiere algo ligero|=
S|T|kids;fpl;cev;cae|Top-down of the four plates together on the same table.|Una sola mesa|Guárdalo para el próximo almuerzo familiar
CAP|Una familia, cuatro pedidos distintos y una sola mesa.\n\nMenú Kids para el más chico, Fetuccini al Pesto con Lomo, Ceviche Clásico y una Caesar's.\n\nGuárdalo para el próximo almuerzo en familia.

@C023
S|E||Table for two just after ordering, menus closed at the edge.|Mientras llega el primer plato|
S|H||Hands unfold a white napkin over a lap.|Las servilletas se despliegan|
S|H||A hand moves a glass of water closer; no pouring scene.|Los vasos se acomodan|
S|H||Two pairs of hands rest on the table mid-conversation, one gesturing.|La conversación arranca|
S|F|croq|The first plate arrives in the center of the table.|Y llega lo primero|=
CAP|Lo que pasa entre el pedido y el primer plato también es parte del almuerzo: servilletas que se despliegan, vasos que se acomodan, una conversación que arranca.\n\nY entonces llega lo primero.

@C024
S|E||Table for six on a Sunday at midday, set and empty.|Un domingo|que merece sobremesa
S|H|cvo|Hands around a Crema Volteada placed in the center.|El postre llega al centro|=
S|H|tcm|A fork lifts a bite of Torta de Chocomanjar.|Alguien pide otro|=
S|E||The table after dessert: glasses partly full, napkins loosened, chairs turned.|Y nadie se levanta|
S|G||Calm crop of the table.|Domingo en ORIGEN|Guárdalo para el próximo
CAP|Hay domingos que merecen sobremesa.\n\nEl postre al centro, alguien pide otro y nadie se quiere levantar.\n\nGuárdalo para el próximo domingo en ORIGEN.

@C025
S|T|croq;teq;ali_b;cho;cpar|Top-down of five sharing plates covering the center of a table for six.|«Probemos un poquito de todo»|
S|M|croq|Macro of the quinoa crust of a Croqueta de Huacho.|Croquetas de Huacho|
S|M|teq|Macro of a tequeño as served.|Tequeños|
S|M|ali_b|Macro of an Alita Blue BBQ as served.|Alitas Blue BBQ|
S|M|cho|Macro of a Chorito del Callao with its zarza chalaca.|Choritos del Callao|
S|M|cpar|Macro of the gratinated parmesan on a Conchita.|Conchitas a la Parmesana|
S|T|croq;teq;ali_b;cho;cpar|Same top-down as slide 1, plates nearly empty.|Lo probamos todo|Etiqueta a quien lo dijo primero
CAP|"Probemos un poquito de todo."\n\nCroquetas de Huacho, tequeños, alitas Blue BBQ, Choritos del Callao y Conchitas a la Parmesana.\n\nEtiqueta a quien siempre lo dice primero.

@C026
S|E||Table for six set at midday.|Una visita|tres generaciones, varios gustos
S|F|cpo|Causa de pollo on the grandparents' side of the table.|El clásico|=
S|F|mac|True Mac & Cheese on a child's cover.|El de los chicos|=
S|F|ajs|Ají Salmón on another cover.|El nuevo de la carta|=
S|H|cvo|Hands of different ages around Crema Volteada de la Abuela.|Y uno para todos|=
CAP|Una visita, tres generaciones y varios gustos.\n\nCausa de pollo para el clásico, True Mac & Cheese para los chicos, Ají Salmón para quien quiere algo nuevo y una Crema Volteada para todos.\n\n¿Cuál es el plato de cada generación en tu familia?

@C027
S|E||Table for four, two people arriving (only torsos and hands, consent).|Todo encuentro|empieza con un piqueo
S|H|spr|A hand takes a Spring Roll Criollo; the other diner's hand rests on the table.|Spring Rolls Criollos|=
S|H|ebi|Hands share Ebi Nikkei with forks.|Ebi Nikkei|=
S|H|cho|A hand holds a Chorito del Callao by its shell.|Choritos del Callao|=
S|G||Calm crop of the table with empty sharing plates.|¿Con qué empiezas tú?|
CAP|Todo encuentro empieza con un primer bocado: Spring Rolls Criollos, Ebi Nikkei o Choritos del Callao, antes de que alguien abra la carta.\n\n¿Con cuál empiezas tú?

@C028
S|S||A staff member (from the shoulders down, written consent) brings a chair closer to the table.|Pequeños gestos|de hospitalidad
S|S||A staff hand places a folded napkin on the cover.|Acercar|
S|S|lso|A staff hand sets Lomo Saltado Origen in front of a cover.|Servir|=
S|S||A staff hand removes an empty plate, the diner's hand still on the table.|Retirar|
S|G||Calm crop of the room.|Gestos reales del equipo|Fotografiados con su autorización
CAP|Acercar una silla, servir, retirar a tiempo: gestos pequeños que hacen el almuerzo.\n\nGracias al equipo de ORIGEN por dejarnos fotografiarlos.

@C029
S|E||Table for two mid-conversation, plates cleared, two hands gesturing.|De la conversación|al postre
S|F|tcm|Torta de Chocomanjar arrives in the center.|Llega el postre|=
S|F|cny|Cheesecake New York & Chocolate beside it.|Y otro más|=
S|H|cvo|Two spoons meet over a Crema Volteada.|Se comparte|=
S|E||Empty dessert plates, glasses partly full, nobody standing up.|Nadie quiere levantarse|
CAP|La conversación sigue y el postre llega.\n\nTorta de Chocomanjar, Cheesecake New York & Chocolate y una Crema Volteada para compartir. Nadie quiere levantarse.

@C030
S|E||Table for four set at midday, no clocks or phones anywhere.|La mesa que se disfruta|sin apuro
S|T|cpo;lso|Top-down of Causa de pollo and Lomo Saltado Origen on the same table.|Sin reloj a la vista|Causa de pollo · Lomo Saltado Origen
S|F|cpo|Causa de pollo at 45 degrees with a fork resting beside it, nobody hurrying.|La entrada, despacio|=
S|H|lso|A hand serves a portion of Lomo Saltado Origen onto a side plate for someone else.|Se comparte|
S|E||The table after lunch with early-afternoon light, chairs turned.|La tarde puede esperar|
CAP|Sin reloj a la vista: la mesa que se disfruta despacio, con luz de mediodía y platos que se comparten.\n\nLa tarde puede esperar.
"""
