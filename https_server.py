import http.server
import ssl

httpd = http.server.HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="~/ssl-certs/localhost.key", certfile="~/ssl-certs/localhost.crt", server_side=True)

print("Serving on https://localhost:8000")
httpd.serve_forever()
