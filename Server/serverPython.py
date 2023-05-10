import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define la ruta de los archivos a compartir
os.chdir("/home/ccrhdbj")

# Inicia el servidor en el puerto 8000
httpd = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
