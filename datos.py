# -*- coding: utf-8 -*-
"""Datos de la web de Reformas APM: direcciones, títulos, descripciones, fases y correcciones de texto.

Regla de oro de la migración: cada dirección que hoy existe en reformasapmbilbao.es sigue existiendo
en la web nueva, con su misma palabra clave en el título y en el H1. Solo se redirige lo que es un
duplicado claro (la segunda portada /reformas-en-bilbao/, listados y mapas del sitio de WordPress).
"""

DOMINIO = 'https://reformasapmbilbao.es'

# id de la sección en el archivo único  ->  dirección en la web publicada
# fase 0 = migración (lo que se sube el primer día). Fases 1-4 = barrios nuevos, por tandas.
PAGINAS = [
    # --- portada y servicios (mismas direcciones que la web actual) ---
    dict(id='p-index', ruta='/', tipo='portada', fase=0,
         titulo='Reformas en Bilbao | Reforma de Vivienda Integral · Reformas APM',
         desc='Empresa de reformas en Bilbao con oficinas en Santutxu y San Adrián. Reforma integral de vivienda, cocinas, baños y ventanas de PVC. Presupuesto en 24 h.'),
    dict(id='p-reforma-integral-bilbao', ruta='/reforma-integral-en-bilbao/', tipo='servicio', fase=0, miga='Reforma integral en Bilbao',
         desc='Reforma integral de pisos en Bilbao llave en mano: distribución, instalaciones, cocina, baños y acabados con un solo equipo. Pide presupuesto sin compromiso.'),
    dict(id='p-reforma-bano-bilbao', ruta='/reforma-de-bano-en-bilbao/', tipo='servicio', fase=0, miga='Reforma de baño en Bilbao', fecha='2019-08-08',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/08/reforma-de-ba%C3%B1os-en-bilbao.jpg', 'Baño reformado por Reformas APM en la calle Iparraguirre, Bilbao'),
         desc='Reforma de baño en Bilbao: cambio de bañera por plato de ducha, alicatado, sanitarios y mampara. Obra rápida y limpia. Presupuesto sin compromiso en 24 h.'),
    dict(id='p-reforma-cocina-bilbao', ruta='/reforma-de-cocina-en-bilbao/', tipo='servicio', fase=0, miga='Reforma de cocina en Bilbao', nueva=True,
         desc='Reforma de cocina en Bilbao a medida: distribución, muebles, encimera, instalaciones y alicatado. Te asesoramos y te damos presupuesto cerrado en 24 h.'),
    dict(id='p-reforma-parcial-vivienda', ruta='/reforma-parcial-de-vivienda/', tipo='servicio', fase=0, miga='Reforma parcial de vivienda',
         desc='Reforma parcial de vivienda en Bilbao: suelos, pintura, electricidad, armarios o una sola estancia. Mejora tu casa por partes y sin una gran inversión.'),
    dict(id='p-ventanas-pvc-bilbao', ruta='/ventanas-de-pvc/', tipo='servicio', fase=0, miga='Ventanas de PVC',
         desc='Ventanas de PVC en Bilbao a medida con perfiles Deceuninck: más aislamiento térmico y acústico y menos gasto en calefacción. Medición y presupuesto sin compromiso.'),
    dict(id='p-productos', ruta='/productos/', tipo='pagina', fase=0, miga='Productos',
         desc='Productos para tu reforma en Bilbao: armarios empotrados, vestidores a medida, papel pintado, estanterías, decoración y ventanas de PVC Deceuninck.'),
    dict(id='p-trabajos-realizados', ruta='/trabajos-realizados/', tipo='pagina', fase=0, miga='Trabajos realizados',
         desc='Trabajos realizados por Reformas APM en Bilbao y Bizkaia: reformas integrales, cocinas y baños en Santutxu, Miribilla y otros barrios, con sus fotos.'),
    dict(id='p-contacto', ruta='/contacto/', tipo='contacto', fase=0, miga='Contacto', nueva=True,
         desc='Contacta con Reformas APM: oficinas en Karmelo Kalea 15 (Santutxu) y San Adrián Etorbidea 19, Bilbao. Llámanos al 946 033 652 o pide presupuesto online.'),
    # --- zonas (nuevas, ya estaban en la web de 28 páginas) ---
    dict(id='p-reformas-bizkaia', ruta='/reformas-en-bizkaia/', tipo='zona', fase=0, miga='Reformas en Bizkaia', nueva=True,
         desc='Reformas en Bizkaia: trabajamos en Bilbao, Getxo, Barakaldo, Basauri, Sestao y el resto de la provincia. Visita y presupuesto sin compromiso.'),
    dict(id='p-reformas-getxo', ruta='/reformas-en-getxo/', tipo='zona', fase=0, miga='Reformas en Getxo', nueva=True,
         desc='Reformas en Getxo: reformas integrales, cocinas, baños y ventanas en Algorta, Las Arenas y Neguri. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    dict(id='p-reformas-barakaldo', ruta='/reformas-en-barakaldo/', tipo='zona', fase=0, miga='Reformas en Barakaldo', nueva=True,
         desc='Reformas en Barakaldo: reformas integrales de pisos, cocinas y baños en todos los barrios. Visita y presupuesto sin compromiso de Reformas APM.'),
    dict(id='p-reformas-basauri', ruta='/reformas-en-basauri/', tipo='zona', fase=0, miga='Reformas en Basauri', nueva=True,
         desc='Reformas en Basauri: reforma integral de vivienda, cocinas y baños, a un paso de Bilbao. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    dict(id='p-reformas-sestao', ruta='/reformas-en-sestao/', tipo='zona', fase=0, miga='Reformas en Sestao', nueva=True,
         desc='Reformas en Sestao: reformas de pisos, instalaciones, cocinas y baños en vivienda antigua. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    # --- las páginas locales que ya posicionan: misma dirección exacta ---
    dict(id='p-reforma-integral-en-santutxu-index', ruta='/reforma-integral-en-santutxu/', tipo='local', fase=0, miga='Reforma integral en Santutxu', fecha='2019-11-21',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/11/reforma-integral-en-santutxu.jpeg', 'Reforma integral en Santutxu'),
         desc='Reforma integral en Santutxu: cómo planteamos un piso entero del barrio, fases, plazos y qué se cambia. Oficina en Karmelo Kalea 15, a un paso de tu casa.'),
    dict(id='p-reforma-de-cocina-en-santutxu-index', ruta='/reforma-de-cocina-en-santutxu/', tipo='local', fase=0, miga='Reforma de cocina en Santutxu', fecha='2021-04-30',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2021/04/reforma-de-cocina-santutxu-scaled.jpg', 'Reforma de cocina en Santutxu'),
         desc='Reforma de cocina en Santutxu: cocinas a medida para los pisos del barrio, con instalaciones nuevas y presupuesto cerrado. Oficina en Karmelo Kalea 15.'),
    dict(id='p-reforma-de-bano-en-santutxu-index', ruta='/reforma-de-bano-en-santutxu/', tipo='local', fase=0, miga='Reforma de baño en Santutxu', fecha='2021-06-08',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2021/06/ducha-por-banera.jpg', 'Reforma de baño en Santutxu'),
         desc='Reforma de baño en Santutxu: cambio de bañera por plato de ducha y baño completo en los pisos del barrio. Presupuesto sin compromiso. Karmelo Kalea 15.'),
    dict(id='p-nuevo-local-de-reformas-en-santutxu-index', ruta='/nuevo-local-de-reformas-en-santutxu/', tipo='local', fase=0, miga='Reformas en Santutxu', fecha='2022-01-04',
         desc='Reformas en Santutxu: nuestra oficina de Karmelo Kalea 15, junto al metro. Ven a vernos y cuéntanos tu reforma integral o parcial en persona.'),
    dict(id='p-reforma-de-bano-en-miribilla-index', ruta='/reforma-de-bano-en-miribilla/', tipo='local', fase=0, miga='Reforma de baño en Miribilla', fecha='2019-06-25',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/06/WhatsApp-Image-2019-06-25-at-12.52.50-1.jpeg', 'Reforma de baño en Miribilla'),
         desc='Reforma de baño en Miribilla: baños completos y cambio de bañera por ducha en los pisos del barrio. Oficina en San Adrián Etorbidea 19. Presupuesto en 24 h.'),
    # --- blog: cada artículo nuevo va en la dirección del artículo viejo del mismo tema ---
    dict(id='p-blog-index', ruta='/blog/', tipo='blog', fase=0, miga='Blog',
         desc='Blog de Reformas APM: consejos e ideas para reformar tu casa en Bilbao. Baños, cocinas, ventanas de PVC, vestidores y reformas integrales, explicado claro.'),
    dict(id='p-blog-cambiar-banera-por-plato-de-ducha-bilbao', ruta='/cambiar-la-banera-por-un-plato-de-ducha/', tipo='articulo', fase=0, fecha='2024-09-03',
         desc='¿Merece la pena cambiar la bañera por un plato de ducha en Bilbao? Ventajas, precio orientativo, tiempo de obra y consejos para acertar con el cambio.'),
    dict(id='p-blog-vestidor-a-medida', ruta='/vestidor-a-medida/', tipo='articulo', fase=0, fecha='2024-09-03',
         desc='Cómo diseñar un vestidor a medida aunque tengas poco espacio: tipos, ideas, materiales y consejos para aprovechar cada rincón de tu casa en Bilbao.'),
    dict(id='p-blog-reforma-integral-transformar-hogar', ruta='/reforma-integral-en-bilbao-descubre-como-transformar-tu-hogar-con-reformas-apm/', tipo='articulo', fase=0, fecha='2024-05-03',
         desc='Reforma integral en Bilbao paso a paso: qué implica reformar un piso entero, fases, plazos, presupuesto y cómo transformar tu hogar sin sorpresas.'),
    dict(id='p-blog-como-elegir-empresa-de-reformas-bilbao', ruta='/reformas-integrales-bilbao-descubre-el-mejor-servicio-con-reformas-apm/', tipo='articulo', fase=0, fecha='2024-02-03',
         titulo='Reformas Integrales en Bilbao: Cómo Elegir Empresa sin Sorpresas',
         h1='Reformas integrales en Bilbao: cómo elegir una buena empresa',
         desc='Reformas integrales en Bilbao: cómo elegir una buena empresa de reformas, qué mirar en el presupuesto, señales de alarma y qué preguntar antes de firmar.'),
    dict(id='p-blog-ventajas-ventanas-pvc-bilbao', ruta='/ventanas-de-pvc-en-bilbao-descubre-las-ventajas-de-reformas-apm/', tipo='articulo', fase=0, fecha='2024-02-03',
         desc='Ventajas de las ventanas de PVC en Bilbao: aislamiento térmico y acústico, ahorro en calefacción, poco mantenimiento y qué tener en cuenta al cambiarlas.'),
    dict(id='p-blog-ideas-para-reformar-tu-cocina', ruta='/tendencias-2022-para-reformar-tu-cocina/', tipo='articulo', fase=0, fecha='2022-03-10',
         titulo='Ideas y Tendencias para Reformar tu Cocina en Bilbao | Reformas APM',
         h1='Ideas y tendencias para reformar tu cocina',
         desc='Ideas y tendencias para reformar tu cocina en Bilbao: distribución, materiales, iluminación y almacenaje para una cocina práctica y bonita.'),
    dict(id='p-blog-antes-de-una-reforma-integral', ruta='/3-cosas-que-debes-saber-antes-de-hacer-una-reforma-integral/', tipo='articulo', fase=0, fecha='2022-05-09',
         desc='Antes de una reforma integral en Bilbao, ten claras estas 3 cosas: presupuesto realista, permisos y planificación. Te lo explicamos para evitar disgustos.'),
    dict(id='p-blog-pvc-o-aluminio-que-ventana-elegir', ruta='/por-que-elegir-las-ventanas-pvc/', tipo='articulo', fase=0, fecha='2022-05-09',
         titulo='Por Qué Elegir Ventanas de PVC: PVC o Aluminio | Reformas APM',
         h1='Por qué elegir ventanas de PVC: PVC o aluminio',
         desc='Por qué elegir ventanas de PVC: comparamos PVC y aluminio en aislamiento, ruido, mantenimiento y precio para que aciertes con las ventanas de tu casa.'),
    dict(id='p-blog-estilos-de-cocina-que-son-tendencia', ruta='/estilos-de-cocina-que-son-tendencia/', tipo='articulo', fase=0, fecha='2022-03-15',
         desc='Estilos de cocina que son tendencia: nórdico, industrial, mediterráneo y moderno. Ideas para inspirarte y elegir el estilo de tu cocina en Bilbao.'),
    dict(id='p-blog-errores-al-reformar-el-bano', ruta='/reformar-tu-bano-sin-errores/', tipo='articulo', fase=0, fecha='2022-03-15',
         desc='Reformar tu baño sin errores: los 4 fallos más comunes al reformar un baño (ventilación, materiales, distribución e instalaciones) y cómo evitarlos.'),
    # --- legales y utilidades ---
    dict(id='p-aviso-legal', ruta='/aviso-legal/', tipo='legal', fase=0, miga='Aviso legal',
         desc='Aviso legal de Reformas APM (Reformas APMendi), empresa de reformas en Bilbao con oficinas en Karmelo Kalea 15, Santutxu, y San Adrián Etorbidea 19.'),
    dict(id='p-politica-privacidad', ruta='/politica-de-privacidad/', tipo='legal', fase=0, miga='Política de privacidad',
         desc='Política de privacidad de Reformas APM: qué datos recogemos en los formularios de presupuesto, para qué los usamos y cómo ejercer tus derechos.'),
    dict(id='p-politica-cookies', ruta='/politica-de-cookies/', tipo='legal', fase=0, miga='Política de cookies',
         desc='Política de cookies de Reformas APM: qué cookies usa la web, incluido el mapa de Google, y cómo aceptarlas, rechazarlas o cambiar tu elección.'),
    dict(id='p-gracias', ruta='/gracias/', tipo='util', fase=0, miga='Solicitud enviada', noindex=True,
         desc='Hemos recibido tu solicitud de presupuesto. Te llamamos lo antes posible.'),
    dict(id='p-404', ruta='/404.html', tipo='util', fase=0, miga='Página no encontrada', noindex=True,
         desc='Esta página no existe. Desde aquí llegas a todo lo importante de Reformas APM.'),
    # --- barrios de Bilbao: se publican por tandas, después de la migración ---
    dict(id='p-reformas-bilbao-barrios', ruta='/reformas-en-bilbao-por-barrios/', tipo='zona', fase=1, miga='Bilbao por barrios', nueva=True,
         desc='Reformas en Bilbao barrio a barrio: los 8 distritos y sus tipos de vivienda, de Santutxu y Begoña a Deusto, Abando o Rekalde. Elige tu zona.'),
]

BARRIOS = [  # (slug, nombre, fase)
    ('begona', 'Begoña', 1), ('miribilla', 'Miribilla', 1), ('casco-viejo', 'Casco Viejo', 1), ('indautxu', 'Indautxu', 1),
    ('abando', 'Abando', 2), ('deusto', 'Deusto', 2), ('bolueta', 'Bolueta', 2), ('txurdinaga', 'Txurdinaga', 2), ('otxarkoaga', 'Otxarkoaga', 2),
    ('san-francisco-bilbao-la-vieja', 'San Francisco y Bilbao La Vieja', 3), ('atxuri-solokoetxe', 'Atxuri y Solokoetxe', 3),
    ('san-ignacio', 'San Ignacio', 3), ('uribarri', 'Uribarri', 3),
    ('rekalde', 'Rekalde', 4), ('amezola-iralabarri', 'Amezola e Iralabarri', 4), ('basurto', 'Basurto', 4), ('zorroza', 'Zorroza', 4),
]
for slug, nombre, fase in BARRIOS:
    PAGINAS.append(dict(id='p-reformas-' + slug, ruta='/reformas-en-' + slug + '/', tipo='zona', fase=fase,
                        miga='Reformas en ' + nombre, nueva=True,
                        desc=f'Reformas en {nombre} (Bilbao): reformas integrales, cocinas y baños pensadas para los pisos del barrio. Presupuesto cerrado y sin compromiso.'))

# La página «Reformas en Santutxu» nueva NO se publica aparte: competiría con la antigua
# /nuevo-local-de-reformas-en-santutxu/, que es la que Google tiene con ese título. Sus enlaces van ahí.
ALIAS = {'p-reformas-santutxu': 'p-nuevo-local-de-reformas-en-santutxu-index'}

# Artículos viejos que NO tienen versión nueva: se quedan como están, los sigue sirviendo WordPress.
SIGUEN_EN_WORDPRESS = [
    ('/reforma-integral-de-vivienda-en-bilbao/', 'Reforma integral de vivienda en Bilbao', '2020-03-17'),
    ('/reforma-tu-salon-con-estas-ideas-reformas-apm/', 'Ideas para reformar tu salón', '2022-05-09'),
    ('/reforma-integral-de-salon-en-bilbao/', 'Reforma integral de salón en Bilbao', '2021-05-17'),
    ('/ideas-para-integrar-cocina-y-salon/', 'Ideas para integrar cocina y salón', '2021-09-28'),
    ('/cocinas-pequenas-en-bilbao-como-sacarlas-partido/', 'Cocinas pequeñas en Bilbao: cómo sacarles partido', '2021-07-21'),
    ('/estilos-de-cocina-en-bilbao/', 'Estilos de cocina en Bilbao', '2021-05-06'),
]

# Redirecciones 301 (solo duplicados claros)
REDIRECCIONES = [
    (r'^reformas-en-bilbao/?$', '/', 'la segunda portada (hoy hace de Contacto) se une a la portada, que es la que va a por «reformas en Bilbao»'),
    (r'^personalizar-cookies/?$', '/politica-de-cookies/', 'página de ajustes del plugin de cookies'),
    (r'^aviso-legal-y-politica-de-privacidad/?$', '/aviso-legal/', 'enlace del pie de la web vieja'),
    (r'^blog/page/[0-9]+/?$', '/blog/', 'páginas 2, 3… del listado del blog: el blog nuevo lo enseña todo en una'),
    (r'^category/blog/?$', '/blog/', 'categoría única del blog'),
    (r'^(sitemap_index|post-sitemap|page-sitemap|category-sitemap|media-category-sitemap)\.xml$', '/sitemap.xml', 'mapas del sitio de Yoast -> mapa nuevo'),
]

# Las 33 direcciones que tiene hoy la web (mapas del sitio de Yoast, comprobado el 11-oct-2026)
DIRECCIONES_ACTUALES = [
    '/', '/trabajos-realizados/', '/aviso-legal/', '/politica-de-privacidad/', '/personalizar-cookies/',
    '/reforma-parcial-de-vivienda/', '/productos/', '/reforma-integral-en-bilbao/', '/ventanas-de-pvc/', '/reformas-en-bilbao/',
    '/blog/', '/reforma-de-bano-en-miribilla/', '/reforma-de-bano-en-bilbao/', '/reforma-integral-en-santutxu/',
    '/reforma-integral-de-vivienda-en-bilbao/', '/reforma-de-cocina-en-santutxu/', '/estilos-de-cocina-en-bilbao/',
    '/reforma-integral-de-salon-en-bilbao/', '/reforma-de-bano-en-santutxu/', '/cocinas-pequenas-en-bilbao-como-sacarlas-partido/',
    '/ideas-para-integrar-cocina-y-salon/', '/nuevo-local-de-reformas-en-santutxu/', '/tendencias-2022-para-reformar-tu-cocina/',
    '/reformar-tu-bano-sin-errores/', '/estilos-de-cocina-que-son-tendencia/', '/3-cosas-que-debes-saber-antes-de-hacer-una-reforma-integral/',
    '/por-que-elegir-las-ventanas-pvc/', '/reforma-tu-salon-con-estas-ideas-reformas-apm/',
    '/ventanas-de-pvc-en-bilbao-descubre-las-ventajas-de-reformas-apm/', '/reformas-integrales-bilbao-descubre-el-mejor-servicio-con-reformas-apm/',
    '/reforma-integral-en-bilbao-descubre-como-transformar-tu-hogar-con-reformas-apm/', '/vestidor-a-medida/', '/cambiar-la-banera-por-un-plato-de-ducha/',
]

# Palabra clave que lleva hoy cada dirección en su título (para comprobar que la nueva la conserva)
PALABRA_CLAVE_ACTUAL = {
    '/': 'reforma de vivienda', '/reforma-integral-en-bilbao/': 'reforma integral en bilbao',
    '/reforma-parcial-de-vivienda/': 'reforma parcial de vivienda', '/ventanas-de-pvc/': 'ventanas de pvc',
    '/productos/': 'productos', '/trabajos-realizados/': 'trabajos realizados',
    '/reforma-de-bano-en-miribilla/': 'reforma de baño en miribilla', '/reforma-de-bano-en-bilbao/': 'reforma de baño en bilbao',
    '/reforma-integral-en-santutxu/': 'reforma integral en santutxu', '/reforma-de-cocina-en-santutxu/': 'reforma de cocina en santutxu',
    '/reforma-de-bano-en-santutxu/': 'reforma de baño en santutxu', '/nuevo-local-de-reformas-en-santutxu/': 'reformas en santutxu',
    '/tendencias-2022-para-reformar-tu-cocina/': 'reformar tu cocina', '/reformar-tu-bano-sin-errores/': 'reformar tu baño',
    '/estilos-de-cocina-que-son-tendencia/': 'estilos de cocina que son tendencia',
    '/3-cosas-que-debes-saber-antes-de-hacer-una-reforma-integral/': 'antes de',
    '/por-que-elegir-las-ventanas-pvc/': 'por qué elegir ventanas de pvc',
    '/ventanas-de-pvc-en-bilbao-descubre-las-ventajas-de-reformas-apm/': 'ventanas de pvc en bilbao',
    '/reformas-integrales-bilbao-descubre-el-mejor-servicio-con-reformas-apm/': 'reformas integrales en bilbao',
    '/reforma-integral-en-bilbao-descubre-como-transformar-tu-hogar-con-reformas-apm/': 'reforma integral en bilbao',
    '/vestidor-a-medida/': 'vestidor a medida', '/cambiar-la-banera-por-un-plato-de-ducha/': 'cambiar la bañera por un plato de ducha',
    '/blog/': 'blog',
}

# Etiquetas de verificación que lleva hoy la portada real (Search Console, Bing, Yandex)
VERIFICACION = [
    ('google-site-verification', '4pSYw6xTzR6Eaj7yTtDFqXiW2z5LRQZKXbPajpLg3Os'),
    ('msvalidate.01', 'F65B5CFEE157336E679731CCEC189A6B'),
    ('yandex-verification', '182906592dca32dd'),
]

# Vídeos de la portada: primero el archivo propio (carpeta /video/), si no está, el de Higgsfield
VIDEOS = [
    ('apm-obra.mp4', 'https://d8j0ntlcm91z4.cloudfront.net/user_3JVkNd1GnfKqGxO6OaFHjhkWtp2/hf_20260918_210207_07e34844-c3a8-498f-847a-ce828ac2a9e3.mp4'),
    ('apm-cocina.mp4', 'https://d8j0ntlcm91z4.cloudfront.net/user_3JVkNd1GnfKqGxO6OaFHjhkWtp2/hf_20260918_210207_77b5bc2a-de19-4668-a0a6-be2fb422fdf5.mp4'),
    ('apm-bano.mp4', 'https://d8j0ntlcm91z4.cloudfront.net/user_3JVkNd1GnfKqGxO6OaFHjhkWtp2/hf_20260918_210207_784f9573-025f-4955-b1c1-c5e07ede1987.mp4'),
    ('apm-ventanas.mp4', 'https://d8j0ntlcm91z4.cloudfront.net/user_3JVkNd1GnfKqGxO6OaFHjhkWtp2/hf_20260918_210207_c51b8253-f97d-4e2c-acd0-b2666904fec1.mp4'),
]

# --- Afirmaciones sin confirmar que se quitan (APM no ha confirmado los «más de veinte años» ni lo de «familiar») ---
# Si el dueño lo confirma, basta con vaciar esta lista y volver a construir.
QUITAR_AFIRMACIONES = [
    ('Es lo que llevamos haciendo desde hace más de veinte años en Bilbao.', 'Es como trabajamos en cada obra en Bilbao.'),
    ('En Reformas APM llevamos más de veinte años reformando pisos en Bilbao y Bizkaia.', 'En Reformas APM reformamos pisos en Bilbao y Bizkaia, con oficina en Santutxu.'),
    ('Llevamos más de veinte años reformando pisos en Bilbao.', 'Nos dedicamos a reformar pisos en Bilbao.'),
    ('En Reformas APM llevamos más de veinte años haciendo este trabajo en pisos como el tuyo,', 'En Reformas APM hacemos este trabajo en pisos como el tuyo,'),
    ('en Reformas APM llevamos más de veinte años haciendo obras en Bilbao y en Bizkaia,', 'en Reformas APM hacemos obras en Bilbao y en Bizkaia,'),
    ('Llevamos más de veinte años cambiando ventanas en Santutxu, Begoña, Deusto o Rekalde, y lo vemos a diario:', 'Cambiamos ventanas en Santutxu, Begoña, Deusto o Rekalde, y lo vemos a menudo:'),
    ('En veinte años no hemos visto una ventana mala por el material.', 'Rara vez el problema de una ventana es el material.'),
    ('En más de veinte años reformando pisos en Bilbao hemos entrado a arreglar muchos baños', 'Reformando pisos en Bilbao hemos entrado a arreglar muchos baños'),
    ('En Reformas APM llevamos más de veinte años haciendo esto en pisos como el tuyo,', 'En Reformas APM hacemos esto en pisos como el tuyo,'),
    ('Llevamos más de veinte años reformando en Bilbao y en estos portales hemos aprendido algo:', 'Reformando en Bilbao, en estos portales hemos aprendido algo:'),
    ('Somos una empresa de reformas en Indautxu familiar, con más de veinte años de oficio:', 'Somos una empresa de reformas que trabaja en Indautxu:'),
    ('Somos una empresa de reformas en Abando familiar, con más de veinte años de oficio:', 'Somos una empresa de reformas que trabaja en Abando:'),
    ('Somos una empresa de reformas en Zorroza familiar, con más de veinte años de oficio:', 'Somos una empresa de reformas que trabaja en Zorroza:'),
    ('Somos una empresa familiar de reformas con base en Santutxu.', 'Somos una empresa de reformas con base en Santutxu.'),
    ('y llevamos más de veinte años entrando en portales de esta zona.', 'y conocemos bien los portales de esta zona.'),
    ('En Reformas APM llevamos más de veinte años en el barrio, con la oficina y la exposición en Karmelo Kalea 15,', 'En Reformas APM estamos en el barrio, con la oficina en Karmelo Kalea 15,'),
    ('y es también el que más veces hemos desmontado en más de veinte años de oficio.', 'y es también el que más veces hemos desmontado.'),
    ('Llevamos más de veinte años de oficio y buena parte de ese tiempo trabajando en este barrio.', 'Buena parte de nuestro trabajo está en este barrio.'),
    ('Llevamos más de veinte años haciendo baños en Bilbao y tenemos oficina en San Adrián Etorbidea 19,', 'Hacemos baños en Bilbao y tenemos oficina en San Adrián Etorbidea 19,'),
    ('Es la forma que tenemos de trabajar desde hace más de veinte años y nos ha ido bien así.', 'Es nuestra forma de trabajar.'),
    ('Llevamos más de veinte años transformando pisos en Bilbao.', 'Transformamos pisos en Bilbao y toda Bizkaia.'),
    ('Empresa de reformas integrales en Bilbao con más de veinte años transformando viviendas en Santutxu y toda Bizkaia.',
     'Empresa de reformas integrales en Bilbao, con oficinas en Santutxu y San Adrián y trabajo en toda Bizkaia.'),
    ('<span data-count="20" data-pre="+">+20</span></div><div class="l">años de experiencia</div>',
     '<span>Bizkaia</span></div><div class="l">servicio en toda la provincia</div>'),
    ('<div class="n">+20</div><div class="l">años de oficio en Bilbao</div>', '<div class="n">8</div><div class="l">distritos de Bilbao</div>'),
    (' Más de veinte años</div>', ' Dos oficinas en Bilbao</div>'),
]

# Relatos de obras concretas que no se pueden comprobar: se cuentan como caso típico, no como obra real
REENCUADRES = [
    ('Esta página no es un catálogo: cuenta una obra concreta. Una <strong>reforma integral en Santutxu</strong> para una pareja joven que compró un piso del barrio con la distribución original, la de toda la vida. Se reformó por completo, de la entrada a la última toma de corriente, y el movimiento que lo cambió todo fue el más fácil de contar y el más difícil de decidir: eliminar el pasillo y repartir esos metros entre las estancias que de verdad se usan.',
     'Esta página no es un catálogo: cuenta cómo se plantea una <strong>reforma integral en Santutxu</strong> en un piso del barrio con la distribución original, la de toda la vida. Se reforma por completo, de la entrada a la última toma de corriente, y el movimiento que más cambia la casa suele ser el más fácil de contar y el más difícil de decidir: eliminar el pasillo y repartir esos metros entre las estancias que de verdad se usan.'),
    ('En este piso salieron las cuentas: la tabiquería del pasillo era divisoria y se pudo eliminar por completo.',
     'Cuando la tabiquería del pasillo es divisoria, como pasa en muchos pisos del barrio, se puede eliminar por completo.'),
    ('Hace poco terminamos el baño de un cliente del barrio que llevaba años aguantando el suyo tal cual estaba, con la bañera de siempre y sin sitio para nada. Quedó encantado, y no por el azulejo nuevo, sino por lo que ganó en el día a día:',
     'Muchos vecinos del barrio llevan años aguantando su baño tal cual está, con la bañera de siempre y sin sitio para nada. Lo que más se nota después de la reforma no es el azulejo nuevo, sino lo que se gana en el día a día:'),
    ('Esta página cuenta una obra concreta: una reforma de baño en Miribilla que terminó siendo más moderna y, sobre todo, mucho más funcional que la de partida. No era un baño en mal estado. Era un baño correcto, de una promoción relativamente nueva, con todo en su sitio y nada roto. Y aun así se quedaba corto todos los días,',
     'Esta página va de la reforma de baño en Miribilla: cómo dejar un baño más moderno y, sobre todo, mucho más funcional que el de partida. Muchas veces no es un baño en mal estado. Es un baño correcto, de una promoción relativamente nueva, con todo en su sitio y nada roto. Y aun así se queda corto todos los días,'),
]

# Pregunta frecuente con una promesa que APM no ha confirmado (financiación): se quita
QUITAR_BLOQUES = [
    r'<details data-reveal><summary>¿Puedo financiar la reforma\?</summary>.*?</details>',
]

# Trabajos realizados: solo obras que la propia APM ha publicado (con su foto cuando la hay)
TRABAJOS_REALES = [
    ('Reforma integral en Santutxu', 'Santutxu, Bilbao', '/reforma-integral-en-santutxu/',
     'https://reformasapmbilbao.es/wp-content/uploads/2019/11/reforma-integral-en-santutxu.jpeg'),
    ('Reforma de cocina en Santutxu', 'Santutxu, Bilbao', '/reforma-de-cocina-en-santutxu/',
     'https://reformasapmbilbao.es/wp-content/uploads/2021/04/reforma-de-cocina-santutxu-scaled.jpg'),
    ('Reforma de baño en Santutxu', 'Santutxu, Bilbao', '/reforma-de-bano-en-santutxu/',
     'https://reformasapmbilbao.es/wp-content/uploads/2021/06/ducha-por-banera.jpg'),
    ('Reforma de baño en Miribilla', 'Miribilla, Bilbao', '/reforma-de-bano-en-miribilla/',
     'https://reformasapmbilbao.es/wp-content/uploads/2019/06/WhatsApp-Image-2019-06-25-at-12.52.50-1.jpeg'),
    ('Reforma de baño en la calle Iparraguirre', 'Bilbao', '/reforma-de-bano-en-bilbao/',
     'https://reformasapmbilbao.es/wp-content/uploads/2019/08/reforma-de-ba%C3%B1os-en-bilbao.jpg'),
    ('Reforma integral de salón', 'Bilbao', '/reforma-integral-de-salon-en-bilbao/',
     'https://reformasapmbilbao.es/wp-content/uploads/2021/05/reforma-integral-salon-en-bilbao.jpg'),
]
TRABAJOS_SIN_FOTO = ['Miradores en Orduña', 'Reforma de piso en el Casco Viejo', 'Aleros de fachada en Algorta']

NEGOCIO = {
    'nombre': 'Reformas APM', 'alt': 'Reformas APMendi',
    'tel_santutxu': '+34946033652', 'tel_movil': '+34671938614', 'email': 'info@reformasapmbilbao.es',
    'logo': 'https://reformasapmbilbao.es/wp-content/uploads/2021/12/apm-reformas.png',
    # Datos de las dos fichas de Google (comprobados el 11-oct-2026)
    'santutxu': dict(calle='Karmelo Kalea 15', cp='48004', lat=43.2542915, lng=-2.911939),
    'sanadrian': dict(calle='San Adrian Etorbidea 19', cp='48003', lat=43.2481916, lng=-2.93254),
}


# Páginas cuya versión nueva es texto largo escrito con IA y que, en la web real, hoy tienen texto escrito a mano
# (o artículos que ya posicionan). En el paquete «principal» NO se cambian: las sigue sirviendo WordPress tal cual
# hasta que alguien de APM lea la versión nueva, la corrija y le añada fotos y datos suyos (guía de Google, oct-2026).
REVISION_APM = [
    'p-blog-index', 'p-reforma-bano-bilbao',
    'p-reforma-integral-en-santutxu-index', 'p-reforma-de-cocina-en-santutxu-index', 'p-reforma-de-bano-en-santutxu-index',
    'p-nuevo-local-de-reformas-en-santutxu-index', 'p-reforma-de-bano-en-miribilla-index',
    'p-blog-cambiar-banera-por-plato-de-ducha-bilbao', 'p-blog-vestidor-a-medida', 'p-blog-reforma-integral-transformar-hogar',
    'p-blog-como-elegir-empresa-de-reformas-bilbao', 'p-blog-ventajas-ventanas-pvc-bilbao', 'p-blog-ideas-para-reformar-tu-cocina',
    'p-blog-antes-de-una-reforma-integral', 'p-blog-pvc-o-aluminio-que-ventana-elegir', 'p-blog-estilos-de-cocina-que-son-tendencia',
    'p-blog-errores-al-reformar-el-bano',
]
