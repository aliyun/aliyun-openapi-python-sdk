import sys

# The unittest module got a significant overhaul
# in 2.7, so if we're in 2.6 we can use the backported
# version unittest2.
import threading

if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest


# the version under py3 use the different package
if sys.version_info[0] == 3:
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer
else:
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer


class MyServer:
    _headers = {}
    _url = ''

    def __enter__(self):
        class ServerHandler(SimpleHTTPRequestHandler):

            def do_GET(_self):
                _self.protocol_version = 'HTTP/1.1'
                self._headers = _self.headers
                self._url = _self.path
                _self.send_response(200)
                _self.send_header("Content-type", "application/json")
                _self.end_headers()
                _self.wfile.write(b"{}")

        self.server = HTTPServer(("", 51352), ServerHandler)

        def thread_func():
            self.server.serve_forever()

        thread = threading.Thread(target=thread_func)
        thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.server:
            self.server.shutdown()
            self.server = None

    @property
    def headers(self):
        return self._headers

    @property
    def url(self):
        return self._url

    @property
    def content(self):
        class Response:
            def __init__(self, headers):
                self.headers = headers
        response = Response(self._headers)
        return response
