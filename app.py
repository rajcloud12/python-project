
# Write a simple python http server
#Python Application
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello World")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Starting httpd...')
    httpd.serve_forever()

run()

# Run the server and open the browser to http://localhost:8000
# You should see the message Hello World

