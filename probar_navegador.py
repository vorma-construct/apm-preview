# -*- coding: utf-8 -*-
"""Abre las páginas en un navegador de verdad (escritorio y móvil): errores, desbordes y capturas."""
import sys, os, subprocess, time, json
from playwright.sync_api import sync_playwright

WEB = sys.argv[1]
CAPTURAS = sys.argv[2]
PAGS = sys.argv[3].split(',') if len(sys.argv) > 3 else None
os.makedirs(CAPTURAS, exist_ok=True)
PUERTO = 8091
srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(PUERTO), '--bind', '127.0.0.1'], cwd=WEB,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1.2)
if PAGS is None:
    PAGS = []
    for raiz, _, fs in os.walk(WEB):
        for f in fs:
            if f.endswith('.html'):
                rel = os.path.relpath(os.path.join(raiz, f), WEB).replace(os.sep, '/')
                PAGS.append('/' + (rel[:-10] if rel.endswith('index.html') else rel))
    PAGS.sort()
res = []
try:
    with sync_playwright() as p:
        nav = p.chromium.launch()
        for nombre, vp, movil in (('escritorio', {'width': 1366, 'height': 900}, False), ('movil', {'width': 390, 'height': 844}, True)):
            ctx = nav.new_context(viewport=vp, is_mobile=movil, has_touch=movil, device_scale_factor=1)
            # lo de fuera (fotos de WordPress, vídeos, Google) no se alcanza desde aquí: se corta para no esperar
            ctx.route('**/*', lambda r: r.continue_() if r.request.url.startswith(f'http://127.0.0.1:{PUERTO}') else r.abort())
            for ruta in PAGS:
                pg = ctx.new_page()
                errores = []
                pg.on('pageerror', lambda e: errores.append('JS: ' + str(e)))
                pg.on('console', lambda m: errores.append('consola: ' + m.text) if m.type == 'error' and 'Failed to load resource' not in m.text and 'net::ERR' not in m.text else None)
                r = pg.goto(f'http://127.0.0.1:{PUERTO}{ruta}', wait_until='load')
                pg.wait_for_timeout(700)
                # bajar hasta abajo para disparar las apariciones
                pg.evaluate("""async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 40)); } window.scrollTo(0, 0); }""")
                pg.wait_for_timeout(500)
                datos = pg.evaluate("""() => ({
                    ancho: document.documentElement.scrollWidth, vista: window.innerWidth,
                    ocultos: [...document.querySelectorAll('[data-reveal]')].filter(e => getComputedStyle(e).opacity === '0').length,
                    h1: document.querySelectorAll('h1').length,
                    tactiles: [...document.querySelectorAll('a,button,input,select,textarea,label[for]')].filter(e => { const b = e.getBoundingClientRect(); return b.width > 0 && b.height > 0 && getComputedStyle(e).visibility !== 'hidden' && (b.height < 24 || b.width < 24); }).length
                })""")
                desborde = datos['ancho'] > datos['vista'] + 1
                if ruta in ('/', '/reforma-integral-en-bilbao/', '/reforma-integral-en-santutxu/', '/blog/', '/trabajos-realizados/', '/contacto/', '/404.html', '/reformas-integrales-bilbao-descubre-el-mejor-servicio-con-reformas-apm/'):
                    nom = (ruta.strip('/').replace('/', '_') or 'portada')[:60]
                    pg.screenshot(path=os.path.join(CAPTURAS, f'{nom}-{nombre}.png'), full_page=False)
                res.append(dict(ruta=ruta, tam=nombre, estado=r.status, errores=errores, desborde=desborde, **datos))
                pg.close()
            ctx.close()
        nav.close()
finally:
    srv.terminate()

malos = [x for x in res if x['estado'] != 200 and not x['ruta'].endswith('404.html') or x['errores'] or x['desborde'] or x['h1'] != 1 or x['ocultos']]
print(f'{len(res)} aperturas ({len(PAGS)} páginas × 2 tamaños)')
for x in malos:
    print('  ✗', x['tam'], x['ruta'], 'estado', x['estado'], '| desborde' if x['desborde'] else '', f"| ancho {x['ancho']}/{x['vista']}" if x['desborde'] else '',
          '| ocultos', x['ocultos'] if x['ocultos'] else '', '| h1', x['h1'], '|', '; '.join(x['errores'])[:300])
print('Sin problemas' if not malos else f'{len(malos)} con algo que mirar')
json.dump(res, open(os.path.join(CAPTURAS, 'resultado.json'), 'w'), ensure_ascii=False, indent=1)
