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
         titulo='Reforma Integral en Bilbao | Pisos Llave en Mano · Reformas APM',
         desc='Reforma integral de pisos en Bilbao llave en mano: coordinamos todos los gremios, de la distribución a los acabados. Presupuesto detallado y sin compromiso.'),
    dict(id='p-reforma-bano-bilbao', ruta='/reforma-de-bano-en-bilbao/', tipo='servicio', fase=0, miga='Reforma de baño en Bilbao', fecha='2019-08-08',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/08/reforma-de-ba%C3%B1os-en-bilbao.jpg', 'Baño reformado por Reformas APM en la calle Iparraguirre, Bilbao'),
         desc='Reforma de baño en Bilbao: cambio de bañera por plato de ducha, alicatado, sanitarios y mampara. Presupuesto detallado y sin compromiso en 24 h.'),
    dict(id='p-reforma-cocina-bilbao', ruta='/reforma-de-cocina-en-bilbao/', tipo='servicio', fase=0, miga='Reforma de cocina en Bilbao', nueva=True,
         desc='Reforma de cocina en Bilbao a medida: distribución, muebles, encimera, instalaciones y alicatado. Presupuesto detallado y sin compromiso en 24 h.'),
    dict(id='p-reforma-parcial-vivienda', ruta='/reforma-parcial-de-vivienda/', tipo='servicio', fase=0, miga='Reforma parcial de vivienda',
         desc='Reforma parcial de vivienda en Bilbao: suelos, pintura, electricidad, armarios o una sola estancia. Mejora tu casa por partes y sin una gran inversión.'),
    dict(id='p-ventanas-pvc-bilbao', ruta='/ventanas-de-pvc/', tipo='servicio', fase=0, miga='Ventanas de PVC',
         desc='Ventanas de PVC en Bilbao a medida con perfiles Deceuninck: más aislamiento térmico y acústico y menos gasto en calefacción. Medición y presupuesto sin compromiso.'),
    dict(id='p-productos', ruta='/productos/', tipo='pagina', fase=0, miga='Productos',
         desc='Productos para tu reforma en Bilbao: armarios empotrados, vestidores a medida, papel pintado, estanterías, decoración y ventanas de PVC Deceuninck.'),
    dict(id='p-trabajos-realizados', ruta='/trabajos-realizados/', tipo='pagina', fase=0, miga='Trabajos realizados',
         desc='Trabajos realizados por Reformas APM en Bilbao y Bizkaia: reformas integrales, cocinas y baños en Santutxu, Miribilla y otros barrios, con sus fotos.'),
    dict(id='p-contacto', ruta='/contacto/', tipo='contacto', fase=0, miga='Contacto', nueva=True,
         titulo='Contacto y Presupuesto sin Compromiso | Reformas APM Bilbao',
         desc='Contacta con Reformas APM: oficinas en Karmelo Kalea 15 (Santutxu) y San Adrián Etorbidea 19, Bilbao. Llámanos al 946 033 652 o pide presupuesto online.'),
    # --- zonas (nuevas, ya estaban en la web de 28 páginas) ---
    dict(id='p-reformas-bizkaia', ruta='/reformas-en-bizkaia/', tipo='zona', fase=0, miga='Reformas en Bizkaia', nueva=True,
         desc='Reformas en Bizkaia: trabajamos en Bilbao, Getxo, Barakaldo, Basauri, Sestao y el resto de la provincia. Visita y presupuesto sin compromiso.'),
    dict(id='p-reformas-getxo', ruta='/reformas-en-getxo/', tipo='zona', fase=1, miga='Reformas en Getxo', nueva=True,
         desc='Reformas en Getxo: reformas integrales, cocinas, baños y ventanas en Algorta, Las Arenas y Neguri. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    dict(id='p-reformas-barakaldo', ruta='/reformas-en-barakaldo/', tipo='zona', fase=1, miga='Reformas en Barakaldo', nueva=True,
         desc='Reformas en Barakaldo: reformas integrales de pisos, cocinas y baños en todos los barrios. Visita y presupuesto sin compromiso de Reformas APM.'),
    dict(id='p-reformas-basauri', ruta='/reformas-en-basauri/', tipo='zona', fase=1, miga='Reformas en Basauri', nueva=True,
         desc='Reformas en Basauri: reforma integral de vivienda, cocinas y baños, a un paso de Bilbao. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    dict(id='p-reformas-sestao', ruta='/reformas-en-sestao/', tipo='zona', fase=1, miga='Reformas en Sestao', nueva=True,
         desc='Reformas en Sestao: reformas de pisos, instalaciones, cocinas y baños en vivienda antigua. Presupuesto cerrado y sin compromiso de Reformas APM.'),
    # --- las páginas locales que ya posicionan: misma dirección exacta ---
    dict(id='p-reforma-integral-en-santutxu-index', ruta='/reforma-integral-en-santutxu/', tipo='local', fase=0, miga='Reforma integral en Santutxu', fecha='2019-11-21',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/11/reforma-integral-en-santutxu.jpeg', 'Reforma integral en Santutxu'),
         desc='Reforma integral en Santutxu: qué incluye en un piso del barrio, fases, plazo y precio orientativos y trámites en Bilbao. Oficina en Karmelo Kalea 15.'),
    dict(id='p-reforma-de-cocina-en-santutxu-index', ruta='/reforma-de-cocina-en-santutxu/', tipo='local', fase=0, miga='Reforma de cocina en Santutxu', fecha='2021-04-30',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2021/04/reforma-de-cocina-santutxu-scaled.jpg', 'Reforma de cocina en Santutxu'),
         desc='Reforma de cocina en Santutxu: qué se suele cambiar en las cocinas del barrio, trámites en Bilbao, precio orientativo y plazo. Oficina en Karmelo Kalea 15.'),
    dict(id='p-reforma-de-bano-en-santutxu-index', ruta='/reforma-de-bano-en-santutxu/', tipo='local', fase=0, miga='Reforma de baño en Santutxu', fecha='2021-06-08',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2021/06/ducha-por-banera.jpg', 'Reforma de baño en Santutxu'),
         desc='Reforma de baño en Santutxu: cambio de bañera por plato de ducha y baño completo en los pisos del barrio. Presupuesto sin compromiso. Karmelo Kalea 15.'),
    dict(id='p-nuevo-local-de-reformas-en-santutxu-index', ruta='/nuevo-local-de-reformas-en-santutxu/', tipo='local', fase=0, miga='Reformas en Santutxu', fecha='2022-01-04',
         desc='Reformas en Santutxu: nuestra oficina en Karmelo Kalea 15, en pleno centro del barrio. Qué hacemos, horario, teléfonos y qué traer para pedir presupuesto.'),
    dict(id='p-reforma-de-bano-en-miribilla-index', ruta='/reforma-de-bano-en-miribilla/', tipo='local', fase=0, miga='Reforma de baño en Miribilla', fecha='2019-06-25',
         foto=('https://reformasapmbilbao.es/wp-content/uploads/2019/06/WhatsApp-Image-2019-06-25-at-12.52.50-1.jpeg', 'Reforma de baño en Miribilla'),
         desc='Reforma de baño en Miribilla: baño completo o cambio de bañera por ducha, cómo ajustar el presupuesto y trámites. Oficina en San Adrián Etorbidea 19.'),
    # --- blog: cada artículo nuevo va en la dirección del artículo viejo del mismo tema ---
    dict(id='p-blog-index', ruta='/blog/', tipo='blog', fase=0, miga='Blog',
         desc='Blog de Reformas APM: consejos e ideas para reformar tu casa en Bilbao. Baños, cocinas, ventanas de PVC, vestidores y reformas integrales, explicado claro.'),
    dict(id='p-blog-cambiar-banera-por-plato-de-ducha-bilbao', ruta='/cambiar-la-banera-por-un-plato-de-ducha/', tipo='articulo', fase=0, fecha='2024-09-03',
         desc='¿Merece la pena cambiar la bañera por un plato de ducha en Bilbao? Ventajas, precio orientativo, tiempo de obra y consejos para acertar con el cambio.'),
    dict(id='p-blog-vestidor-a-medida', ruta='/vestidor-a-medida/', tipo='articulo', fase=0, fecha='2024-09-03',
         desc='Cómo diseñar un vestidor a medida aunque tengas poco espacio: tipos, ideas, materiales y consejos para aprovechar cada rincón de tu casa en Bilbao.'),
    dict(id='p-blog-reforma-integral-transformar-hogar', ruta='/reforma-integral-en-bilbao-descubre-como-transformar-tu-hogar-con-reformas-apm/', tipo='articulo', fase=0, fecha='2024-05-03',
         desc='Reforma integral en Bilbao fase a fase: qué se decide antes de empezar, en qué orden entra cada gremio, cuánto suele durar y cómo se entrega la obra.'),
    dict(id='p-blog-como-elegir-empresa-de-reformas-bilbao', ruta='/reformas-integrales-bilbao-descubre-el-mejor-servicio-con-reformas-apm/', tipo='articulo', fase=0, fecha='2024-02-03',
         titulo='Reformas Integrales en Bilbao: Cómo Elegir Empresa sin Sorpresas',
         h1='Reformas integrales en Bilbao: cómo elegir una buena empresa',
         desc='Reformas integrales en Bilbao: cómo elegir una buena empresa de reformas, qué mirar en el presupuesto, señales de alarma y qué preguntar antes de firmar.'),
    dict(id='p-blog-ventajas-ventanas-pvc-bilbao', ruta='/ventanas-de-pvc-en-bilbao-descubre-las-ventajas-de-reformas-apm/', tipo='articulo', fase=0, fecha='2024-02-03',
         desc='Ventajas de las ventanas de PVC en Bilbao con datos del IDAE y del Código Técnico: aislamiento, ruido, condensación, mantenimiento, precio y ayudas.'),
    dict(id='p-blog-ideas-para-reformar-tu-cocina', ruta='/tendencias-2022-para-reformar-tu-cocina/', tipo='articulo', fase=0, fecha='2022-03-10',
         titulo='Ideas y Tendencias para Reformar tu Cocina en Bilbao | Reformas APM',
         h1='Ideas y tendencias para reformar tu cocina',
         desc='Ideas y tendencias para reformar tu cocina en Bilbao: distribución, materiales, iluminación y almacenaje para una cocina práctica y bonita.'),
    dict(id='p-blog-antes-de-una-reforma-integral', ruta='/3-cosas-que-debes-saber-antes-de-hacer-una-reforma-integral/', tipo='articulo', fase=0, fecha='2022-05-09',
         desc='Antes de hacer una reforma integral en Bilbao: presupuesto realista con ICIO e imprevistos, comunicación previa o licencia, ayudas y cómo planificar la obra.'),
    dict(id='p-blog-pvc-o-aluminio-que-ventana-elegir', ruta='/por-que-elegir-las-ventanas-pvc/', tipo='articulo', fase=0, fecha='2022-05-09',
         titulo='Por Qué Elegir Ventanas de PVC: PVC o Aluminio | Reformas APM',
         h1='Por qué elegir ventanas de PVC: PVC o aluminio',
         desc='Por qué elegir ventanas de PVC: comparamos PVC y aluminio en aislamiento, ruido, mantenimiento y precio para que aciertes con las ventanas de tu casa.'),
    dict(id='p-blog-estilos-de-cocina-que-son-tendencia', ruta='/estilos-de-cocina-que-son-tendencia/', tipo='articulo', fase=0, fecha='2022-03-15',
         titulo='Estilos de Cocina que son Tendencia | Ideas para tu Reforma · APM',
         desc='Estilos de cocina que son tendencia: nórdico, industrial, mediterráneo, moderno y rústico actual. Materiales, colores y qué cuidar en cada uno.'),
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


# ======================================================================================================
# REVISIÓN DE OCTUBRE DE 2026: que la web diga solo lo que es verdad (guía de Google del 1-2 oct. 2026)
# ======================================================================================================
REVISADO_EN = 'octubre de 2026'   # los 15 textos reescritos y comprobados con fuentes (carpeta revisado/)

# Fichas de Google de las dos oficinas (para que cualquiera lea las opiniones)
GOOGLE_SANTUTXU = 'https://www.google.com/maps/search/?api=1&amp;query=Reformas%20APM%20Santutxu&amp;query_place_id=ChIJw6Dkx61PTg0RC7qVFo_lG1Y'
GOOGLE_SANADRIAN = 'https://www.google.com/maps/search/?api=1&amp;query=Reformas%20APM%20San%20Adri%C3%A1n&amp;query_place_id=ChIJOZUwQblPTg0RDFdM1kEzcLs'

def _svg(dentro):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round" >' + dentro + '</svg>')
ICONO = {
    'casa': _svg('<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M9 21v-6h6v6"/>'),
    'doc': _svg('<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Z"/><path d="M14 3v6h6M8 13h8M8 17h6"/>'),
    'llave': _svg('<path d="M12 2 4 5v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V5Z"/><path d="m9 12 2 2 4-4"/>'),
    'ventana': _svg('<rect x="4" y="3" width="16" height="18" rx="1.5"/><path d="M12 3v18M4 12h16"/>'),
    'foto': _svg('<path d="M4 7h3l2-2h6l2 2h3v12H4Z"/><circle cx="12" cy="13" r="3.5"/>'),
    'estrella': _svg('<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9Z"/>'),
}
_OPINIONES = (f'Lee lo que dicen los clientes en nuestras fichas de Google de <a href="{GOOGLE_SANTUTXU}" target="_blank" rel="noopener">Santutxu</a> '
              f'y de <a href="{GOOGLE_SANADRIAN}" target="_blank" rel="noopener">San Adrián</a>.')
_OFICINAS = 'Karmelo Kalea 15, en pleno centro de Santutxu, y San Adrián Etorbidea 19, junto a Miribilla.'
_PRESUPUESTO = 'Detallado, en 24 horas desde que vemos tu vivienda.'

def _feat(ic, h, p):
    return f'<div class="feat" data-reveal><div class="feat__ic">{ICONO[ic]}</div><div><h4>{h}</h4><p>{p}</p></div></div>'
def _quote(ic, h, p):
    return (f'<div class="quote" data-reveal><div class="feat__ic" style="margin-bottom:1rem">{ICONO[ic]}</div>\n'
            f'        <h3 style="font-size:1.14rem;margin-bottom:.5rem">{h}</h3><p style="margin:0">{p}</p></div>')

# «Por qué Reformas APM» (portada y Bizkaia): antes eran promesas (precio cerrado, plazos, oficios propios, financiación…)
BLOQUE_POR_QUE = ('<section class="section"><div class="container">\n'
    '      <div class="shead center" data-reveal><span class="kicker">Por qué Reformas APM</span>\n'
    '        <h2>Lo que puedes comprobar antes de llamarnos</h2>\n'
    '        <p class="lead">Sin promesas: son cosas que puedes ver por ti mismo.</p></div>\n'
    '      <div class="grid grid--3 mt-3">'
    + _feat('casa', 'Dos oficinas en Bilbao', _OFICINAS + ' Puedes pasar a contarnos tu obra.')
    + _feat('doc', 'Presupuesto sin compromiso', _PRESUPUESTO)
    + _feat('llave', 'Llave en mano', 'En la reforma integral coordinamos todos los gremios de principio a fin.')
    + _feat('ventana', 'Ventanas Deceuninck', 'Instalamos ventanas de PVC de la marca Deceuninck, hechas a medida.')
    + _feat('foto', 'Obras con fotos', 'Mira reformas que hemos hecho en Santutxu, en Miribilla o en la calle Iparraguirre en <a href="#p-trabajos-realizados">trabajos realizados</a>.')
    + _feat('estrella', 'Opiniones en Google', _OPINIONES)
    + '</div>\n    </div></section>')

# «Tres compromisos, por escrito» (presupuesto cerrado, plazos por escrito, garantía por escrito): se cambia por esto
BLOQUE_COMPROBAR = ('<section class="section section--paper2 comprobar"><div class="container">\n'
    '      <div class="shead center" data-reveal><span class="kicker">Antes de llamarnos</span>\n'
    '        <h2>Lo que puedes comprobar</h2>\n'
    '        <p class="lead">Antes de elegir empresa de reformas conviene saber quién es. Esto lo puedes ver por ti mismo.</p></div>\n'
    '      <div class="quotes mt-3">'
    + _quote('casa', 'Dos oficinas en Bilbao', _OFICINAS)
    + _quote('doc', 'Presupuesto sin compromiso', _PRESUPUESTO)
    + _quote('estrella', 'Opiniones en Google', _OPINIONES)
    + '</div>\n    </div></section>')

# Bloques enteros (expresión regular -> sustituto)
VERDAD_BLOQUES = [
    (r'<section class="section"><div class="container">\s*<div class="shead center" data-reveal><span class="kicker">Por qué Reformas APM</span>.*?</section>', BLOQUE_POR_QUE),
    (r'<section class="section section--paper2"><div class="container">\s*<div class="shead center" data-reveal><span class="kicker">Nuestra palabra</span>.*?</section>', BLOQUE_COMPROBAR),
    (r'te llamaremos\s+en <strong style="color:#fff">menos de 24 horas laborables</strong> para concretar la visita\.', 'te llamaremos lo antes posible para concretar la visita.'),
    (r'<h4>Presupuesto cerrado</h4>\s*<p>Recibes el presupuesto detallado por partidas en 24–48 h\. El precio que se firma es el que se paga\.</p>',
     '<h4>Presupuesto detallado</h4>\n      <p>Te lo damos en 24 horas desde que vemos la vivienda.</p>'),
    (r'<div class="callout"><p>(Este es un texto orientativo|Texto orientativo y simplificado|Si se instala Google Analytics).*?</div>', ''),
]

# Frases sueltas (texto exacto -> texto nuevo). Lo que no se puede comprobar (presupuesto cerrado, gratis, garantía por
# escrito, equipo propio, plazos por escrito, financiación, exposición y muestras, datos técnicos mal) sale de la web.
VERDAD = [
    # --- botones y cromo común ---
    ('Pedir presupuesto gratis', 'Pedir presupuesto'),
    ('Presupuesto gratis en 24 h', 'Pedir presupuesto'),
    ('>Presupuesto gratis</a>', '>Pedir presupuesto</a>'),
    ('<span>Presupuesto gratis</span>', '<span>Presupuesto</span>'),
    ('presupuesto cerrado, gratis y sin compromiso', 'presupuesto detallado y sin compromiso'),
    ('presupuesto cerrado y sin compromiso', 'presupuesto detallado y sin compromiso'),
    ('Trato directo, presupuesto cerrado y obra garantizada.', 'Presupuesto detallado y sin compromiso.'),
    # --- «Cómo trabajamos» (se repite en muchas páginas) ---
    ('<p class="lead">Sin subcontratas descontroladas ni sobrecostes. Tú tienes un único interlocutor de principio a fin.</p>',
     '<p class="lead">Así es una reforma con nosotros, de la primera visita a la entrega.</p>'),
    ('<h4>Visita y medición</h4><p>Vamos a tu casa, tomamos medidas y escuchamos qué necesitas. Sin coste y sin compromiso.</p>',
     '<h4>Visita y medición</h4><p>Vamos a tu casa, vemos cómo está la vivienda, tomamos medidas y escuchamos qué necesitas.</p>'),
    ('<h4>Presupuesto cerrado</h4><p>Recibes un presupuesto detallado y por partidas en 24–48 h. El precio es el que se firma.</p>',
     '<h4>Presupuesto detallado</h4><p>Te lo damos en 24 horas desde que vemos la vivienda. Sin compromiso.</p>'),
    ('<p>Un solo equipo coordina albañilería, fontanería, electricidad, carpintería y pintura.</p>',
     '<p>Coordinamos todos los gremios: albañilería, fontanería, electricidad, carpintería y pintura.</p>'),
    ('<h4>Entrega y garantía</h4><p>Te entregamos la reforma limpia y rematada, con garantía por escrito y postventa cercana.</p>',
     '<h4>Entrega</h4><p>Te entregamos la obra terminada y lista para usar.</p>'),
    # --- tarjetas de las páginas del barrio ---
    ('<h2>Este mismo trabajo, barrio a barrio</h2><p class="lead">Si vives en Santutxu o en Miribilla, aquí te contamos cómo son estas obras en tu tipo de piso.</p>',
     '<h2>Este mismo trabajo, en el barrio</h2><p class="lead">Hemos hecho obras así en Santutxu y en Miribilla. Aquí te contamos cómo se plantean en los pisos de esos barrios.</p>'),
    ('Cómo trabajamos un piso entero en Santutxu: fases, plazos y qué se cambia en cada una.', 'Qué incluye en un piso del barrio, fases, plazo y precio orientativos, y trámites.'),
    ('Distribuciones que funcionan en las cocinas estrechas del barrio y qué cuesta cada opción.', 'Qué se suele cambiar en las cocinas del barrio, trámites, precio y plazo.'),
    ('Cambiar la bañera por ducha, bajantes antiguos y baños de 3 m²: lo que nos encontramos aquí.', 'Cambiar la bañera por un plato de ducha o renovar el baño entero: qué se hace y cuánto cuesta.'),
    ('Los baños de la promoción de Miribilla y cómo se personalizan sin tocar la estructura.', 'Baño completo o solo la ducha, y cómo ajustar el presupuesto.'),
    ('Karmelo Kalea 15: pásate a ver muestras de materiales y a contarnos tu obra en persona.', 'Karmelo Kalea 15: horario, teléfonos y qué traer para pedir presupuesto.'),
    # --- portada ---
    ('<h1>Reformas integrales en Bilbao que <em>cumplen plazos y presupuesto</em></h1>', '<h1>Reformas integrales en Bilbao, <em>llave en mano</em></h1>'),
    ('Un solo equipo, precio cerrado por escrito y obra garantizada. Sin sorpresas ni sobrecostes.',
     'Coordinamos todos los gremios de principio a fin y te damos un presupuesto detallado y sin compromiso.'),
    (' Presupuesto cerrado</div>', ' Presupuesto sin compromiso</div>'),
    (' Obra garantizada</div>', ' Servicio en toda Bizkaia</div>'),
    ('<span class="qcard__tag">Gratis · 24 h</span>', '<span class="qcard__tag">Sin compromiso</span>'),
    ('<h3>Calcula tu reforma</h3>', '<h3>Pide tu presupuesto</h3>'),
    ('<p>Dinos qué quieres reformar y te llamamos con un precio orientativo.</p>', '<p>Dinos qué quieres reformar y te llamamos para hablarlo.</p>'),
    ('<h2>Todo tipo de reformas, un único responsable</h2>', '<h2>Todo tipo de reformas, llave en mano</h2>'),
    ('Nos encargamos de todo —albañilería, fontanería, electricidad, carpintería y pintura— para que tú solo tengas que disfrutar del resultado.',
     'Coordinamos todos los gremios —albañilería, fontanería, electricidad, carpintería y pintura— de principio a fin.'),
    ('Cocinas funcionales y bonitas, con muebles a medida, electrodomésticos y encimeras de primeras marcas.',
     'Cocinas a medida: distribución, muebles, encimera, electrodomésticos e instalaciones.'),
    ('Cambiamos tu bañera por un plato de ducha y renovamos el baño completo en pocos días.', 'Cambiamos tu bañera por un plato de ducha o renovamos el baño completo.'),
    ('Ventanas de PVC a medida que aíslan del frío y del ruido y bajan tu factura de calefacción.', 'Ventanas de PVC Deceuninck a medida, para aislar mejor del frío y del ruido.'),
    ('<h2>Una empresa de barrio con oficio de verdad</h2>', '<h2>Una empresa de reformas con oficina en el barrio</h2>'),
    ('Nos conocen por hacer las cosas bien: presupuesto claro, plazos que se cumplen y un trato cercano que no encontrarás en las grandes constructoras.',
     'Tenemos la oficina en Karmelo Kalea 15, en pleno centro del barrio, y otra en San Adrián Etorbidea 19, junto a Miribilla.'),
    ('<span>Presupuesto cerrado y detallado por partidas, sin sorpresas</span>', '<span>Presupuesto detallado y sin compromiso</span>'),
    ('<span>Un único interlocutor de principio a fin de la obra</span>', '<span>Coordinamos todos los gremios de principio a fin</span>'),
    ('<span>Oficios propios con años trabajando juntos</span>', '<span>Reformas integrales y parciales, cocinas, baños y ventanas</span>'),
    ('<span>Garantía por escrito y postventa cercana</span>', '<span>Servicio en toda Bizkaia</span>'),
    ('<div class="l">oficinas propias</div>', '<div class="l">oficinas en Bilbao</div>'),
    ('<h2>Las obras que más nos piden en el barrio</h2><p class="lead">Llevamos años reformando en Santutxu y en Miribilla. Aquí tienes el detalle de cada tipo de obra, con lo que nos encontramos de verdad en estos pisos.</p>',
     '<h2>Obras en el barrio, explicadas una a una</h2><p class="lead">Hemos hecho reformas en Santutxu y en Miribilla. Aquí tienes cada tipo de obra: qué se suele hacer, precio orientativo y trámites.</p>'),
    ('Nuestra base está en Santutxu, pero reformamos en todos los barrios de Bilbao y en los municipios de alrededor. Consulta tu zona:',
     'Nuestra base está en Santutxu, y trabajamos en todo Bilbao y en el resto de Bizkaia.'),
    ('Lo mejor es que vengamos a verlo: te damos un presupuesto cerrado y por partidas, sin compromiso, en 24 horas.',
     'Es un precio orientativo de mercado, con calidades medias. Para tu piso, vamos a verlo y te damos un presupuesto detallado y sin compromiso en 24 horas.'),
    ('<summary>¿El presupuesto tiene algún coste?</summary><div class="a">No. La visita, la toma de medidas y el presupuesto son totalmente gratis y sin ningún compromiso.</div>',
     '<summary>¿Pedir presupuesto me compromete a algo?</summary><div class="a">No. El presupuesto es sin compromiso: lo revisas con calma y decides.</div>'),
    ('Un baño puede estar en una o dos semanas y una reforma integral de un piso medio entre cuatro y ocho semanas. Te damos los plazos por escrito antes de empezar.',
     'Como referencia, un baño completo suele llevar una o dos semanas de obra, y la reforma integral de un piso de 60 a 80 m², de seis a diez semanas. Son plazos habituales: el de tu obra depende de lo que haya que hacer.'),
    # --- reforma integral ---
    ('<p>Renovamos tu vivienda de arriba a abajo con un presupuesto cerrado y un único responsable de la obra. Reforma integral llave en mano en Bilbao y toda Bizkaia.</p>',
     '<p>Renovamos tu vivienda de arriba abajo y coordinamos todos los gremios de principio a fin. Reforma integral llave en mano en Bilbao y toda Bizkaia.</p>'),
    ('<h2>Tu piso nuevo sin mover un dedo</h2>', '<h2>Tu piso entero, llave en mano</h2>'),
    ('Nos encargamos del proyecto, las licencias, la obra y los acabados. Tú te despreocupas y nosotros te entregamos las llaves de un hogar renovado.',
     'Coordinamos todos los gremios de principio a fin, de la nueva distribución a los acabados, y te entregamos la vivienda lista para entrar a vivir.'),
    ('<span>Cocina y baños completos con materiales de primera</span>', '<span>Cocina y baños completos</span>'),
    ('<div class="n">4–8</div><div class="l">semanas de media</div>', '<div class="n">6–10</div><div class="l">semanas en un piso de 60–80 m²</div>'),
    ('Derribos, tabiquería, solados y alicatados ejecutados por nuestros propios oficiales.', 'Derribos, tabiquería, solados y alicatados.'),
    ('Electricidad, fontanería, calefacción y domótica al día, con sus boletines y garantías.', 'Electricidad, fontanería y calefacción nuevas, según la normativa.'),
    ('Diseñamos y montamos cocina y baños completos, con muebles y sanitarios de primeras marcas.', 'Cocina y baños completos: distribución, muebles, sanitarios y alicatado.'),
    ('Puertas, armarios y ventanas de PVC o aluminio para un mejor aislamiento.', 'Puertas, armarios empotrados y ventanas de PVC Deceuninck.'),
    ('Pintura, suelos, iluminación y una entrega final limpia y lista para vivir.', 'Pintura, suelos e iluminación, hasta dejar la vivienda lista para entrar a vivir.'),
    ('Te damos un presupuesto cerrado y por partidas tras visitar tu vivienda, gratis y sin compromiso.', 'Para tu piso, te damos un presupuesto detallado y sin compromiso después de verlo.'),
    ('Para una reforma integral suele hacer falta comunicación previa o licencia según el ayuntamiento y si tocas distribución o estructura. Nosotros nos encargamos de toda la tramitación por ti.',
     'En Bilbao, las obras interiores sencillas van por comunicación previa, pero si cambias la distribución o tocas la estructura o la fachada hace falta licencia de obra menor. Además se paga el ICIO, el 5 % del coste de ejecución material. En otros municipios las reglas cambian. Te decimos qué trámite corresponde a tu obra cuando la vemos.'),
    ('En una reforma integral no es lo recomendable, porque se interviene en toda la vivienda. Muchos clientes aprovechan para hacerla antes de mudarse. Si necesitas vivir en ella, lo organizamos por fases.',
     'No es lo recomendable: habrá días sin agua, sin baño o sin cocina, y polvo en toda la casa. Lo práctico es hacerla antes de mudarte o buscar dónde vivir esas semanas.'),
    ('Un piso medio suele estar listo en cuatro a ocho semanas, según el alcance. Te entregamos un calendario por escrito antes de empezar y te informamos de cada avance.',
     'Lo habitual son de seis a diez semanas de obra para un piso de 60 a 80 m², y más si se redistribuye o el piso es mayor.'),
    ('<details data-reveal><summary>¿Qué garantía tiene la reforma?</summary><div class="a">Todos nuestros trabajos van con garantía por escrito y postventa. Si algo no queda a tu gusto, volvemos.</div></details>', ''),
    # --- reforma de baño ---
    ('<p>Renovamos tu baño completo o cambiamos la bañera por un plato de ducha en pocos días, con el mínimo desorden. Baños cómodos, seguros y con acabados que enamoran.</p>',
     '<p>Renovamos tu baño completo o cambiamos la bañera por un plato de ducha. Baños más cómodos y seguros, con presupuesto detallado y sin compromiso.</p>'),
    ('<h2>Un baño nuevo en cuestión de días</h2>', '<h2>Un baño nuevo, más cómodo y seguro</h2>'),
    ('Renovamos sanitarios, grifería, alicatado, mampara y muebles, dejándolo impecable y listo para usar.', 'Renovamos sanitarios, grifería, alicatado, mampara y muebles.'),
    ('Renovamos tuberías, desagües y grifería para olvidarte de goteras y averías.', 'Renovamos tuberías, desagües y grifería, con la pendiente que marca el Código Técnico.'),
    ('Cambiar solo la bañera por un plato de ducha puede ser bastante más económico. Te damos precio cerrado sin compromiso.',
     'Cambiar solo la bañera por un plato de ducha suele costar entre 900 y 2.000 €. Son precios orientativos con calidades medias: el de tu baño te lo damos en un presupuesto detallado y sin compromiso.'),
    ('El cambio de bañera por plato de ducha puede hacerse en pocos días.', 'El cambio de bañera por plato de ducha suele llevar de uno a tres días.'),
    ('Menos de lo que parece. Lo hacemos con el mínimo polvo y desorden, protegiendo el resto de la casa, y lo dejamos todo limpio al terminar.',
     'Menos de lo que parece: lo habitual es que dure de uno a tres días. Lo tienes paso a paso en nuestra <a href="#p-blog-cambiar-banera-por-plato-de-ducha-bilbao">guía para cambiar la bañera por un plato de ducha</a>.'),
    ('Sí. Instalamos platos antideslizantes, asideros, duchas a ras de suelo y grifería termostática para un baño seguro y accesible.',
     'Sí: un plato antideslizante y a ras de suelo, barras de apoyo bien ancladas y un grifo termostático hacen el baño más seguro.'),
    # --- reforma de cocina ---
    ('<p>Diseñamos y reformamos tu cocina de principio a fin: muebles a medida, encimeras, electrodomésticos, fontanería y electricidad. Una cocina bonita y práctica, hecha para durar.</p>',
     '<p>Reformamos tu cocina de principio a fin: muebles a medida, encimera, electrodomésticos, fontanería y electricidad.</p>'),
    ('Nos ocupamos de todo el proceso —del derribo al último tirador— para que tu cocina quede perfecta y funcione de maravilla.', 'Coordinamos todo el proceso, del derribo al último tirador.'),
    ('<span>Encimeras de cuarzo, porcelánico o Silestone</span>', '<span>Encimeras de cuarzo, porcelánico o laminado</span>'),
    ('<span>Electrodomésticos de primeras marcas y zona de aguas nueva</span>', '<span>Electrodomésticos y zona de aguas nueva</span>'),
    ('<div class="n">2–3</div><div class="l">semanas</div>', '<div class="n">3–4</div><div class="l">semanas de obra</div>'),
    ('Una reforma de cocina en Bilbao suele ir de 6.000 a 15.000 € según el tamaño, los muebles y los electrodomésticos. Te damos un presupuesto cerrado tras medir tu cocina, sin compromiso.',
     'Como referencia orientativa, una cocina completa con muebles y electrodomésticos de gama media cuesta entre 6.000 y 15.000 €. El precio de la tuya te lo damos en un presupuesto detallado y sin compromiso, después de verla.'),
    ('Lo habitual es entre dos y tres semanas, dependiendo de si hay que cambiar distribución o instalaciones. Te damos los plazos por escrito.',
     'Lo habitual son de tres a cuatro semanas de obra. Los muebles a medida se encargan antes de empezar, porque tardan en fabricarse.'),
    ('En muchos pisos sí, siempre que no sea un muro de carga o previo estudio si lo es. Te asesoramos sobre lo que se puede hacer y cómo quedaría.',
     'En muchos pisos sí. Si la pared es de carga, antes hace falta el estudio de un técnico. Y en Bilbao, cambiar la distribución pide licencia de obra menor.'),
    ('<summary>¿Incluís los electrodomésticos?</summary><div class="a">Sí, si quieres. Trabajamos con primeras marcas y te asesoramos para elegir los que mejor se ajustan a tu uso y presupuesto.</div>',
     '<summary>¿Cuándo hay que elegir los electrodomésticos?</summary><div class="a">Antes de encargar los muebles, sobre todo si van integrados, para que las medidas encajen.</div>'),
    # --- reforma parcial ---
    ('—el salón, un dormitorio, la instalación eléctrica o los armarios— con la misma seriedad y garantía que una reforma integral.', ': el salón, un dormitorio, la instalación eléctrica o los armarios.'),
    ('Cada fase lleva su presupuesto cerrado, así controlas el gasto en todo momento.', 'Eso sí, en conjunto no suele salir más barato: hacerlo todo de una vez evita repetir trabajos.'),
    ('Sí. Desde pintar un piso o cambiar un suelo hasta poner un armario a medida. Ningún trabajo es demasiado pequeño.', 'Sí: desde pintar un piso o cambiar un suelo hasta poner un armario a medida.'),
    ('Depende del alcance, pero suelen ser trabajos de pocos días a dos semanas. Te damos el plazo antes de empezar.',
     'Depende de lo que se haga: pintar o cambiar un suelo suele ser cuestión de días, y una cocina completa lleva de tres a cuatro semanas de obra.'),
    ('<details data-reveal><summary>¿Dais garantía también en reformas parciales?</summary><div class="a">Por supuesto. Toda nuestra obra va con garantía por escrito, sea grande o pequeña.</div></details>', ''),
    # --- ventanas de PVC (también corrige datos técnicos: el PVC no lleva «rotura de puente térmico», nada es «0 mantenimiento») ---
    ('<p>Instalamos ventanas de PVC a medida que aíslan del frío, del calor y del ruido de la calle, y reducen tu factura de calefacción. Con rotura de puente térmico y vidrio bajo emisivo.</p>',
     '<p>Instalamos ventanas de PVC Deceuninck a medida, con perfiles multicámara y vidrio bajo emisivo, para aislar mejor del frío y del ruido de la calle.</p>'),
    ('El PVC es el material con mejor relación aislamiento-precio: mantiene el calor en invierno, el fresco en verano y deja el ruido fuera. Además, no necesita mantenimiento y da un aspecto limpio y moderno a la fachada.',
     'Según el IDAE, las ventanas suponen entre el 25 % y el 30 % de las necesidades de calefacción de una vivienda. Con el mismo vidrio doble bajo emisivo, una ventana de PVC ronda 1,5 W/m²K, por debajo del máximo de 2,1 que marca el Código Técnico en Bilbao. Y su mantenimiento es mínimo: limpiar los perfiles y engrasar los herrajes de vez en cuando.'),
    ('<span>Perfiles de PVC con rotura de puente térmico</span>', '<span>Perfiles de PVC multicámara de Deceuninck</span>'),
    ('<span>Doble o triple acristalamiento bajo emisivo</span>', '<span>Vidrio doble bajo emisivo</span>'),
    ('<span>Gran aislamiento acústico frente al ruido de la calle</span>', '<span>Cierre estanco, clave contra el frío y el ruido</span>'),
    ('<span>Medición e instalación por nuestro equipo, sin subcontratas</span>', '<span>Medición e instalación a medida</span>'),
    ('<div class="n">−30%</div><div class="l">menos ruido y frío</div>', '<div class="n">25–30 %</div><div class="l">de la calefacción depende de las ventanas</div>'),
    ('<div class="n">0</div><div class="l">mantenimiento</div>', '<div class="n">2,1</div><div class="l">W/m²K, máximo para una ventana nueva en Bilbao</div>'),
    ('Fabricamos cada ventana a la medida exacta de tu hueco, con el color y apertura que elijas.', 'Cada ventana se fabrica a la medida de tu hueco, con el color y la apertura que elijas.'),
    ('Descansa mejor con ventanas que dejan el ruido del tráfico fuera de casa.', 'Contra el ruido cuenta el conjunto: una ventana estanca, el vidrio adecuado y un cajón de persiana sin holguras.'),
    ('<h4>Instalación limpia</h4><p>Montamos con el mínimo desorden y retiramos las ventanas viejas por ti.</p>',
     '<h4>Bien colocada</h4><p>Una ventana tiene que quedar asentada y sellada contra el muro: si no, pasan aire y agua por bueno que sea el perfil.</p>'),
    ('Te medimos y presupuestamos gratis.', 'Te damos un presupuesto detallado y sin compromiso.'),
    ('El PVC tiene, por sí mismo, mejor aislamiento térmico que el aluminio. Si prefieres aluminio, lo instalamos con rotura de puente térmico para un buen rendimiento.',
     'Con el mismo vidrio, sí: según el IDAE, una ventana de PVC ronda 1,5 W/m²K y una de aluminio con rotura de puente térmico, 2,1. Lo comparamos con calma en <a href="#p-blog-pvc-o-aluminio-que-ventana-elegir">PVC o aluminio</a>.'),
    ('Sí. La instalación de ventanas es rápida y limpia, y puede hacerse sin tener que reformar la vivienda.',
     'Sí. En Bilbao, cambiar las ventanas que dan a un patio va con comunicación previa, y las que dan a la calle necesitan licencia porque tocan la fachada.'),
    ('Según el momento puede haber subvenciones de eficiencia energética o deducciones. Te informamos de lo vigente cuando te pasamos el presupuesto.',
     'En 2026 siguen abiertas las ayudas a la rehabilitación del Gobierno Vasco, en las que el cambio de ventanas cuenta como mejora de eficiencia energética (según ingresos y pidiéndolas antes de empezar). Si tributas en Bizkaia, hay además una deducción foral del 15 % en el IRPF, pero solo para instalar renovables o para obras que rebajen al menos un 30 % el consumo de energía primaria no renovable o lleven la vivienda a la clase A o B, con certificado energético de antes y de después: un cambio de ventanas cuenta si forma parte de una obra así.'),
    # --- productos ---
    ('decoración y ventanas de PVC. Con medición, suministro y montaje por nuestro equipo.</p>', 'decoración y ventanas de PVC Deceuninck.</p>'),
    ('<p class="lead">Trabajamos con proveedores y marcas de calidad contrastada. Te asesoramos, lo medimos y lo montamos nosotros: un único responsable de principio a fin.</p>',
     '<p class="lead">Para completar una reforma o para darle otro aire a una estancia.</p>'),
    ('Amplio catálogo de papel pintado para dar personalidad a un salón, un dormitorio o una pared concreta. Colocación incluida.', 'Papel pintado para dar personalidad a un salón, un dormitorio o una pared concreta.'),
    ('Ventanas de PVC de <strong>Deceuninck</strong>, una de las primeras marcas europeas, con gran aislamiento térmico y acústico.', 'Ventanas de PVC de <strong>Deceuninck</strong>, fabricante belga de perfiles, hechas a medida.'),
    ('<h2>Marcas de primer nivel, montadas por nuestro equipo</h2>', '<h2>Ventanas de PVC a medida</h2>'),
    ('En ventanas trabajamos con perfiles de Deceuninck, un fabricante europeo de referencia en PVC. Elegimos con cada cliente el perfil, el vidrio y el tipo de apertura según la orientación de la vivienda y el ruido de la calle.',
     'En ventanas trabajamos con perfiles de PVC de Deceuninck, fabricante belga. El perfil, el vidrio y la apertura se eligen según la vivienda: el ruido de la calle, la orientación y el tamaño del hueco.'),
    ('<span>Perfiles con rotura de puente térmico y buen aislamiento acústico</span>', '<span>Perfiles de PVC multicámara</span>'),
    ('<span>Medición, fabricación a medida e instalación sin subcontratas</span>', '<span>Medición e instalación a medida</span>'),
    ('<details data-reveal><summary>¿Vendéis los productos sueltos o solo con reforma?</summary><div class="a">Podemos suministrarlos e instalarlos aunque no hagas una reforma completa. Por ejemplo, solo un armario empotrado, un vestidor o el cambio de ventanas.</div></details>', ''),
    ('Sí, todos. Tomamos medidas en tu casa y los fabricamos para que encajen al centímetro y aprovechen toda la altura.', 'Sí: se miden en tu casa para que aprovechen el hueco y toda la altura.'),
    ('<details data-reveal><summary>¿El montaje está incluido?</summary><div class="a">Sí. Nos encargamos de la medición, el suministro y el montaje con nuestro propio equipo, y te damos garantía por escrito.</div></details>', ''),
    ('<details data-reveal><summary>¿Puedo ver muestras?</summary><div class="a">Claro. Pásate por la oficina de Karmelo Kalea 15, en Santutxu, y te enseñamos muestras de materiales y acabados.</div></details>', ''),
    # --- trabajos realizados ---
    ('¿Quieres ver más ejemplos parecidos a tu caso? Enséñanos tu vivienda y te mostramos reformas similares que hemos hecho.', '¿Tu obra se parece a alguna de estas? Cuéntanosla y vamos a verla.'),
    # --- contacto ---
    ('Pide tu presupuesto gratis</h1>', 'Pide tu presupuesto sin compromiso</h1>'),
    ('Cuéntanos tu reforma y te damos un precio cerrado en 24 horas, sin compromiso. O llámanos ahora mismo: estamos en Santutxu, a un paso de ti.',
     'Cuéntanos tu reforma: vamos a ver la vivienda y te damos un presupuesto detallado y sin compromiso en 24 horas. O llámanos: estamos en Karmelo Kalea 15, en Santutxu.'),
    ('Rellena estos datos y te llamamos con un presupuesto en menos de 24 horas.', 'Rellena estos datos y te llamamos para hablar de tu reforma.'),
    (' Respuesta en menos de 24 h · Sin compromiso</div>', ' Sin compromiso · No compartimos tus datos</div>'),
    ('Pásate a vernos sin cita en Santutxu, o pide cita para la oficina de San Adrián.',
     'Pásate a vernos en Santutxu en horario de oficina (las tardes, con cita previa), o pide cita para la oficina de San Adrián.'),
    # --- reformas en Bizkaia ---
    ('a los municipios de alrededor con el mismo presupuesto cerrado y la misma garantía.', 'a los municipios de alrededor.'),
    ('Elige tu zona o cuéntanos dónde está tu vivienda. Nos desplazamos por toda la provincia sin coste para valorar tu reforma.',
     'Cuéntanos dónde está tu vivienda: vamos a verla a cualquier punto de la provincia y te damos un presupuesto sin compromiso. Fuera de Bilbao hemos hecho trabajos como unos miradores en Orduña o unos aleros de fachada en Algorta.'),
    # --- solicitud enviada ---
    ('<p>En menos de 24 h laborables, para entender bien qué necesitas y concretar día y hora de visita.</p>', '<p>Para entender bien qué necesitas y quedar un día para la visita.</p>'),
    ('<p>Visitamos tu casa, medimos y escuchamos. Sin coste, sin compromiso y sin prisas.</p>', '<p>Visitamos tu casa, medimos y escuchamos. Sin compromiso y sin prisas.</p>'),
    # --- legales: sin notas internas; la privacidad dice por dónde llegan los formularios ---
    ('<h2>Con quién los compartimos</h2><p>No cedemos tus datos a terceros salvo obligación legal o cuando sea imprescindible para ejecutar tu reforma (por ejemplo, un proveedor concreto), siempre con las debidas garantías.</p>',
     '<h2>Con quién los compartimos</h2><p>Los formularios de la web nos llegan por correo electrónico a través de FormSubmit (formsubmit.co), un servicio externo de envío de formularios. Fuera de eso, no cedemos tus datos a terceros salvo obligación legal o cuando sea imprescindible para hacer tu reforma (por ejemplo, un proveedor concreto).</p>'),
    ('Si no quieres que se carguen, puedes bloquear las cookies de terceros en tu navegador.</p><h2>Si se añade analítica</h2><p>Si en el futuro se incorporan herramientas de estadísticas de visitas (como Google Analytics), se informará aquí y se pedirá tu consentimiento previo mediante un aviso.</p><h2>Cómo gestionarlas</h2><p>Puedes bloquear o eliminar las cookies desde la configuración de tu navegador en cualquier momento.</p>',
     'El mapa solo se carga si lo aceptas en el aviso de cookies o si pulsas «Ver el mapa».</p><h2>Tu elección</h2><p>La web guarda en tu navegador si has aceptado o rechazado esas cookies, para no volver a preguntarte. Puedes cambiar de opinión cuando quieras en «Configurar cookies», al pie de cada página, o borrar las cookies desde la configuración de tu navegador.</p>'),
]
