import http.server
import socketserver
import termcolor
from pathlib import Path


PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        request = self.requestline.split()[1][1:]
        if request == "":
            contents = Path("html/index.html").read_text()
        else:
            try:
                contents = Path("html/" + request + ".html").read_text()
            except:
                contents = Path("html/error.html").read_text()


        self.send_response(200)  # -- Status line: OK!

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        self.end_headers()

        self.wfile.write(contents.encode())

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()