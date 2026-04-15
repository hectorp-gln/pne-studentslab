import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from jinja2.nodes import Compare

PORT = 8080


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def read_fasta(filename):
    file_contents = Path(filename).read_text()
    non_header = file_contents.split("\n")[1:-1]
    bases = "".join(non_header)
    return bases

def complement(seq):
    compliment_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement = ""
    for base in seq:
        complement += compliment_dict[base]
    return complement

def reverse(seq):
    return seq[::-1]

def count(seq, base):
    count = 0
    for nucleotide in seq:
        if nucleotide == base:
            count += 1
    return count

def percentage(seq, base):
    return round(count(seq,base) / len(seq), 4) * 100

sequence_dict = {"0":"AATG","1":"GATA","2":"TCCC","3":"GCTA","4":"TCGT"}

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)

        if path == "/" or (path == "/myserver" and not arguments):
            contents = Path('html/index.html').read_text()
        elif path == "/myserver":
            action = arguments.get("action",[""])[0]

            if action == "PING":
                contents = Path("html/ping.html").read_text()

            elif action == "GET":
                num = arguments["get"][0]
                contents = read_html_file("get.html").render(context={"seq": sequence_dict[num], "num":num})

            elif action == "GENE":
                name = arguments["gene"][0]
                full_gene = read_fasta("sequences/" + name +".txt")
                contents = read_html_file("gene.html").render(context={"gene": full_gene, "name":name})

            elif action == "OPERATE!":
                seq = arguments["user_seq"][0]
                operation = arguments["operation"][0]

                if operation == "Info":
                    a = f"A: {count(seq, 'A')} ({percentage(seq,"A"):.2f}%)"
                    c = f"C: {count(seq, 'C')} ({percentage(seq,"C"):.2f}%)"
                    t = f"T: {count(seq, 'T')} ({percentage(seq,"T"):.2f}%)"
                    g = f"G: {count(seq, 'G')} ({percentage(seq,"G"):.2f}%)"
                    contents = read_html_file("operation.html").render(context={
                        "seq": seq,
                        "op": operation,
                        "res": "Sequence: " + seq,
                        "count": "Total length: " + str(len(seq)),
                        "A":a,
                        "C":c,
                        "T":t,
                        "G":g})

                else:

                    if operation == "Comp":
                        result = complement(seq)

                    else:
                        result = reverse(seq)

                    contents = read_html_file("operation.html").render(context={
                        "seq":seq,
                        "op":operation,
                        "res":result})

            else:
                contents = Path("html/error.html").read_text()
        else:
            contents = Path("html/error.html").read_text()

        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()