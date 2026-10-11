# -*- coding: utf-8 -*-
"""Mide el contraste de todos los textos de todas las páginas (letra frente a su fondo real)."""
import sys, os, subprocess, time, json
from playwright.sync_api import sync_playwright

WEB = sys.argv[1]
PUERTO = 8098
srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(PUERTO), '--bind', '127.0.0.1'], cwd=WEB,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
PAGS = []
for raiz, _, fs in os.walk(WEB):
    for f in fs:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(raiz, f), WEB).replace(os.sep, '/')
            PAGS.append('/' + (rel[:-10] if rel.endswith('index.html') else rel))
JS = r"""() => {
  const lum = c => { const [r,g,b] = c.map(v => { v/=255; return v<=.03928? v/12.92 : Math.pow((v+.055)/1.055,2.4) }); return .2126*r+.7152*g+.0722*b };
  const parse = s => { const m = s.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p = m[1].split(',').map(x=>parseFloat(x)); return {c:p.slice(0,3), a: p.length>3? p[3]:1} };
  const mezcla = (arriba, abajo) => arriba.c.map((v,i)=> v*arriba.a + abajo[i]*(1-arriba.a));
  function fondo(el){ // color de fondo efectivo; null si hay imagen o degradado por medio
    const capas=[]; let e=el;
    while(e){ const cs=getComputedStyle(e);
      if(cs.backgroundImage && cs.backgroundImage!=='none') return null;
      if(e.matches && e.matches('.hero, .hero *, .phero, .phero *')) return null;
      const b=parse(cs.backgroundColor); if(b && b.a>0){ capas.push(b); if(b.a>=1) break; }
      e=e.parentElement; }
    let base=[255,255,255]; for(let i=capas.length-1;i>=0;i--) base=mezcla(capas[i],base); return base; }
  const malos=[];
  document.querySelectorAll('p,li,h1,h2,h3,h4,a,span,summary,label,td,th,figcaption,b,strong,em').forEach(el=>{
    const t=[...el.childNodes].filter(n=>n.nodeType===3).map(n=>n.textContent.trim()).join('');
    if(!t) return; const r=el.getBoundingClientRect(); if(r.width===0||r.height===0) return;
    const cs=getComputedStyle(el); if(cs.visibility==='hidden'||parseFloat(cs.opacity)===0) return;
    if(el.closest('.cookiebar,.lightbox,.mobile-nav,.dropdown,[aria-hidden=true]')) return;
    const f=fondo(el); if(!f) return; const col=parse(cs.color); if(!col) return;
    const c=mezcla(col,f); const L1=lum(c), L2=lum(f); const ratio=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
    const grande = parseFloat(cs.fontSize)>=24 || (parseFloat(cs.fontSize)>=18.66 && parseInt(cs.fontWeight)>=700);
    if(ratio < (grande?3:4.5)) malos.push({t:t.slice(0,60), ratio:+ratio.toFixed(2), tag:el.tagName, cls:el.className&&el.className.baseVal===undefined?el.className:''});
  });
  return malos; }"""
total, porpag = 0, {}
try:
    with sync_playwright() as p:
        nav = p.chromium.launch()
        ctx = nav.new_context(viewport={'width': 1280, 'height': 900})
        ctx.route('**/*', lambda r: r.continue_() if r.request.url.startswith(f'http://127.0.0.1:{PUERTO}') else r.abort())
        pg = ctx.new_page()
        for ruta in sorted(PAGS):
            pg.goto(f'http://127.0.0.1:{PUERTO}{ruta}', wait_until='load')
            pg.evaluate("()=>{document.querySelectorAll('[data-reveal]').forEach(e=>{e.classList.add('in');e.style.transition='none'})}")
            pg.wait_for_timeout(150)
            malos = pg.evaluate(JS)
            total += len(malos)
            if malos:
                porpag[ruta] = malos
        nav.close()
finally:
    srv.terminate()
print(f'{len(PAGS)} páginas medidas. Textos con poco contraste: {total}')
for r, ms in porpag.items():
    print(' ', r, len(ms), '|', '; '.join(f"«{m['t']}» {m['ratio']}" for m in ms[:4]))
