# -*- coding: utf-8 -*-
# Genera moodboard.html (página con imágenes embebidas) y MOODBOARD.md (texto con enlaces).
import base64, io, json, os, sys
from html import escape as e
from PIL import Image

SP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(SP, "scripts"))
import content as c

W = os.path.join(SP, "work")
META = json.load(open(os.path.join(W, "pin", "selected_meta.json")))
N_PINS = len(c.PINS)


def pin_url(pid):
    return f"https://www.pinterest.com/pin/{pid}/"


def data_uri(path, width, crop=None, quality=74):
    im = Image.open(path).convert("RGB")
    if crop:
        im = im.crop(crop)
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode(), im.size


def pin_img(pid, width):
    return data_uri(os.path.join(W, "pin", "v", "img", f"{pid}.jpg"), width)


def frame_img(name, width=260):
    f = [x for x in os.listdir(os.path.join(W, "frames")) if x.startswith(name + "_")][0]
    return data_uri(os.path.join(W, "frames", f), width)


def pdf_img(name, width=360, crop=None):
    return data_uri(os.path.join(W, "pdf", name), width, crop)


def credit(pid):
    m = META[pid]
    who = m.get("author") or "desconocido"
    user = m.get("author_user")
    dom = m.get("domain")
    src = "subida por el usuario, sin enlace de origen" if (not dom or dom == "Uploaded by user") else dom
    return who, user, src, m.get("link"), m.get("img_dim"), m.get("headline") or m.get("title")


# ---------- HTML ----------
CSS = r"""
:root{
  /* Layout: sala de proyección. Barra de tiempo proporcional de 25 s arriba y fichas de escena debajo, como una mesa de montaje. */
  --bg:#F4ECE2; --surface:#FBF7F1; --raise:#FFFFFF; --ink:#2A1012; --muted:#6B5650; --line:#E2D4C4;
  --wine:#43080A; --gold:#8F6118; --gold-soft:#F1E2C6; --ok:#2F6B3A; --ok-soft:#E3EFE2; --warn:#8A4B06; --warn-soft:#F8E6CF; --no:#9B1C1C; --no-soft:#F6DCDA;
  --on-wine:#F4ECE2;
  --f-display:"Antonio","Oswald","Arial Narrow",sans-serif;
  --f-body:"Source Sans 3","Segoe UI",system-ui,sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#140A0B; --surface:#1E1112; --raise:#271617; --ink:#F1E7DA; --muted:#B9A595; --line:#3A2527;
  --wine:#5A1013; --gold:#D6A04A; --gold-soft:#3A2814; --ok:#8FCB97; --ok-soft:#1C2C1E; --warn:#F0B26A; --warn-soft:#33220F; --no:#F29A93; --no-soft:#3A1716;
  --on-wine:#F4ECE2; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#140A0B; --surface:#1E1112; --raise:#271617; --ink:#F1E7DA; --muted:#B9A595; --line:#3A2527;
  --wine:#5A1013; --gold:#D6A04A; --gold-soft:#3A2814; --ok:#8FCB97; --ok-soft:#1C2C1E; --warn:#F0B26A; --warn-soft:#33220F; --no:#F29A93; --no-soft:#3A1716;
  --on-wine:#F4ECE2; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:16px;line-height:1.55;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 64px}
.wrap{max-width:1240px;margin:0 auto}
a{color:var(--gold);text-underline-offset:2px}
a:focus-visible,button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
h1,h2,h3{font-family:var(--f-display);font-weight:700;letter-spacing:.01em;text-wrap:balance;margin:0;line-height:1.05;text-transform:uppercase}
h1{font-size:clamp(34px,6vw,64px)}
h2{font-size:clamp(28px,4vw,40px)}
h3{font-size:22px}
p{margin:0}
.mono{font-family:var(--f-mono);font-variant-numeric:tabular-nums}
.eyebrow{font-family:var(--f-mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.muted{color:var(--muted)}
.small{font-size:14px}
header.top{padding-block:40px 24px;display:grid;gap:16px;border-bottom:1px solid var(--line)}
header.top .row{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:baseline}
.logo-chip{display:inline-flex;align-items:center;gap:12px}
.logo-chip img{height:56px;width:auto;border-radius:4px}
nav.toc{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);border-bottom:1px solid var(--line);
  display:flex;gap:4px;overflow-x:auto;padding-block:10px;scrollbar-width:thin}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
nav.toc a{flex:0 0 auto;text-decoration:none;color:var(--ink);font-family:var(--f-mono);font-size:13px;padding:6px 10px;border-radius:6px;white-space:nowrap}
nav.toc a:hover{background:var(--surface)}
nav.toc a b{color:var(--gold);font-weight:600;margin-right:6px}
section.sec{padding-block:56px 8px;display:grid;gap:24px;scroll-margin-top:60px}
.sec-head{display:grid;gap:8px;max-width:820px}
.num{font-family:var(--f-mono);color:var(--gold);font-size:14px;letter-spacing:.08em}
.grid{display:grid;gap:16px}
.g2{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(240px,1fr))}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:20px;min-width:0;display:grid;gap:10px;align-content:start}
.panel h3{font-size:18px}
.kv{display:grid;grid-template-columns:minmax(110px,max-content) 1fr;gap:6px 16px;font-size:15px}
.kv dt{color:var(--muted);font-family:var(--f-mono);font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding-top:3px}
.kv dd{margin:0;min-width:0}
ul.clean{margin:0;padding-left:18px;display:grid;gap:6px}
.concept{background:var(--wine);color:var(--on-wine);border-radius:12px;padding:28px;display:grid;gap:10px}
.concept .eyebrow{color:var(--on-wine);opacity:.75}
.concept h2{font-size:clamp(32px,5vw,52px)}
.copyline{display:grid;gap:4px}
.copyline div{display:grid;grid-template-columns:44px 1fr;gap:8px;font-size:15px}
.copyline span.mono{color:var(--gold)}
.chip{display:inline-flex;align-items:center;gap:6px;font-family:var(--f-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:999px;white-space:nowrap}
.c-ok{background:var(--ok-soft);color:var(--ok)} .c-warn{background:var(--warn-soft);color:var(--warn)} .c-no{background:var(--no-soft);color:var(--no)}
.c-gold{background:var(--gold-soft);color:var(--gold)} .c-line{border:1px solid var(--line);color:var(--muted)}
.tablewrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:14px;min-width:720px}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:var(--f-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);background:var(--surface)}
tr:last-child td{border-bottom:0}
td.thumb{width:84px} td.thumb img{width:72px;border-radius:4px;display:block}
.frames{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px}
.frames figure{margin:0;flex:0 0 120px;display:grid;gap:4px}
.frames img{width:120px;border-radius:6px;display:block}
.frames figcaption{font-family:var(--f-mono);font-size:11px;color:var(--muted)}
.swatches{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px}
.sw{border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--surface)}
.sw div.c{height:72px}
.sw div.t{padding:10px 12px;display:grid;gap:2px;font-size:13px}
.pdfs{display:flex;gap:12px;overflow-x:auto;padding-bottom:6px}
.pdfs figure{margin:0;flex:0 0 190px;display:grid;gap:6px}
.pdfs img{width:190px;border-radius:6px;border:1px solid var(--line);display:block}
.pdfs figcaption{font-size:12px;color:var(--muted)}
.prod{display:grid;gap:8px}
.score{display:flex;gap:4px;flex-wrap:wrap}
.score span{font-family:var(--f-mono);font-size:11px;padding:2px 6px;border-radius:4px;background:var(--bg);border:1px solid var(--line)}
/* barra de tiempo proporcional */
.ruler{display:flex;gap:3px;width:100%;min-width:0}
.ruler a{display:grid;grid-template-rows:auto 1fr auto;gap:6px;text-decoration:none;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:8px;min-width:0;overflow:hidden}
.ruler a:hover{border-color:var(--gold)}
.ruler .tc{font-family:var(--f-mono);font-size:11px;color:var(--gold)}
.ruler .im{display:flex;gap:3px;min-height:0}
.ruler .im img{flex:1 1 0;min-width:0;height:120px;object-fit:cover;border-radius:4px}
.ruler .im .card7{flex:1;height:120px;border-radius:4px;background:var(--wine);color:var(--on-wine);display:grid;place-items:center;font-family:var(--f-display);font-size:18px;text-align:center;line-height:1}
.ruler .nm{font-size:12px;line-height:1.25;overflow:hidden;text-overflow:ellipsis}
.ticks{display:flex;justify-content:space-between;font-family:var(--f-mono);font-size:11px;color:var(--muted);padding-inline:2px}
@media (max-width:760px){.ruler{flex-direction:column}.ruler a{flex:none!important}.ruler .im img,.ruler .im .card7{height:90px}.ticks{display:none}}
.compare td:nth-child(3){color:var(--gold);font-weight:600}
/* fichas de escena */
.scene{border:1px solid var(--line);border-radius:14px;background:var(--surface);overflow:hidden;scroll-margin-top:60px}
.scene-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;padding:20px 24px;border-bottom:1px solid var(--line)}
.scene-head .tc{font-family:var(--f-mono);font-size:14px;color:var(--gold)}
.scene-head h3{font-size:28px}
.scene-body{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:24px;padding:24px}
@media (max-width:900px){.scene-body{grid-template-columns:1fr}}
.refs{display:grid;gap:16px;align-content:start}
.refs.two{grid-template-columns:1fr 1fr}
@media (max-width:520px){.refs.two{grid-template-columns:1fr}}
.ref{display:grid;gap:8px;align-content:start;min-width:0}
.ref img{width:100%;max-height:560px;object-fit:contain;background:var(--bg);border-radius:8px;display:block}
.ref .cap{display:grid;gap:4px;font-size:13px}
.ref .cap .id{font-family:var(--f-mono);font-size:11px;color:var(--muted);word-break:break-all}
.brandcard{aspect-ratio:9/16;max-width:320px;width:100%;background:var(--wine);color:var(--on-wine);border-radius:10px;display:grid;place-items:center;text-align:center;padding:24px}
.brandcard .in{display:grid;gap:14px;justify-items:center}
.brandcard .lg{border:2px solid var(--on-wine);padding:10px 14px;font-family:var(--f-display);font-size:40px;line-height:.95}
.brandcard .ct{font-family:var(--f-display);font-size:14px;letter-spacing:.3em}
.brandcard .cta{background:#B07A27;color:#F4ECE2;font-family:var(--f-mono);font-size:12px;padding:6px 10px;border-radius:4px}
.info{display:grid;gap:16px;align-content:start;min-width:0}
.block{display:grid;gap:6px}
.block .eyebrow{color:var(--gold)}
.ontext{font-family:var(--f-display);font-size:24px;line-height:1.1;text-transform:none;letter-spacing:.01em}
.prompt{display:grid;gap:8px;background:var(--raise);border:1px solid var(--line);border-radius:10px;padding:14px}
.prompt .ph{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap}
.prompt pre{margin:0;white-space:pre-wrap;word-break:break-word;font-family:var(--f-mono);font-size:12.5px;line-height:1.55;color:var(--ink)}
.prompt .neg{font-size:12px;color:var(--muted);font-family:var(--f-mono)}
button.copy{font-family:var(--f-mono);font-size:12px;background:var(--gold);color:var(--bg);border:0;border-radius:6px;padding:6px 10px;cursor:pointer}
button.copy:hover{filter:brightness(1.08)}
.altrow{display:flex;gap:10px;overflow-x:auto;padding:0 24px 24px}
.altrow figure{margin:0;flex:0 0 140px;display:grid;gap:4px;opacity:.85}
.altrow img{width:140px;height:180px;object-fit:cover;border-radius:6px;display:block}
.altrow figcaption{font-size:11px;font-family:var(--f-mono);color:var(--muted)}
.alts{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}
.alt{display:grid;gap:8px;background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px;min-width:0}
.alt img{width:100%;height:260px;object-fit:cover;border-radius:6px;display:block}
.alt .t{font-size:13px;display:grid;gap:4px}
.checks{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.vlist{display:grid;gap:8px}
.vlist div{display:grid;grid-template-columns:92px 1fr;gap:10px;align-items:start;font-size:15px}
.legend{display:flex;flex-wrap:wrap;gap:8px}
footer{margin-top:56px;padding-top:20px;border-top:1px solid var(--line);font-size:13px;color:var(--muted);display:grid;gap:6px}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto!important}}
"""

JS = r"""
document.querySelectorAll('button.copy').forEach(function(b){
  b.addEventListener('click',function(){
    var pre=document.getElementById(b.dataset.target);var txt=pre.innerText;
    function done(){var o=b.textContent;b.textContent='Copiado';setTimeout(function(){b.textContent=o},1400)}
    function fallback(){var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Texto seleccionado';setTimeout(function(){b.textContent='Copiar'},1600)}
    try{navigator.clipboard.writeText(txt).then(done,fallback)}catch(err){fallback()}
  });
});
"""


def chip(kind, label):
    return f'<span class="chip {kind}">{e(label)}</span>'


def ref_figure(pid, label, width=560):
    uri, size = pin_img(pid, width)
    who, user, src, link, dim, head = credit(pid)
    p = c.PINS[pid]
    src_html = e(src)
    if link:
        src_html = f'<a href="{e(link)}" target="_blank" rel="noopener">{e(src)}</a>'
    return f"""<figure class="ref" style="margin:0">
  <img src="{uri}" alt="{e(p['what'])}" loading="lazy">
  <div class="cap">
    <div>{chip('c-gold', 'Aprobada')} <span class="mono small">{e(label)}</span></div>
    <div><b>{e(p['what'])}</b></div>
    <div><a href="{pin_url(pid)}" target="_blank" rel="noopener">Abrir pin en Pinterest</a> · <span class="muted">guardado por {e(who)}{(' (@' + e(user) + ')') if user else ''}</span></div>
    <div class="muted">Origen: {src_html} · imagen {e(str(dim).replace(',', '×'))} px</div>
    <div class="id">ID {pid}</div>
  </div>
</figure>"""


def build_html():
    logo_uri, _ = pdf_img("alm-1.jpg", 220, crop=(30, 20, 165, 195))
    out = []
    A = out.append
    A('<title>Moodboard GUDCUK Matrimonios</title>')
    A('<meta name="claude:viewport-fit-sides" content="cover">')
    A('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    A('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Antonio:wght@600;700&family=IBM+Plex+Mono:wght@400;600&family=Source+Sans+3:wght@400;600;700&display=swap">')
    A(f'<style>{CSS}</style>')
    A('<div class="wrap">')
    # header
    A(f'''<header class="top">
  <div class="row"><span class="logo-chip"><img src="{logo_uri}" alt="Logotipo GUD CUK Catering tomado del PDF Almuerzos y Cenas"></span>
  <span class="eyebrow">Anuncio vertical · 25 s · público: wedding planners</span></div>
  <h1>{e(c.TITLE)}</h1>
  <p class="muted" style="max-width:820px">Moodboard de producción para un anuncio de 25 segundos generado con Higgsfield. Reúne el análisis del video anterior, la oferta real de los PDFs, referencias de Pinterest verificadas, el storyboard escena por escena y los prompts listos para copiar.</p>
  <div class="legend">{chip('c-gold','Referencia aprobada')}{chip('c-line','Alternativa')}{chip('c-ok','Verificado')}{chip('c-warn','Pendiente / riesgo')}{chip('c-no','Bloqueado')}</div>
</header>''')
    nav = [("brief", "01", "Brief"), ("video", "02", "Video original"), ("identidad", "03", "Identidad"), ("gastronomia", "04", "Gastronomía"),
           ("storyboard", "05", "Moodboard cronológico"), ("alternativas", "06", "Alternativas"), ("prompts", "07", "Prompts"), ("checklist", "08", "Checklist")]
    A('<nav class="toc" aria-label="Secciones">' + "".join(f'<a href="#{a}"><b>{n}</b>{e(t)}</a>' for a, n, t in nav) + '</nav>')

    # 01 brief
    b = c.BRIEF
    A(f'''<section class="sec" id="brief"><div class="sec-head"><span class="num">01</span><h2>Brief y objetivo comercial</h2></div>
<div class="concept"><span class="eyebrow">Concepto</span><h2>{e(b["concept"])}</h2><p style="max-width:760px;font-size:18px">{e(b["concept_line"])}</p></div>
<div class="grid g2">
 <div class="panel"><h3>Objetivo</h3><p>{e(b["objective"])}</p></div>
 <div class="panel"><h3>Público</h3><p>{e(b["audience"])}</p></div>
 <div class="panel"><h3>Insight</h3><p>{e(b["insight"])}</p></div>
 <div class="panel"><h3>Posicionamiento</h3><p>{e(b["positioning"])}</p></div>
 <div class="panel"><h3>Regla de protagonismo</h3><p>{e(b["not_this"])}</p></div>
 <div class="panel"><h3>Formato y CTA</h3><p>{e(b["format"])}</p><p>{e(b["cta"])}</p></div>
</div>
<div class="panel"><h3>Texto en pantalla, escena por escena</h3><div class="copyline">{"".join(f'<div><span class="mono">{k}</span><span>{e(v)}</span></div>' for k, v in b["copy"])}</div>
<p class="muted small">El texto se añade en edición, no dentro de los clips de IA.</p></div>
<div class="panel"><h3>Archivos recibidos (fase 1)</h3><div class="tablewrap"><table><thead><tr><th>Archivo</th><th>Tipo</th><th>Estado</th><th>Nota</th></tr></thead><tbody>
{"".join(f'<tr><td>{e(f)}</td><td>{e(t)}</td><td>{chip("c-ok" if s=="Analizado" else ("c-no" if s=="No recibido" else "c-warn"), s)}</td><td>{e(n)}</td></tr>' for f, t, s, n in c.FILES)}
</tbody></table></div></div>
</section>''')

    # 02 video
    frames_html = []
    rows = []
    for name, a, z, desc, txt, cam, fn in c.SHOTS:
        uri, _ = frame_img(name, 240)
        frames_html.append(f'<figure><img src="{uri}" alt="{e(desc)}" loading="lazy"><figcaption>{a}</figcaption></figure>')
        turi, _ = frame_img(name, 144)
        rows.append(f'<tr><td class="thumb"><img src="{turi}" alt="" loading="lazy"></td><td class="mono">{a}–{z}</td><td>{e(desc)}</td><td><i>{e(txt)}</i></td><td>{e(cam)}</td><td>{e(fn)}</td></tr>')
    A(f'''<section class="sec" id="video"><div class="sec-head"><span class="num">02</span><h2>Análisis del video original</h2>
<p class="muted">Un fotograma por plano, extraído del centro de cada corte. Lo observado está en la tabla; la interpretación va aparte.</p></div>
<div class="frames">{"".join(frames_html)}</div>
<div class="grid g3">{"".join(f'<div class="panel"><span class="eyebrow">{e(k)}</span><p>{e(v)}</p></div>' for k, v in c.VIDEO_SPECS)}</div>
<div class="panel"><h3>Lista de planos (observado)</h3><div class="tablewrap"><table><thead><tr><th></th><th>Tiempo</th><th>Lo que se ve</th><th>Texto en pantalla</th><th>Cámara</th><th>Función</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div></div>
<div class="grid g3">
 <div class="panel"><h3>Lectura creativa</h3><span class="chip c-line">Interpretación</span><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.VIDEO_READING)}</ul></div>
 <div class="panel"><h3>Conservar</h3><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.KEEP)}</ul></div>
 <div class="panel"><h3>Mejorar</h3><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.IMPROVE)}</ul></div>
</div></section>''')

    # 03 identidad
    idt = c.IDENTITY
    style_refs = "".join(
        f'<figure style="margin:0" class="ref"><img src="{pin_img(p, 360)[0]}" alt="{e(c.PINS[p]["what"])}" loading="lazy" style="max-height:340px;object-fit:cover"><div class="cap"><span class="muted">{e(c.PINS[p]["what"])}</span><a href="{pin_url(p)}" target="_blank" rel="noopener">Pin</a></div></figure>'
        for p in ["1103100502517478668", "235172411767956567", "521010250662396060", "267471665365495378"])
    A(f'''<section class="sec" id="identidad"><div class="sec-head"><span class="num">03</span><h2>Identidad visual y dirección artística</h2>
<p class="muted">Colores medidos sobre las páginas de los PDFs. La dirección artística es la propuesta para el anuncio.</p></div>
<div class="swatches">{"".join(f'<div class="sw"><div class="c" style="background:{h}"></div><div class="t"><b>{e(n)}</b><span class="mono">{h}</span><span class="muted">{e(u)}</span></div></div>' for n, h, u in idt["palette"])}</div>
<div class="grid g2">
 <div class="panel"><h3>Lo que muestran los PDFs</h3><span class="chip c-ok">Observado</span><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in idt["observed"])}</ul></div>
 <div class="panel"><h3>Dirección para el anuncio</h3><span class="chip c-line">Propuesta</span><dl class="kv">{"".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in idt["direction"])}</dl></div>
</div>
<div class="grid g3" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">{style_refs}</div>
</section>''')

    # 04 gastronomía
    pdfs = [("alm-4.jpg", "Almuerzos y Cenas · p.4 · Selección Social"), ("coc-2.jpg", "Cócteles · p.2 · Formatos"), ("coc-3.jpg", "Cócteles · p.3 · Bocaditos salados"),
            ("coc-4.jpg", "Cócteles · p.4 · Bocaditos dulces"), ("buf-4.jpg", "Buffets · p.4 · Italiano"), ("des-6.jpg", "Desayunos · p.6 · Servicio y logística")]
    pdf_html = "".join(f'<figure><img src="{pdf_img(f, 380)[0]}" alt="{e(t)}" loading="lazy"><figcaption>{e(t)}</figcaption></figure>' for f, t in pdfs)
    offer_rows = "".join(f'<tr><td>{e(a)}</td><td><b>{e(b_)}</b></td><td>{e(p)}</td><td class="mono">{e(s)}</td><td>{e(n)}</td></tr>' for a, b_, p, s, n in c.OFFER)
    crit = ["Visual", "Presentación", "Matrimonio", "Cine", "Premium"]
    prods = "".join(f'''<div class="panel prod"><div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap"><h3>{e(n)}</h3><span class="chip c-gold">{e(sc)}</span></div>
<p class="muted small">{e(src)}</p><p><i>«{e(q)}»</i></p><p>{e(why)}</p>
<div class="score">{"".join(f"<span>{k} {v}/5</span>" for k, v in zip(crit, s))}</div></div>''' for n, src, q, sc, why, s in c.PRODUCTS)
    A(f'''<section class="sec" id="gastronomia"><div class="sec-head"><span class="num">04</span><h2>Productos y propuesta gastronómica</h2>
<p class="muted">Solo platos y servicios que aparecen en los PDFs, con página citada. Las páginas se cuentan desde la portada del PDF; el folio es el número impreso.</p></div>
<div class="pdfs">{pdf_html}</div>
<div class="panel"><h3>Oferta documentada</h3><div class="tablewrap"><table><thead><tr><th>Catálogo</th><th>Propuesta</th><th>Precio</th><th>Fuente</th><th>Nota</th></tr></thead><tbody>{offer_rows}</tbody></table></div>
<ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.OFFER_NOTES)}</ul></div>
<div class="grid g2">{prods}</div>
<div class="grid g2">
 <div class="panel"><h3>Alternativas documentadas</h3><ul class="clean">{"".join(f"<li><b>{e(n)}</b> · <span class='muted'>{e(s)}</span>. {e(t)}</li>" for n, s, t in c.PRODUCT_ALTS)}</ul></div>
 <div class="panel"><h3>Descartado y por qué</h3><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.EXCLUDED)}</ul></div>
</div></section>''')

    # 05 storyboard
    durs = {"E1": 3.0, "E2": 3.5, "E3": 4.0, "E4": 4.0, "E5": 3.5, "E6": 4.0, "E7": 3.0}
    ruler = []
    for s in c.SCENES:
        if s["refs"]:
            ims = "".join(f'<img src="{pin_img(p, 220)[0]}" alt="">' for p, _ in s["refs"])
        else:
            ims = '<div class="card7">GUD<br>CUK</div>'
        ruler.append(f'<a href="#{s["id"].lower()}" style="flex:{durs[s["id"]]} 1 0"><span class="tc">{s["id"]} · {s["start"][3:]}–{s["end"][3:]}</span><span class="im">{ims}</span><span class="nm">{e(s["title"])}</span></a>')
    cmp_rows = "".join(f"<tr><td>{e(a)}</td><td class='mono'>{e(b_)}</td><td class='mono'>{e(r)}</td><td>{e(n)}</td></tr>" for a, b_, r, n in c.TIMELINE_COMPARE)
    scenes = []
    for s in c.SCENES:
        if s["refs"]:
            refs = "".join(ref_figure(p, lab) for p, lab in s["refs"])
            refs_cls = "refs two" if len(s["refs"]) > 1 else "refs"
        else:
            refs = '<div class="brandcard"><div class="in"><div class="lg">GUD<br>CUK</div><div class="ct">CATERING</div><div style="font-size:15px">Catering para matrimonios</div><div class="cta">COTIZA POR WHATSAPP</div><div class="mono" style="font-size:12px">@gudcukcatering</div></div></div><p class="muted small">Maqueta de la placa final. Se arma en edición.</p>'
            refs_cls = "refs"
        prompts = []
        for pid_label, pid, text in s["prompts"]:
            tid = f"pr-{pid_label.split()[0]}"
            base = f'Imagen base: <a href="{pin_url(pid)}" target="_blank" rel="noopener">pin {pid}</a>' if pid else "Sin imagen base (text-to-video)"
            prompts.append(f'''<div class="prompt"><div class="ph"><span class="mono small"><b>{e(pid_label)}</b> · {base}</span><button class="copy" type="button" data-target="{tid}">Copiar</button></div>
<pre id="{tid}">{e(text)}</pre><div class="neg">Evitar: {e(c.NEG)}</div></div>''')
        cine = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in s["cine"])
        alts = ""
        if s["alts"]:
            alts = '<div class="altrow">' + "".join(f'<figure><img src="{pin_img(p, 280)[0]}" alt="{e(c.PINS[p]["what"])}" loading="lazy"><figcaption><a href="{pin_url(p)}" target="_blank" rel="noopener">Alternativa · pin</a></figcaption></figure>' for p in s["alts"]) + '</div>'
        risks = "".join(f'<li>{e(c.PINS[p]["risk"])}</li>' for p, _ in s["refs"])
        scenes.append(f'''<article class="scene" id="{s["id"].lower()}">
<div class="scene-head"><span class="tc">{s["id"]} · {s["start"]}–{s["end"]} · {s["dur"]}</span><h3>{e(s["title"])}</h3></div>
<div class="scene-body">
 <div class="{refs_cls}">{refs}</div>
 <div class="info">
  <div class="block"><span class="eyebrow">Texto en pantalla</span><p class="ontext">{e(s["text"])}</p></div>
  <div class="block"><span class="eyebrow">Objetivo estratégico</span><p>{e(s["objective"])}</p></div>
  <div class="block"><span class="eyebrow">Dirección de fotografía</span><dl class="kv">{cine}</dl></div>
  <div class="block"><span class="eyebrow">Acción visual</span><p>{e(s["action"])}</p></div>
  <div class="block"><span class="eyebrow">Transición</span><p>{e(s["transition"])}</p></div>
  <div class="block"><span class="eyebrow">Audio</span><p>{e(s["audio"])}</p></div>
  <div class="block"><span class="eyebrow">Higgsfield</span><p>{e(s["higgs"])}</p></div>
  {"".join(prompts)}
  <div class="block"><span class="eyebrow">Criterio de aprobación</span><p>{e(s["approval"])}</p></div>
  {f'<div class="block"><span class="eyebrow">Riesgos de la referencia</span><ul class="clean small">{risks}</ul></div>' if risks else ''}
 </div>
</div>{alts}</article>''')
    A(f'''<section class="sec" id="storyboard"><div class="sec-head"><span class="num">05</span><h2>Moodboard cronológico</h2>
<p class="muted">El ancho de cada bloque es proporcional a su duración. Total: 25,0 s.</p></div>
<div><div class="ruler">{"".join(ruler)}</div><div class="ticks"><span>0 s</span><span>5</span><span>10</span><span>15</span><span>20</span><span>25 s</span></div></div>
<div class="panel"><h3>Hipótesis inicial y montaje recomendado</h3><p>La estructura inicial dejaba 1 s para la marca. Un segundo no alcanza para leer el nombre y el CTA, así que el montaje recomendado reserva 3 s para el cierre y acorta E1, E2 y E5.</p>
<div class="tablewrap"><table class="compare"><thead><tr><th>Momento</th><th>Hipótesis</th><th>Recomendado</th><th>Cambio</th></tr></thead><tbody>{cmp_rows}</tbody></table></div>
<p class="muted small">Comida, bebida o servicio son el sujeto principal en 15 de los 25 s (E2-B, E3, E4, E5 y E6-A). E1 muestra la mesa ya puesta y E7 es la marca.</p></div>
{"".join(scenes)}
</section>''')

    # 06 alternativas
    alt_cards = []
    for pid, p in c.PINS.items():
        if p["role"] != "alternativa":
            continue
        who, user, src, link, dim, head = credit(pid)
        alt_cards.append(f'''<div class="alt"><img src="{pin_img(pid, 360)[0]}" alt="{e(p["what"])}" loading="lazy">
<div class="t"><span>{chip("c-line", "Alternativa · " + p["scene"])}</span><b>{e(p["what"])}</b><span>{e(p["why"])}</span><span class="muted">Riesgo: {e(p["risk"])}</span>
<span><a href="{pin_url(pid)}" target="_blank" rel="noopener">Abrir pin</a> · <span class="muted">{e(src)}</span></span></div></div>''')
    disc = "".join(f'<li><a href="{pin_url(i)}" target="_blank" rel="noopener">pin {i}</a> · {e(r)}</li>' for i, r in c.DISCARDED_PINS)
    A(f'''<section class="sec" id="alternativas"><div class="sec-head"><span class="num">06</span><h2>Referencias alternativas</h2>
<p class="muted">Buenas fotos que no quedaron como primera opción. Sirven de reemplazo si una generación falla.</p></div>
<div class="alts">{"".join(alt_cards)}</div>
<div class="panel"><h3>Revisadas y descartadas</h3><ul class="clean small">{disc}</ul></div>
</section>''')

    # 07 prompts
    plist = []
    for s in c.SCENES:
        for pid_label, pid, text in s["prompts"]:
            tid = f"pl-{pid_label.split()[0]}"
            base = f'<a href="{pin_url(pid)}" target="_blank" rel="noopener">pin {pid}</a>' if pid else "sin imagen base"
            thumb = f'<img src="{pin_img(pid, 160)[0]}" alt="" style="width:64px;height:84px;object-fit:cover;border-radius:4px">' if pid else '<div style="width:64px;height:84px;border-radius:4px;background:var(--wine)"></div>'
            plist.append(f'''<div class="prompt" style="grid-template-columns:72px 1fr;align-items:start">{thumb}<div style="display:grid;gap:8px;min-width:0"><div class="ph"><span class="mono small"><b>{e(pid_label)}</b> · {s["id"]} {e(s["title"])} · {base}</span><button class="copy" type="button" data-target="{tid}">Copiar</button></div><pre id="{tid}">{e(text)}</pre></div></div>''')
    A(f'''<section class="sec" id="prompts"><div class="sec-head"><span class="num">07</span><h2>Prompts finales para Higgsfield</h2>
<p class="muted">Un prompt por generación. Subir la imagen base indicada y pegar el prompt. Modo: image-to-video con una imagen inicial; las funciones disponibles dependen del plan.</p></div>
<div class="panel"><span class="eyebrow">Negativos comunes (si el modelo los acepta)</span><pre class="mono small" style="margin:0;white-space:pre-wrap">{e(c.NEG)}</pre></div>
<div class="grid" style="gap:12px">{"".join(plist)}</div>
<div class="panel"><h3>Instrucciones de edición</h3><div class="tablewrap"><table><thead><tr><th>#</th><th>Toma</th><th>Prompt</th><th>Entra</th><th>Duración</th><th>Corte / transición</th><th>Sonido</th></tr></thead><tbody>
{"".join(f'<tr><td class="mono">{a}</td><td class="mono">{b_}</td><td class="mono">{p}</td><td class="mono">{t}</td><td class="mono">{d}</td><td>{e(tr)}</td><td>{e(so)}</td></tr>' for a, b_, p, t, d, tr, so in c.EDIT)}
</tbody></table></div><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in c.EDIT_NOTES)}</ul></div>
</section>''')

    # 08 checklist
    cls = {"ok": ("c-ok", "Verificado"), "warn": ("c-warn", "Pendiente"), "no": ("c-no", "Bloqueado")}
    val = "".join(f'<div><span class="chip {cls[k][0]}">{cls[k][1]}</span><span>{e(t.format(n_pins=N_PINS))}</span></div>' for k, t in c.VALIDATION)
    groups = "".join(f'<div class="panel"><h3>{e(g)}</h3><ul class="clean">{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>' for g, items in c.CHECKLIST.items())
    A(f'''<section class="sec" id="checklist"><div class="sec-head"><span class="num">08</span><h2>Checklist de producción</h2></div>
<div class="panel"><h3>Validación final</h3><div class="vlist">{val}</div></div>
<div class="checks">{groups}</div>
</section>''')

    A(f'''<footer><span>Preparado el 26-10-2026 a partir del video y 4 PDFs de GUDCUK, con referencias de Pinterest comprobadas el mismo día.</span>
<span>Las imágenes de Pinterest se muestran como referencia interna de producción. No se verificaron sus derechos de uso.</span></footer>''')
    A('</div>')
    A(f'<script>{JS}</script>')
    return "\n".join(out)


# ---------- Markdown ----------
def build_md():
    L = []
    A = L.append
    A(f"# {c.TITLE}\n")
    A("Moodboard de producción para un anuncio vertical de 25 s generado con Higgsfield, dirigido a wedding planners. Marca: **GUDCUK Catering** (logotipo GUD CUK · CATERING).\n")
    A("> El tablero de Miro no se pudo crear: el conector de Miro de la sesión solo tenía herramientas de lectura. Este documento y la página visual contienen el moodboard completo, listo para pasarlo a Miro.\n")
    A("## Archivos recibidos\n\n| Archivo | Tipo | Estado | Nota |\n|---|---|---|---|")
    for f, t, s, n in c.FILES:
        A(f"| {f} | {t} | {s} | {n} |")
    b = c.BRIEF
    A("\n## 01 — Brief y objetivo comercial\n")
    A(f"**Concepto: {b['concept']}.** {b['concept_line']}\n")
    for k, lab in [("objective", "Objetivo"), ("audience", "Público"), ("insight", "Insight"), ("positioning", "Posicionamiento"), ("not_this", "Regla de protagonismo"), ("format", "Formato"), ("cta", "CTA")]:
        A(f"- **{lab}:** {b[k]}")
    A("\n**Texto en pantalla (se añade en edición):**\n")
    for k, v in b["copy"]:
        A(f"- {k}: {v}")
    A("\n## 02 — Análisis del video original\n")
    for k, v in c.VIDEO_SPECS:
        A(f"- **{k}:** {v}")
    A("\n| Tiempo | Lo que se ve | Texto en pantalla | Cámara | Función |\n|---|---|---|---|---|")
    for name, a, z, desc, txt, cam, fn in c.SHOTS:
        A(f"| {a}–{z} | {desc} | {txt} | {cam} | {fn} |")
    A("\n**Lectura creativa (interpretación):**\n")
    for x in c.VIDEO_READING:
        A(f"- {x}")
    A("\n**Conservar:**\n")
    for x in c.KEEP:
        A(f"- {x}")
    A("\n**Mejorar:**\n")
    for x in c.IMPROVE:
        A(f"- {x}")
    A("\n## 03 — Identidad visual y dirección artística\n")
    for n, h, u in c.IDENTITY["palette"]:
        A(f"- **{n}** `{h}`: {u}")
    A("")
    for x in c.IDENTITY["observed"]:
        A(f"- {x}")
    A("\n**Dirección para el anuncio:**\n")
    for k, v in c.IDENTITY["direction"]:
        A(f"- **{k}:** {v}")
    A("\n## 04 — Productos y propuesta gastronómica\n")
    A("| Catálogo | Propuesta | Precio | Fuente | Nota |\n|---|---|---|---|---|")
    for a, b_, p, s, n in c.OFFER:
        A(f"| {a} | {b_} | {p} | {s} | {n} |")
    A("")
    for x in c.OFFER_NOTES:
        A(f"- {x}")
    A("\n**Seleccionados:**\n\n| Producto | Fuente | Cita | Escena | Por qué |\n|---|---|---|---|---|")
    for n, src, q, sc, why, s in c.PRODUCTS:
        A(f"| {n} | {src} | «{q}» | {sc} | {why} |")
    A("\n**Alternativas documentadas:**\n")
    for n, s, t in c.PRODUCT_ALTS:
        A(f"- **{n}** ({s}). {t}")
    A("\n**Descartado:**\n")
    for x in c.EXCLUDED:
        A(f"- {x}")
    A("\n## 05 — Moodboard cronológico\n")
    A("| Momento | Hipótesis | Recomendado | Cambio |\n|---|---|---|---|")
    for a, b_, r, n in c.TIMELINE_COMPARE:
        A(f"| {a} | {b_} | {r} | {n} |")
    for s in c.SCENES:
        A(f"\n### {s['id']} · {s['start']}–{s['end']} · {s['dur']} · {s['title']}\n")
        A(f"**Texto en pantalla:** {s['text']}\n")
        A(f"**Objetivo:** {s['objective']}\n")
        if s["refs"]:
            A("**Referencias aprobadas:**\n")
            for p, lab in s["refs"]:
                who, user, src, link, dim, head = credit(p)
                A(f"- {lab}: [pin {p}]({pin_url(p)}). {c.PINS[p]['what']} Guardado por {who}" + (f" (@{user})" if user else "") + f"; origen: {src}" + (f" ({link})" if link else "") + f". Movimiento: {c.PINS[p]['move']} Riesgo: {c.PINS[p]['risk']}")
        if s["alts"]:
            A("\n**Alternativas:** " + ", ".join(f"[pin {p}]({pin_url(p)})" for p in s["alts"]) + "\n")
        A("**Dirección de fotografía:**\n")
        for k, v in s["cine"]:
            A(f"- {k}: {v}")
        A(f"\n**Acción visual:** {s['action']}\n")
        A(f"**Transición:** {s['transition']}\n")
        A(f"**Audio:** {s['audio']}\n")
        A(f"**Higgsfield:** {s['higgs']}\n")
        for lab, p, text in s["prompts"]:
            A(f"**{lab}**" + (f" (imagen base: pin {p})" if p else "") + "\n\n```text\n" + text + "\n```\n")
        A(f"**Criterio de aprobación:** {s['approval']}")
    A("\n## 06 — Referencias alternativas\n")
    for pid, p in c.PINS.items():
        if p["role"] == "alternativa":
            A(f"- [pin {pid}]({pin_url(pid)}) · {p['scene']} · {p['what']} {p['why']} Riesgo: {p['risk']}")
    A("\n**Revisadas y descartadas:**\n")
    for i, r in c.DISCARDED_PINS:
        A(f"- [pin {i}]({pin_url(i)}): {r}")
    A("\n## 07 — Prompts finales para Higgsfield\n")
    A(f"Negativos comunes: `{c.NEG}`\n")
    for s in c.SCENES:
        for lab, p, text in s["prompts"]:
            A(f"**{lab} · {s['id']} {s['title']}**" + (f" · imagen base [pin {p}]({pin_url(p)})" if p else " · sin imagen base") + "\n\n```text\n" + text + "\n```\n")
    A("### Instrucciones de edición\n\n| # | Toma | Prompt | Entra | Duración | Corte / transición | Sonido |\n|---|---|---|---|---|---|---|")
    for row in c.EDIT:
        A("| " + " | ".join(row) + " |")
    A("")
    for x in c.EDIT_NOTES:
        A(f"- {x}")
    A("\n## 08 — Checklist de producción\n")
    lab = {"ok": "Verificado", "warn": "Pendiente", "no": "Bloqueado"}
    for k, t in c.VALIDATION:
        A(f"- **{lab[k]}:** {t.format(n_pins=N_PINS)}")
    for g, items in c.CHECKLIST.items():
        A(f"\n**{g}**\n")
        for x in items:
            A(f"- [ ] {x}")
    A("\n---\nLas imágenes de Pinterest son referencias de terceros. No se verificaron sus derechos de uso.")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    out_html, out_md = sys.argv[1], sys.argv[2]
    html = build_html()
    open(out_html, "w", encoding="utf-8").write(html)
    open(out_md, "w", encoding="utf-8").write(build_md())
    print("html bytes", len(html.encode()), "md ok")
