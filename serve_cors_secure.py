import http.server
import socketserver
PORT = 8000

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    def log_message(self, fmt, *args):
        return

socketserver.TCPServer.allow_reuse_address = True
httpd = socketserver.TCPServer(('', PORT), CORSHandler)
httpd.serve_forever()
