# -*- coding: utf-8 -*-
"""Convierte el archivo único de la vista previa en la web de verdad: una página por dirección.

Uso:  python3 construir.py prod    <fase> <carpeta_salida>   -> paquete para subir al alojamiento
      python3 construir.py preview <fase> <carpeta_salida>   -> vista previa para GitHub Pages (/apm-preview/)
"""
import re, os, sys, json, html, shutil, base64, hashlib, datetime
from datos import *

MODO = sys.argv[1]
FASE = int(sys.argv[2])
OUT = sys.argv[3]
PROD = MODO == 'prod'
BASE = '/' if PROD else '/apm-preview/'
HOY = datetime.date.today().isoformat()
AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = open(os.path.join(AQUI, 'fuente', 'archivo-unico.html'), encoding='utf-8').read()

if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

# ------------------------------------------------------------------ utilidades
def secciones_nivel_superior(s):
    tok = re.compile(r'<section\b|</section>')
    res, depth, ini = [], 0, None
    for m in tok.finditer(s):
        if m.group(0) == '<section':
            if depth == 0:
                ini = m.start()
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                res.append((ini, m.end()))
    return res

def texto(h):
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()

def esc(t):
    return html.escape(t, quote=True)

def escribir(ruta_rel, contenido, modo='w'):
    p = os.path.join(OUT, ruta_rel.lstrip('/'))
    os.makedirs(os.path.dirname(p) or OUT, exist_ok=True)
    if 'b' in modo:
        open(p, modo).write(contenido)
    else:
        open(p, modo, encoding='utf-8').write(contenido)

# ------------------------------------------------------------------ piezas del archivo único
head = SRC[:SRC.find('</head>')]
body = SRC[SRC.find('<body>') + 6: SRC.rfind('</body>')]
mi, mf = body.find('<main id="contenido">'), body.find('</main>')
antes_main = body[:mi]
despues_main = body[mf + len('</main>'):]
main = body[mi + len('<main id="contenido">'):mf]

PAG_HTML = {}
for a, b in secciones_nivel_superior(main):
    blk = main[a:b]
    pid = re.search(r'\bid="([^"]+)"', blk[:blk.find('>')]).group(1)
    PAG_HTML[pid] = blk

# cromo común (cabecera, menú móvil, pie, barra de acciones, cookies, visor de fotos)
cromo_arriba = antes_main
corte = despues_main.find('<script')
cromo_abajo = despues_main[:corte]
cromo_abajo = re.sub(r'<div class="demo-note">.*?</div>\s*', '', cromo_abajo, flags=re.S)  # aviso de demo: fuera

scripts = [m for m in re.finditer(r'<script([^>]*)>(.*?)</script>', SRC, re.S) if 'ld+json' not in m.group(1)]
JS_MEJORAS = scripts[1].group(2)
JS_INTERACCION = scripts[2].group(2)

# ------------------------------------------------------------------ recursos: CSS, letras, logo, iconos
os.makedirs(os.path.join(OUT, 'assets', 'fonts'), exist_ok=True)
os.makedirs(os.path.join(OUT, 'assets', 'ph'), exist_ok=True)
css = '\n'.join(m.group(1) for m in re.finditer(r'<style[^>]*>(.*?)</style>', SRC, re.S))

def _fuente(m):
    fam, peso, b64 = m.group(1), m.group(2), m.group(3)
    nombre = f'{fam.lower()}-{peso}.woff2'
    escribir(f'assets/fonts/{nombre}', base64.b64decode(b64), 'wb')
    return (f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{peso};font-display:swap;"
            f"src:url(fonts/{nombre}) format('woff2')}}")
css = re.sub(r"@font-face\{font-family:'([^']+)';font-style:normal;font-weight:(\d+);font-display:swap;"
             r"src:url\(data:font/woff2;base64,([A-Za-z0-9+/=]+)\) format\('woff2'\)\}", _fuente, css)

def _ph(m):
    nombre, b64 = m.group(1), m.group(2)
    escribir(f'assets/ph/{nombre}.jpg', base64.b64decode(b64), 'wb')
    # el dibujo de respaldo solo se pide si la foto falla (antes se descargaba siempre)
    return f'img.ph-err[data-ph="{nombre}"]{{background-image:url(ph/{nombre}.jpg)'
css = re.sub(r'img\[data-ph="([^"]+)"\]\{background-image:url\(data:image/jpeg;base64,([A-Za-z0-9+/=]+)\)', _ph, css)

m = re.search(r'\.brand__mark\{background-image:url\(data:image/png;base64,([A-Za-z0-9+/=]+)\)', css)
escribir('assets/logo-apm.png', base64.b64decode(m.group(1)), 'wb')
css = css.replace(m.group(0), '.brand__mark{background-image:url(logo-apm.png)')
for rel, nombre in (('icon', 'favicon.png'), ('apple-touch-icon', 'apple-touch-icon.png')):
    mm = re.search(r'<link rel="' + rel + r'" href="data:image/png;base64,([A-Za-z0-9+/=]+)"', head)
    escribir('assets/' + nombre, base64.b64decode(mm.group(1)), 'wb')

# navegación por anclas del archivo único -> páginas normales
css = css.replace('.vpage{display:none;scroll-margin-top:0}', '.vpage{display:block;scroll-margin-top:0}')
css = css.replace('.vpage:target{display:block}', '')
css = css.replace('.vpage:target ~ #p-index{display:none}', '')
css = css.replace('html:not(:has(.vpage:target)) body{', 'html.es-portada body{')
css = css.replace('html:not(:has(.vpage:target)){', 'html.es-portada{')
# el fondo oscuro del vídeo era para la portada, pero estaba puesto a toda la web: los artículos salían con letra oscura sobre fondo oscuro
assert css.count('html,body{background:#06110a}') == 1
css = css.replace('html,body{background:#06110a}', 'html.es-portada,html.es-portada body{background:#06110a}')
assert 'data:font' not in css and 'data:image/jpeg' not in css, 'quedan datos incrustados en el CSS'
css += ('\n/* franja de cifras de la portada: vuelve a ser oscura, que las cifras son blancas (salían blanco sobre blanco) */\n'
        'body.portada #p-index > section.strip{background:rgba(10,26,18,.90)!important}\n'
        '/* «Cómo trabajamos» de la portada: sección oscura con letra blanca (salía blanco sobre blanco) */\n'
        'body.portada #p-index > section.section--ink{background:rgba(10,26,18,.90)!important}\n'
        'body.portada #p-index > section.section--paper2{background:rgba(244,241,234,.94)!important}\n'
        '/* subtítulo del logo con contraste suficiente */\n.brand__txt span{color:#46505a}\n')
css += '\n/* foto original de la obra dentro del artículo */\n.prose figure{margin:1.8rem 0}.prose figure img{margin:0;width:100%;height:auto}.prose figcaption{font-size:.92rem;color:var(--ink-3,#5b6472);margin-top:.6rem}\n'
css = '/* Reformas APM — estilos (generado desde el archivo único) */\n' + css
VCSS = hashlib.md5(css.encode()).hexdigest()[:8]
escribir('assets/apm.css', css)

# ------------------------------------------------------------------ JavaScript común
js1 = JS_MEJORAS
assert "if(t && t.tagName==='IMG' && !t.dataset.px){ t.dataset.px='1'; t.src=PX; }" in js1
assert "if(i.complete && i.naturalWidth===0 && !i.dataset.px){ i.dataset.px='1'; i.src=PX; }" in js1
js1 = js1.replace("if(t && t.tagName==='IMG' && !t.dataset.px){ t.dataset.px='1'; t.src=PX; }",
                  "if(t && t.tagName==='IMG' && !t.dataset.px){ t.dataset.px='1'; t.classList.add('ph-err'); t.src=PX; }")
js1 = js1.replace("if(i.complete && i.naturalWidth===0 && !i.dataset.px){ i.dataset.px='1'; i.src=PX; }",
                  "if(i.complete && i.naturalWidth===0 && !i.dataset.px){ i.dataset.px='1'; i.classList.add('ph-err'); i.src=PX; }")
# la navegación por anclas ya no existe: solo marcamos en el menú la página en la que estamos
ini = js1.find('  /* Al cambiar de página')
fin = js1.find('  /* Bloquear el scroll')
js1 = js1[:ini] + """  /* Marca en el menú la página actual */
  (function(){
    var aqui = location.pathname.replace(/index\\.html$/, '');
    document.querySelectorAll('.nav a, .mobile-nav a').forEach(function(a){
      var h = a.getAttribute('href'); if(h && h === aqui) a.classList.add('active');
    });
  })();

""" + js1[fin:]
ini = js1.find('  /* Aviso inicial */')
fin = js1.find('})();', ini)
js1 = js1[:ini] + js1[fin:]
assert 'hashchange' not in js1 and 'demo-note' not in js1
js2 = JS_INTERACCION
_v = '    if (img.dataset.fbDone) return;                       // ya sustituida'
assert _v in js2
js2 = js2.replace(_v, _v + '\n    if (img.dataset.ph) return;  // tiene dibujo de respaldo (clase ph-err): que se vea')
js = '/* Reformas APM — comportamiento común */\n' + js1 + '\n' + js2
VJS = hashlib.md5(js.encode()).hexdigest()[:8]
escribir('assets/apm.js', js)

# ------------------------------------------------------------------ vídeos de la portada
def js_videos():
    lista = [[BASE + 'video/' + n, c] for n, c in VIDEOS] if PROD else [[c] for n, c in VIDEOS]
    return """<script>(function(){
/* Vídeos de la portada. Primero el archivo propio de la web (carpeta /video/); si no está, el de Higgsfield.
   Solo se carga el que se ve y el siguiente; con ahorro de datos o «reducir movimiento» se queda la foto. */
var V=%s;
var a=document.getElementById('heroVidA'),b=document.getElementById('heroVidB');
if(!a||!b)return;
var cn=navigator.connection||{};
if((window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)||cn.saveData||/2g/.test(cn.effectiveType||''))return;
function carga(v,n){var f=V[n];if(v.dataset.n==String(n))return;v.dataset.n=n;v.innerHTML='';
 f.forEach(function(u){var s=document.createElement('source');s.src=u;s.type='video/mp4';v.appendChild(s)});
 v.preload='auto';try{v.load()}catch(e){}}
var act=0,i=-1,vs=[a,b],t=null;
function pon(n){n=(n%%V.length+V.length)%%V.length;if(n===i)return;i=n;
 var s=1-act,v=vs[s],ant=vs[act];carga(v,n);
 try{v.currentTime=0}catch(e){}
 var p=v.play();if(p&&p.catch)p.catch(function(){});
 v.classList.add('on');ant.classList.remove('on');
 setTimeout(function(){try{ant.pause()}catch(e){};carga(ant,(i+1)%%V.length)},1300);act=s}
pon(0);
function arranca(){if(!t)t=setInterval(function(){pon(i+1)},6000)}
function para(){if(t){clearInterval(t);t=null}}
arranca();
document.addEventListener('visibilitychange',function(){document.hidden?para():arranca()});
var portada=document.getElementById('p-index');
window.addEventListener('scroll',function(){
 if(!portada)return;var alto=portada.scrollHeight-window.innerHeight;if(alto<=0)return;
 var y=Math.min(alto,Math.max(0,window.scrollY-portada.offsetTop));var rec=y/alto;
 var bg=document.querySelector('.hero__bg--video');
 if(bg)bg.style.opacity=rec>0.96?String(Math.max(0,(1-rec)/0.04)):'1';
},{passive:true});
document.addEventListener('touchstart',function(){var v=vs[act];if(v.paused){var p=v.play();if(p&&p.catch)p.catch(function(){})}},{once:true,passive:true});
})();</script>""" % json.dumps(lista)

# ------------------------------------------------------------------ direcciones
PUB = {p['id']: p for p in PAGINAS if p['fase'] <= FASE}
TODAS = {p['id']: p for p in PAGINAS}

def url_de(pid):
    pid = ALIAS.get(pid, pid)
    if pid not in PUB:
        return None
    r = PUB[pid]['ruta']
    return BASE if r == '/' else BASE + r.lstrip('/')

def url_wp(ruta):
    """Artículos que sigue sirviendo WordPress: en la vista previa se enlazan a la web real."""
    return ruta if PROD else DOMINIO + ruta

def pagina_de_ancla(ancla):
    for pid, h in PAG_HTML.items():
        if re.search(r'\bid="' + re.escape(ancla) + '"', h):
            return pid
    return None

def reescribir_enlaces(h, pid_actual, en_cromo=False):
    def rep(m):
        attrs1, destino, attrs2, dentro = m.group(1), m.group(2), m.group(3), m.group(4)
        nuevo = None
        if destino.startswith('p-'):
            nuevo = url_de(destino)
            if nuevo is None:  # página que aún no se publica en esta fase
                ini, fin = m.start(), m.end()
                antes = h[:ini].rstrip()[-1:] if h[:ini].rstrip() else '>'
                despues = h[fin:].lstrip()[:1] or '<'
                if en_cromo or (antes == '>' and despues == '<'):
                    return ''  # elemento suelto (menú, chip, tarjeta): se quita
                return dentro  # enlace dentro de un texto: se queda el texto
        elif destino == 'formulario':
            nuevo = '#formulario' if pid_actual == 'p-contacto' else url_de('p-contacto') + '#formulario'
        elif destino in ('', 'contenido'):
            nuevo = '#' + destino
        else:
            if pid_actual and re.search(r'\bid="' + re.escape(destino) + '"', PAG_HTML.get(pid_actual, '')):
                nuevo = '#' + destino
            else:
                otro = pagina_de_ancla(destino)
                nuevo = (url_de(otro) + '#' + destino) if otro and url_de(otro) else '#' + destino
        return f'<a{attrs1}href="{nuevo}"{attrs2}>{dentro}</a>'
    h = re.sub(r'<a\b([^>]*?)href="#([^"]*)"([^>]*)>(.*?)</a>', rep, h, flags=re.S)
    # contenedores que se han quedado vacíos al quitar enlaces
    h = re.sub(r'<li>\s*</li>', '', h)
    h = re.sub(r'<p class="mt-2" style="font-weight:700">\s*</p>', '', h)
    return h

def correcciones(h):
    for viejo, nuevo in QUITAR_AFIRMACIONES:
        h = h.replace(viejo, nuevo)
    for viejo, nuevo in REENCUADRES:
        h = h.replace(viejo, nuevo)
    for patron in QUITAR_BLOQUES:
        h = re.sub(patron, '', h, flags=re.S)
    # citas de clientes que nadie ha confirmado: fuera
    def _cita(m):
        t = texto(m.group(0))
        if re.search(r'(cliente|clienta|vecino|vecina)', t, re.I) and re.search(r'(dijo|resumió|pidió|contó)', t):
            return ''
        return m.group(0)
    h = re.sub(r'<blockquote\b[^>]*>.*?</blockquote>', _cita, h, flags=re.S)
    # código postal de la oficina de Karmelo: el de su ficha de Google (48004)
    h = h.replace('Karmelo Kalea 15 · 48003', 'Karmelo Kalea 15 · 48004')
    h = h.replace('Karmelo Kalea 15, 48003', 'Karmelo Kalea 15, 48004')
    h = h.replace('Karmelo+Kalea+15,+48003', 'Karmelo+Kalea+15,+48004')
    h = h.replace('Karmelo%20Kalea%2015%2C%2048003', 'Karmelo%20Kalea%2015%2C%2048004')
    # página de gracias nueva
    h = h.replace('https://reformasapmbilbao.es/gracias.html', DOMINIO + '/gracias/')
    # logo propio (una sola descarga, sin depender de WordPress)
    h = h.replace('src="https://reformasapmbilbao.es/wp-content/uploads/2021/12/apm-reformas.png"', f'src="{BASE}assets/logo-apm.png"')
    # fotos: en la web real, misma carpeta de WordPress que hoy (dirección relativa); en la vista previa, la absoluta
    if PROD:
        h = h.replace('https://reformasapmbilbao.es/wp-content/', '/wp-content/')
    return h

# ------------------------------------------------------------------ ajustes por página
def ajustar(pid, h):
    p = TODAS[pid]
    if p.get('h1'):
        h = re.sub(r'(<h1[^>]*>).*?(</h1>)', lambda m: m.group(1) + esc(p['h1']) + m.group(2), h, count=1, flags=re.S)
        # la miga de pan repite el título del artículo
        h = re.sub(r'(<nav class="crumbs"[^>]*>.*?<span>›</span>)([^<]*)(</nav>)',
                   lambda m: m.group(1) + esc(p['h1']) + m.group(3), h, count=1, flags=re.S)
    if p.get('foto'):  # foto original de la obra, en su página de siempre
        src, alt = p['foto']
        src = src.replace(DOMINIO, '') if PROD else src
        fig = (f'<figure><img src="{src}" alt="{esc(alt)}" loading="lazy" decoding="async">'
               f'<figcaption>{esc(alt)}.</figcaption></figure>')
        m = re.search(r'<article class="prose">.*?</p>', h, re.S)
        if m:
            h = h[:m.end()] + '\n' + fig + h[m.end():]
        else:
            imgs = list(re.finditer(r'<img\b[^>]*>', h))
            objetivo = imgs[1] if len(imgs) > 1 else imgs[0]
            tag = objetivo.group(0)
            tag = re.sub(r'src="[^"]*"', f'src="{src}"', tag)
            tag = re.sub(r'alt="[^"]*"', f'alt="{esc(alt)}"', tag)
            tag = re.sub(r'\sdata-ph="[^"]*"', '', tag)
            h = h[:objetivo.start()] + tag + h[objetivo.end():]
    if pid == 'p-index':  # «Consulta tu zona»: todas las zonas que estén publicadas
        chips = [('p-reformas-santutxu', 'Santutxu')]
        chips += [('p-reformas-' + sl, nom) for sl, nom, fa in BARRIOS]
        chips += [('p-reformas-getxo', 'Getxo'), ('p-reformas-barakaldo', 'Barakaldo'), ('p-reformas-basauri', 'Basauri'),
                  ('p-reformas-sestao', 'Sestao'), ('p-reformas-bizkaia', 'Toda Bizkaia')]
        enl = ''.join(f'<a href="#{i}">{esc(n)}</a>' for i, n in chips)
        h, n = re.subn(r'<div class="zones mt-2">.*?</div>', '<div class="zones mt-2">' + enl + '</div>', h, count=1, flags=re.S)
        assert n == 1
    if pid == 'p-index':  # «Trabajos realizados» de la portada: solo obras reales, con su foto
        formas = ['wide', 'sq', 'sq', 'sq', 'sq', 'wide']
        orden = [0, 3, 1, 2, 4, 5]  # integral Santutxu, baño Miribilla, cocina Santutxu, baño Santutxu, Iparraguirre, salón
        items = []
        for forma, k in zip(formas, orden):
            titulo, lugar, ruta, foto = TRABAJOS_REALES[k]
            foto_url = foto.replace(DOMINIO, '') if PROD else foto
            es_wp = any(ruta == r for r, _, _ in SIGUEN_EN_WORDPRESS)
            enlace = url_wp(ruta) if es_wp else (BASE + ruta.lstrip('/'))
            items.append(f'<a class="folio__item folio__item--{forma}" href="{enlace}" data-lightbox="{foto_url}" '
                         f'data-cap="{esc(titulo)}" data-reveal><img src="{foto_url}" alt="{esc(titulo)}" loading="lazy">'
                         f'<span class="cap">{esc(titulo)}</span></a>')
        h, n = re.subn(r'<div class="folio mt-3">.*?</div>\s*(<div class="center mt-3">)', '<div class="folio mt-3">' + ''.join(items) + '</div>\n  \\1', h, count=1, flags=re.S)
        assert n == 1, 'no encuentro la galería de la portada'
        h = h.replace('Una pequeña muestra de pisos, cocinas y baños que hemos transformado. Cada obra, entregada a tiempo y rematada al detalle.',
                      'Algunas de las obras que hemos hecho en Bilbao, con sus fotos. Pulsa en cada una para verla en grande.')
    if pid == 'p-trabajos-realizados':
        h = trabajos(h)
    if pid == 'p-blog-index':
        h = blog_indice(h)
    return h

def trabajos(h):
    ini = h.find('<div class="grid grid--3">')
    fin = h.find('<div class="center mt-3" data-reveal>', ini)
    tarjetas = []
    for titulo, lugar, ruta, foto in TRABAJOS_REALES:
        foto_url = foto.replace(DOMINIO, '') if PROD else foto
        es_wp = any(ruta == r for r, _, _ in SIGUEN_EN_WORDPRESS)
        enlace = url_wp(ruta) if es_wp else (BASE + ruta.lstrip('/'))
        tarjetas.append(f'''<div class="postcard" data-reveal>
          <div class="postcard__img" data-lightbox="{foto_url}" data-cap="{esc(titulo)} · {esc(lugar)}" style="cursor:zoom-in">
            <img src="{foto_url}" alt="{esc(titulo)}" loading="lazy"></div>
          <div class="postcard__b"><span class="tag">{esc(lugar)}</span><h3>{esc(titulo)}</h3><p><a href="{enlace}">Ver la obra →</a></p></div>
        </div>''')
    otros = ' · '.join(esc(t) for t in TRABAJOS_SIN_FOTO)
    nuevo = ('<div class="grid grid--3">' + ''.join(tarjetas) + '</div>\n'
             f'      <p class="center mt-3" data-reveal style="margin-inline:auto">Otros trabajos: {otros}.</p>\n      ')
    h = h[:ini] + nuevo + h[fin:]
    h = h.replace('Una muestra de las reformas que hemos entregado en Bilbao y Bizkaia. Pisos, cocinas, baños y ventanas: cada obra, a tiempo y rematada al detalle.',
                  'Algunas de las obras que hemos hecho en Bilbao y Bizkaia, con sus fotos. Pulsa en cada una para ver cómo se hizo.')
    return h

def blog_indice(h):
    # títulos de las tarjetas iguales al H1 de cada artículo
    for p in PAGINAS:
        if p.get('h1') and p['tipo'] == 'articulo':
            h = re.sub(r'(<a class="postcard" href="#' + re.escape(p['id']) + r'".*?<h3>).*?(</h3>)',
                       lambda m: m.group(1) + esc(p['h1']) + m.group(2), h, count=1, flags=re.S)
    # los artículos de siempre que siguen en WordPress, enlazados desde el blog nuevo
    items = ''.join(f'<li><a href="{url_wp(r)}">{esc(t)}</a></li>' for r, t, _ in SIGUEN_EN_WORDPRESS)
    bloque = ('<section class="section section--paper2"><div class="container"><div class="shead" data-reveal>'
              '<span class="kicker">Más artículos</span><h2>Otros artículos del blog</h2></div>'
              f'<ul class="mt-2" style="columns:2 280px;gap:2rem;line-height:2">{items}</ul></div></section>')
    marca = '</div></div></section><section class="section"><div class="container">\n      <div class="ctaband"'
    assert marca in h, 'no encuentro el final del listado del blog'
    return h.replace(marca, '</div></div></section>' + bloque + '<section class="section"><div class="container">\n      <div class="ctaband"', 1)

# ------------------------------------------------------------------ datos estructurados
def jsonld(p, titulo, desc, h1, imagen):
    url = DOMINIO + p['ruta']
    sant, sadr = NEGOCIO['santutxu'], NEGOCIO['sanadrian']
    empresa = {
        '@type': 'GeneralContractor', '@id': DOMINIO + '/#empresa',
        'name': NEGOCIO['nombre'], 'alternateName': NEGOCIO['alt'], 'url': DOMINIO + '/',
        'logo': NEGOCIO['logo'], 'image': NEGOCIO['logo'],
        'telephone': NEGOCIO['tel_santutxu'], 'email': NEGOCIO['email'], 'priceRange': '€€',
        'address': {'@type': 'PostalAddress', 'streetAddress': sant['calle'], 'postalCode': sant['cp'],
                    'addressLocality': 'Bilbao', 'addressRegion': 'Bizkaia', 'addressCountry': 'ES'},
        'geo': {'@type': 'GeoCoordinates', 'latitude': sant['lat'], 'longitude': sant['lng']},
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '10:00', 'closes': '14:00'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], 'opens': '16:00', 'closes': '20:00'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Saturday', 'opens': '10:00', 'closes': '14:00'}],
        'contactPoint': {'@type': 'ContactPoint', 'telephone': NEGOCIO['tel_movil'], 'contactType': 'customer service', 'availableLanguage': 'es'},
        'areaServed': [{'@type': 'City', 'name': n} for n in ('Bilbao', 'Getxo', 'Barakaldo', 'Basauri', 'Sestao')] + [{'@type': 'AdministrativeArea', 'name': 'Bizkaia'}],
        'department': [{
            '@type': 'GeneralContractor', 'name': NEGOCIO['nombre'] + ' San Adrián', 'telephone': NEGOCIO['tel_movil'],
            'address': {'@type': 'PostalAddress', 'streetAddress': sadr['calle'], 'postalCode': sadr['cp'],
                        'addressLocality': 'Bilbao', 'addressRegion': 'Bizkaia', 'addressCountry': 'ES'},
            'geo': {'@type': 'GeoCoordinates', 'latitude': sadr['lat'], 'longitude': sadr['lng']}}],
    }
    migas = [{'@type': 'ListItem', 'position': 1, 'name': 'Inicio', 'item': DOMINIO + '/'}]
    if p['tipo'] == 'articulo':
        migas.append({'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': DOMINIO + '/blog/'})
    if p['ruta'] != '/':
        migas.append({'@type': 'ListItem', 'position': len(migas) + 1, 'name': p.get('miga') or h1, 'item': url})
    grafo = [empresa,
             {'@type': 'WebSite', '@id': DOMINIO + '/#web', 'url': DOMINIO + '/', 'name': NEGOCIO['nombre'], 'inLanguage': 'es', 'publisher': {'@id': DOMINIO + '/#empresa'}},
             {'@type': 'CollectionPage' if p['tipo'] == 'blog' else 'WebPage', '@id': url + '#pagina', 'url': url, 'name': titulo,
              'description': desc, 'inLanguage': 'es', 'isPartOf': {'@id': DOMINIO + '/#web'}, 'about': {'@id': DOMINIO + '/#empresa'},
              'breadcrumb': {'@id': url + '#migas'}, 'primaryImageOfPage': {'@type': 'ImageObject', 'url': imagen}},
             {'@type': 'BreadcrumbList', '@id': url + '#migas', 'itemListElement': migas}]
    if p['tipo'] == 'articulo':
        grafo.append({'@type': 'BlogPosting', '@id': url + '#articulo', 'headline': h1[:110], 'description': desc,
                      'image': imagen, 'datePublished': p['fecha'], 'dateModified': HOY, 'inLanguage': 'es',
                      'author': {'@id': DOMINIO + '/#empresa'}, 'publisher': {'@id': DOMINIO + '/#empresa'},
                      'mainEntityOfPage': {'@id': url + '#pagina'}})
    return json.dumps({'@context': 'https://schema.org', '@graph': grafo}, ensure_ascii=False, separators=(',', ':'))

# ------------------------------------------------------------------ montaje de cada página
CROMO_ARRIBA = correcciones(cromo_arriba)
CROMO_ABAJO = correcciones(cromo_abajo)

def cabeza(p, titulo, desc, h1, imagen):
    url = DOMINIO + p['ruta']
    robots = 'noindex, nofollow' if (not PROD or p.get('noindex')) else 'index, follow, max-image-preview:large, max-snippet:-1'
    verif = ''.join(f'<meta name="{n}" content="{v}">\n' for n, v in VERIFICACION) if p['ruta'] == '/' else ''
    canon = '' if p['ruta'] == '/404.html' else f'<link rel="canonical" href="{url}">\n'
    ogtipo = 'article' if p['tipo'] == 'articulo' else 'website'
    return f'''<!doctype html>
<html lang="es"{' class="es-portada"' if p['ruta'] == '/' else ''}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titulo)}</title>
<meta name="description" content="{esc(desc)}">
{canon}<meta name="robots" content="{robots}">
{verif}<meta property="og:type" content="{ogtipo}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Reformas APM">
<meta property="og:title" content="{esc(titulo)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{imagen}">
<meta name="theme-color" content="#12161d">
<link rel="icon" href="{BASE}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{BASE}assets/apple-touch-icon.png">
<link rel="preload" href="{BASE}assets/fonts/manrope-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{BASE}assets/fonts/fraunces-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{BASE}assets/apm.css?v={VCSS}">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{jsonld(p, titulo, desc, h1, imagen)}</script>
</head>
'''

def montar(pid):
    p = TODAS[pid]
    h = PAG_HTML[pid]
    h = correcciones(h)
    h = ajustar(pid, h)
    h = reescribir_enlaces(h, pid)
    h = re.sub(r'(<section class="vpage" id="[^"]+")\s+data-title="[^"]*"', r'\1', h, count=1)
    titulo = p.get('titulo') or html.unescape(re.search(r'data-title="([^"]*)"', PAG_HTML[pid]).group(1))
    h1 = texto(re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S).group(1))
    img = re.search(r'<img\b[^>]*src="([^"]+)"', h)
    imagen = img.group(1) if img else NEGOCIO['logo']
    if imagen.startswith('/wp-content/'):
        imagen = DOMINIO + imagen
    if 'assets/' in imagen or imagen.startswith('data:'):
        imagen = NEGOCIO['logo']
    arriba = reescribir_enlaces(CROMO_ARRIBA, pid, en_cromo=True)
    abajo = reescribir_enlaces(CROMO_ABAJO, pid, en_cromo=True)
    clase_body = ' class="portada"' if p['ruta'] == '/' else ''
    extra = js_videos() if p['ruta'] == '/' else ''
    doc = (cabeza(p, titulo, p['desc'], h1, imagen) + f'<body{clase_body}>\n' + arriba +
           '<main id="contenido">\n' + h + '\n</main>' + abajo +
           f'<script src="{BASE}assets/apm.js?v={VJS}" defer></script>\n' + extra + '\n</body>\n</html>\n')
    destino = p['ruta'] if p['ruta'].endswith('.html') else p['ruta'] + 'index.html'
    escribir(destino, doc)
    return dict(id=pid, ruta=p['ruta'], titulo=titulo, desc=p['desc'], h1=h1)

hechas = [montar(pid) for pid in PUB if pid in PAG_HTML]

# ------------------------------------------------------------------ mapa del sitio, robots, .htaccess
if PROD:
    urls = []
    for x in hechas:
        p = TODAS[x['id']]
        if p.get('noindex'):
            continue
        urls.append((DOMINIO + p['ruta'], HOY))
    for ruta, _, fecha in SIGUEN_EN_WORDPRESS:
        urls.append((DOMINIO + ruta, fecha))
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    xml += [f'  <url><loc>{u}</loc><lastmod>{f}</lastmod></url>' for u, f in urls]
    xml.append('</urlset>')
    escribir('sitemap.xml', '\n'.join(xml) + '\n')
    escribir('robots.txt', f'User-agent: *\nDisallow:\n\nSitemap: {DOMINIO}/sitemap.xml\n')
    os.makedirs(os.path.join(OUT, 'video'), exist_ok=True)
    escribir('video/LEEME.txt', 'Aquí van los cuatro vídeos de la portada: ' + ', '.join(n for n, _ in VIDEOS) +
             '.\nMientras no estén, la portada los coge de Higgsfield, así que se ve igual.\n')
    reglas = ['# BEGIN Reformas APM - web nueva (este bloque va ENCIMA de "# BEGIN WordPress")',
              '# La web nueva vive en la carpeta /nueva/. Si una dirección tiene página nueva, se sirve esa;',
              '# si no, contesta WordPress como siempre. Para volver atrás basta con quitar este bloque.',
              'ErrorDocument 404 /nueva/404.html',
              '<IfModule mod_rewrite.c>',
              'RewriteEngine On',
              'RewriteBase /']
    for patron, destino, motivo in REDIRECCIONES:
        reglas += [f'# 301: {motivo}', f'RewriteRule {patron} {destino} [R=301,L]']
    reglas += ['# Recursos de la web nueva',
               'RewriteRule ^(assets/.+|video/.+|sitemap\\.xml|robots\\.txt)$ /nueva/$1 [L]',
               '# Dirección sin barra final que existe en la web nueva: a la versión con barra (como hace WordPress)',
               'RewriteCond %{REQUEST_METHOD} ^(GET|HEAD)$',
               'RewriteCond %{DOCUMENT_ROOT}/nueva/$1/index.html -f',
               'RewriteRule ^(.+[^/])$ /$1/ [R=301,L]',
               '# Portero: solo para leer páginas (GET/HEAD), nunca para el panel ni vistas previas de WordPress.',
               '# Con ?origen=wp se ve siempre lo que daría WordPress (para comparar).',
               'RewriteCond %{REQUEST_METHOD} ^(GET|HEAD)$',
               'RewriteCond %{QUERY_STRING} !(^|&)(p|page_id|s|preview|origen)= [NC]',
               'RewriteCond %{DOCUMENT_ROOT}/nueva/$1index.html -f',
               'RewriteRule ^(.*/)?$ /nueva/$1index.html [L]',
               '# Nadie entra directamente en /nueva/',
               'RewriteCond %{ENV:REDIRECT_STATUS} ^$',
               'RewriteRule ^nueva(/|$) - [R=404,L]',
               '</IfModule>',
               '<IfModule mod_headers.c>',
               '<FilesMatch "\\.(css|js|woff2|png|jpe?g|webp|mp4)$">',
               'Header set Cache-Control "public, max-age=2592000"',
               '</FilesMatch>',
               '</IfModule>',
               '# END Reformas APM - web nueva', '']
    escribir('../htaccess-PEGAR-ARRIBA.txt', '\n'.join(reglas))

json.dump(hechas, open(os.path.join(OUT, '..', f'paginas-{MODO}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'{MODO} fase {FASE}: {len(hechas)} páginas en {OUT} | css {len(css)//1024} KB | js {len(js)//1024} KB')
