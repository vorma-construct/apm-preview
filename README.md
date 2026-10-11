# Reformas APM — cómo se construye la web

Esta rama guarda las herramientas, no la web. La web publicada está en la rama `main`.

- `fuente/archivo-unico.html`: la web completa en un solo archivo (la vista previa de septiembre de 2026).
- `revisado/*.json`: los 15 textos reescritos en octubre de 2026 (10 artículos y 5 páginas de Santutxu y Miribilla),
  comprobados uno a uno con sus fuentes. Cada archivo lleva el H1, la entradilla, el cuerpo, las fuentes y lo que
  solo APM puede confirmar (`pendiente_apm`). `construir.py` los pone en su página con la lista de fuentes al final.
- `reglas-redaccion.md`: qué se puede afirmar de APM y qué no, y cómo se escriben los textos.
- `datos-verificados.md`: precios, plazos, trámites de Bilbao, ayudas y datos técnicos, con sus fuentes.
- `datos.py`: direcciones, títulos, descripciones, fases de publicación y correcciones de texto
  (`VERDAD` y `VERDAD_BLOQUES`: lo que APM no ha confirmado sale de toda la web).
- `construir.py`: crea una página por dirección.
  - `python3 construir.py prod 0 salida/prod/nueva` → paquete para subir (fase 0 = migración; 1-4 = municipios y barrios,
    que solo se publican con obra real de APM, fotos y su visto bueno).
  - `python3 construir.py preview 0 salida/preview/apm-preview` → vista previa de GitHub Pages (noindex).
- `comprobar.py`: las 33 direcciones de la web real, palabras clave, enlaces, canonical, datos estructurados,
  frases prohibidas (promesas sin confirmar, datos técnicos mal) y que cada texto revisado está en su página.
- `probar_navegador.py`, `probar_contraste.py`: errores, desbordes en móvil y contraste de todos los textos.
- `probar_apache.py` + `probar_apache_montar.sh`: prueba el `.htaccess` en un Apache con WordPress simulado.
- `LEEME-PRIMERO.txt`: instrucciones de subida que van dentro del paquete.
