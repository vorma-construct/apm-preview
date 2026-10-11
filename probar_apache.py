# -*- coding: utf-8 -*-
"""Prueba el .htaccess de verdad en Apache: WordPress simulado debajo y la web nueva en /nueva/."""
import subprocess, re, sys
from datos import *
B = 'http://127.0.0.1:8200'
PRINCIPAL = len(sys.argv) > 1 and sys.argv[1] == 'principal'
def pide(ruta, metodo='GET'):
    r = subprocess.run(['curl', '-s', '-X', metodo, '-D', '-', '-o', '/tmp/claude-0/cuerpo', B + ruta], capture_output=True, text=True)
    cab = r.stdout
    estado = int(re.search(r'HTTP/1\.\d (\d+)', cab).group(1))
    loc = re.search(r'(?im)^Location: (\S+)', cab)
    cc = re.search(r'(?im)^Cache-Control: (.+)$', cab)
    cuerpo = open('/tmp/claude-0/cuerpo', encoding='utf-8', errors='ignore').read()
    origen = 'NUEVA' if '<html lang="es"' in cuerpo else ('WP' if 'WORDPRESS' in cuerpo else ('PANEL' if 'PANEL' in cuerpo else 'otro'))
    t = re.search(r'<title>(.*?)</title>', cuerpo)
    return estado, (loc.group(1) if loc else ''), origen, (t.group(1) if t else ''), (cc.group(1).strip() if cc else ''), cuerpo
fallos = []
def espera(ruta, estado, origen=None, loc=None, metodo='GET', contiene=None):
    e, l, o, t, cc, cuerpo = pide(ruta, metodo)
    ok = e == estado and (origen is None or o == origen) and (loc is None or l.endswith(loc)) and (contiene is None or contiene in cuerpo)
    print(('  ✓ ' if ok else '  ✗ ') + f'{metodo} {ruta:<78} {e} {o:<5} {l} {t[:50]}')
    if not ok: fallos.append(ruta)
    return cc
print('— Las 33 direcciones de hoy')
wp = {r for r, _, _ in SIGUEN_EN_WORDPRESS}
if PRINCIPAL:
    _t = {p['id']: p for p in PAGINAS}
    wp |= {_t[i]['ruta'] for i in REVISION_APM}
for ruta in DIRECCIONES_ACTUALES:
    if ruta == '/reformas-en-bilbao/': espera(ruta, 301, loc='/')
    elif ruta == '/personalizar-cookies/': espera(ruta, 301, loc='/politica-de-cookies/')
    elif ruta in wp: espera(ruta, 200, 'WP')
    else: espera(ruta, 200, 'NUEVA')
print('— Páginas nuevas, recursos y casos especiales')
for ruta in ['/contacto/', '/reforma-de-cocina-en-bilbao/', '/reformas-en-bizkaia/', '/reformas-en-getxo/', '/politica-de-cookies/', '/gracias/']:
    espera(ruta, 200, 'NUEVA')
espera('/contacto', 301, loc='/contacto/')
espera('/reforma-integral-en-bilbao', 301, loc='/reforma-integral-en-bilbao/')
cc = espera('/assets/apm.css', 200)
print('     caché del CSS:', cc)
espera('/assets/fonts/manrope-400.woff2', 200)
espera('/robots.txt', 200, contiene='Sitemap: https://reformasapmbilbao.es/sitemap.xml')
espera('/sitemap.xml', 200, contiene='<urlset')
espera('/sitemap_index.xml', 301, loc='/sitemap.xml')
espera('/post-sitemap.xml', 301, loc='/sitemap.xml')
if not PRINCIPAL:
    espera('/blog/page/2/', 301, loc='/blog/')
    espera('/category/blog/', 301, loc='/blog/')
espera('/aviso-legal-y-politica-de-privacidad/', 301, loc='/aviso-legal/')
espera('/nueva/', 404)
espera('/nueva/index.html', 404)
espera('/nueva/contacto/index.html', 404)
espera('/?origen=wp', 200, 'WP')
espera('/reforma-integral-en-santutxu/?origen=wp', 200, 'WP')
espera('/?s=cocina', 200, 'WP')
espera('/', 200, 'WP', metodo='POST')
espera('/esto-no-existe/', 404, 'WP')
espera('/wp-content/uploads/2019/11/reforma-integral-en-santutxu.jpeg', 200)
espera('/wp-admin/', 200, 'PANEL')
print(f'\nFallos: {len(fallos)}')
sys.exit(1 if fallos else 0)
