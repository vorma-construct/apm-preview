#!/bin/bash
# Monta un alojamiento de prueba: WordPress de mentira + la web nueva en /nueva/ + el .htaccess real
set -e
R=/tmp/claude-0/apache; D=/srv/apm-test/docroot
rm -rf $D && mkdir -p $D/wp-content/uploads/2019/11 $D/wp-admin
cp -r ${PAQUETE:-/home/claude/apm-build/salida/prod}/nueva $D/nueva
echo "foto" > $D/wp-content/uploads/2019/11/reforma-integral-en-santutxu.jpeg
echo "<?php echo 'PANEL'; " > $D/wp-admin/index.php
python3 - <<'PY'
import sys; sys.path.insert(0,'/home/claude/apm-build')
from datos import DIRECCIONES_ACTUALES
lista = ','.join("'%s'" % u for u in DIRECCIONES_ACTUALES)
php = """<?php
// WordPress de mentira: contesta las 33 direcciones de siempre como hace hoy la web real
$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$wp = [%s, '/robots.txt', '/sitemap_index.xml'];
if (in_array($uri, $wp)) { echo "WORDPRESS $uri"; exit; }
if (substr($uri, -1) !== '/' && in_array($uri . '/', $wp)) { header("Location: $uri/", true, 301); exit; }
http_response_code(404); echo "WORDPRESS-404 $uri";
""" % lista
open('/srv/apm-test/docroot/index.php','w').write(php)
PY
{ cat ${PAQUETE:-/home/claude/apm-build/salida/prod}/htaccess-PEGAR-ARRIBA.txt; cat <<'WP'
# BEGIN WordPress
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
WP
} > $D/.htaccess
cat > $R/apache.conf <<CONF
ServerRoot /etc/apache2
PidFile /srv/apm-test/apache.pid
Listen 127.0.0.1:8200
User www-data
Group www-data
LoadModule mpm_prefork_module /usr/lib/apache2/modules/mod_mpm_prefork.so
LoadModule authz_core_module /usr/lib/apache2/modules/mod_authz_core.so
LoadModule dir_module /usr/lib/apache2/modules/mod_dir.so
LoadModule mime_module /usr/lib/apache2/modules/mod_mime.so
LoadModule rewrite_module /usr/lib/apache2/modules/mod_rewrite.so
LoadModule headers_module /usr/lib/apache2/modules/mod_headers.so
LoadModule env_module /usr/lib/apache2/modules/mod_env.so
LoadModule php_module /usr/lib/apache2/modules/libphp8.3.so
TypesConfig /etc/mime.types
ErrorLog /srv/apm-test/error.log
LogLevel warn
DirectoryIndex index.php index.html
<Directory />
  AllowOverride None
  Require all denied
</Directory>
DocumentRoot $D
<FilesMatch "\.php$">
  SetHandler application/x-httpd-php
</FilesMatch>
<Directory $D>
  Options FollowSymLinks
  AllowOverride All
  Require all granted
</Directory>
CONF
