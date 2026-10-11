# Reformas APM — cómo se construye la web

Esta rama guarda las herramientas, no la web. La web publicada está en la rama `main`.

- `fuente/archivo-unico.html`: la web completa en un solo archivo (la vista previa de septiembre de 2026).
- `datos.py`: direcciones, títulos, descripciones, fases de publicación y correcciones de texto.
- `construir.py`: crea una página por dirección.
  - `python3 construir.py prod 0 salida/prod/nueva` → paquete para subir (fase 0 = migración; 1-4 = tandas de barrios).
  - `python3 construir.py preview 0 salida/preview/apm-preview` → vista previa de GitHub Pages (noindex).
  - `python3 construir.py prod 0 salida/principal/nueva principal` → solo las páginas principales; las de `REVISION_APM`
    (artículos, páginas de Santutxu y Miribilla, baño en Bilbao) las sigue sirviendo WordPress con su texto de siempre
    hasta que APM las revise. Para publicar una ya revisada, se quita de `REVISION_APM` y se vuelve a construir.
- `comprobar.py`: las 33 direcciones de la web real, palabras clave, enlaces, canonical, datos estructurados.
- `probar_navegador.py`, `probar_contraste.py`: errores, desbordes en móvil y contraste de todos los textos.
- `probar_apache.py` + `probar_apache_montar.sh`: prueba el `.htaccess` en un Apache con WordPress simulado.
- `LEEME-PRIMERO.txt`: instrucciones de subida que van dentro del paquete.
