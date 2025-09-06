import http.server
import socket
import socketserver
import threading
import webbrowser
import time
import os
import sys

def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))           
        return s.getsockname()[1]
    

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class LocalHTTPServer:
    def __init__(self, port=None, html_file="index.html"):
        self.port = port or find_free_port()
        self.html_file = html_file
        self.server_thread = None
        self.httpd = None

    def handler_factory(self):
        parent = self
        class CustomHandler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=os.getcwd(), **kwargs)

            def do_GET(self):
                if self.path in ('/', '/index.html'):
                    self.path = f'/{parent.html_file}'
                return super().do_GET()
        return CustomHandler
    
    def _serve(self):
        handler = self.handler_factory()
        with ReusableTCPServer(("", self.port), handler) as httpd:
            self.httpd = httpd
            print(f"Serving on http://localhost:{self.port}/{self.html_file}")
            httpd.serve_forever()

    def start(self, open_browser=True):
        thread = threading.Thread(target=self._serve, daemon=True)
        thread.start()

        if open_browser:
            def _open():
                time.sleep(1)
                webbrowser.open(f"http://localhost:{self.port}/{self.html_file}")
            threading.Thread(target=_open, daemon=True).start()

    def open_browser(self):
        time.sleep(1)  # give server time to bind
        url = f"http://localhost:{self.port}/{self.html_file}"
        webbrowser.open(url, new=0, autoraise=True)

