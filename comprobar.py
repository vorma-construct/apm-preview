# -*- coding: utf-8 -*-
"""Comprueba el paquete de la web antes de subirlo. Uso: python3 comprobar.py <carpeta_web> [prod|preview]"""
import os, re, sys, json, html, glob
from collections import Counter
from datos import *

WEB = sys.argv[1]
MODO = sys.argv[2] if len(sys.argv) > 2 else 'prod'
BASE = '/' if MODO == 'prod' else '/apm-preview/'
fallos, avisos = [], []

def leer(ruta):
    return open(ruta, encoding='utf-8').read()

def fichero_de(url_path):
    """Dirección publicada -> fichero dentro del paquete (o None)."""
    if not url_path.startswith(BASE):
        return None
    rel = url_path[len(BASE):]
    cand = os.path.join(WEB, rel)
    if rel == '' or rel.endswith('/'):
        cand = os.path.join(WEB, rel, 'index.html')
    return cand if os.path.isfile(cand) else None

paginas = {}
for f in glob.glob(os.path.join(WEB, '**', '*.html'), recursive=True):
    rel = os.path.relpath(f, WEB).replace(os.sep, '/')
    ruta = '/' + (rel[:-len('index.html')] if rel.endswith('index.html') else rel)
    paginas[ruta] = leer(f)

wp_rutas = {r for r, _, _ in SIGUEN_EN_WORDPRESS}
redir = [(re.compile(p), d) for p, d, _ in REDIRECCIONES]
def redirige(ruta):
    for rx, d in redir:
        if rx.match(ruta.lstrip('/')):
            return d
    return None

# A) las 33 direcciones de hoy
cobertura = Counter()
for ruta in DIRECCIONES_ACTUALES:
    if ruta in paginas:
        cobertura['página nueva en su misma dirección'] += 1
    elif ruta in wp_rutas:
        cobertura['se queda tal cual (WordPress)'] += 1
    elif redirige(ruta):
        destino = redirige(ruta)
        if destino not in paginas:
            fallos.append(f'{ruta}: redirige a {destino}, que no existe')
        cobertura[f'301 -> {destino}'] += 1
    else:
        fallos.append(f'{ruta}: DESAPARECE (ni página, ni WordPress, ni redirección)')

# B) cada dirección conserva su palabra clave en el título y en el H1 o la entradilla
def norm(t):
    return html.unescape(t).lower()
for ruta, kw in PALABRA_CLAVE_ACTUAL.items():
    if ruta not in paginas:
        continue
    h = paginas[ruta]
    t = norm(re.search(r'<title>(.*?)</title>', h, re.S).group(1))
    h1 = norm(re.sub(r'<[^>]+>', '', re.search(r'<h1[^>]*>(.*?)</h1>', h, re.S).group(1)))
    if kw not in t and kw not in h1:
        fallos.append(f'{ruta}: la palabra clave «{kw}» no está ni en el título ni en el H1 ({t} | {h1})')

# C) enlaces internos y recursos
rotos = Counter()
for ruta, h in paginas.items():
    for attr, url in re.findall(r'\b(href|src|data-lightbox|content)="(/[^"]*)"', h):
        if url.startswith('//'):
            continue
        u = url.split('#')[0].split('?')[0]
        if not u:
            continue
        if MODO == 'prod' and (u.startswith('/wp-content/') or u.startswith('/video/')):
            continue  # fotos de WordPress (se quedan en el alojamiento) y vídeos que se suben aparte
        if fichero_de(u) or u in wp_rutas or redirige(u):
            continue
        rotos[(ruta, url)] += 1
for (ruta, url), n in rotos.items():
    fallos.append(f'enlace roto en {ruta}: {url}')

# D) cada página por dentro
titulos, descs = Counter(), Counter()
for ruta, h in paginas.items():
    n_h1 = len(re.findall(r'<h1\b', h))
    if n_h1 != 1:
        fallos.append(f'{ruta}: {n_h1} H1')
    t = re.search(r'<title>(.*?)</title>', h, re.S).group(1)
    d = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    titulos[t] += 1; descs[d] += 1
    if not (30 <= len(html.unescape(t)) <= 70):
        avisos.append(f'{ruta}: título de {len(html.unescape(t))} caracteres')
    if ruta not in ('/404.html', '/gracias/') and not (110 <= len(html.unescape(d)) <= 165):
        avisos.append(f'{ruta}: descripción de {len(html.unescape(d))} caracteres')
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    if ruta != '/404.html':
        if not canon or canon.group(1) != DOMINIO + ruta:
            fallos.append(f'{ruta}: canonical {canon.group(1) if canon else "falta"}')
    rob = re.search(r'<meta name="robots" content="([^"]+)"', h).group(1)
    if MODO == 'prod':
        quiere_noindex = ruta in ('/404.html', '/gracias/')
        if ('noindex' in rob) != quiere_noindex:
            fallos.append(f'{ruta}: robots «{rob}»')
    elif 'noindex' not in rob:
        fallos.append(f'{ruta}: la vista previa debe ir con noindex')
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            json.loads(m.group(1))
        except Exception as e:
            fallos.append(f'{ruta}: datos estructurados no válidos ({e})')
    for patron, que in [(r'href="#p-', 'enlaces del archivo único (#p-)'), (r'data-title=', 'restos de data-title'),
                        (r'más de veinte años|veinte años de oficio|empresa familiar|en Indautxu familiar', 'afirmación sin confirmar (veinte años / familiar)'),
                        (r'Karmelo[^<]{0,12}48003|Karmelo\+Kalea\+15,\+48003|Kalea%2015%2C%2048003', 'código postal de Karmelo mal (48003)'),
                        (r'gracias\.html', 'enlace a gracias.html'), (r'demo-note', 'aviso de demo'),
                        (r'financiaci[oó]n a medida', 'promesa de financiación'), (r'pareja joven', 'relato de obra sin confirmar'),
                        (r'Entregada en seis semanas', 'trabajo inventado')]:
        if re.search(patron, h):
            fallos.append(f'{ruta}: {que}')
    if MODO == 'prod' and 'apm-preview' in h:
        fallos.append(f'{ruta}: dirección de la vista previa dentro del paquete')
    if ruta == '/':
        for n, v in VERIFICACION:
            if f'<meta name="{n}" content="{v}">' not in h:
                fallos.append(f'portada: falta la verificación {n}')
for t, n in titulos.items():
    if n > 1: fallos.append(f'título repetido {n} veces: {t}')
for d, n in descs.items():
    if n > 1: fallos.append(f'descripción repetida {n} veces: {d}')

# E) mapa del sitio
if MODO == 'prod':
    sm = leer(os.path.join(WEB, 'sitemap.xml'))
    locs = re.findall(r'<loc>([^<]+)</loc>', sm)
    for u in locs:
        ruta = u.replace(DOMINIO, '')
        if ruta not in paginas and ruta not in wp_rutas:
            fallos.append(f'sitemap: {u} no existe')
    for ruta in paginas:
        if ruta not in ('/404.html', '/gracias/') and DOMINIO + ruta not in locs:
            fallos.append(f'sitemap: falta {ruta}')
    print(f'Mapa del sitio: {len(locs)} direcciones')

print(f'Páginas en el paquete: {len(paginas)}')
print('Las 33 direcciones de hoy:')
for k, v in cobertura.items():
    print(f'   {v:>2}  {k}')
print(f'Fallos: {len(fallos)}')
for f in fallos: print('   ✗', f)
print(f'Avisos: {len(avisos)}')
for a in avisos: print('   ·', a)
sys.exit(1 if fallos else 0)
