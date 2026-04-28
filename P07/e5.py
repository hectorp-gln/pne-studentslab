import http.client
import json
from Seq1 import Seq

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6-269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
    }

for gene in genes:

    SERVER = "rest.ensembl.org"
    ENDPOINT = "/sequence/id/" + genes[gene]
    PARAMS = "?content-type=application/json"
    URL = SERVER + ENDPOINT + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

        # -- Read the response message from the server
    r1 = conn.getresponse()

    # -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # -- Read the response's body
    object = r1.read().decode("utf-8")

    response = json.loads(object)

    print(f"Gene: {gene}")
    print(f"Description: {response["desc"]}")
    s = Seq(response["seq"])
    print(f"Total length: {s.len()}")
    highest = 0
    highest_key = None
    for base in s.count():
        if s.count()[base] > highest:
                highest = s.count()[base]
                highest_key = base
        print(base + ": " + str(s.count()[base]) + "(" + str(round(s.count()[base]/s.len()*100,2)) + "%)")
    print(f"Most frequent base: " + highest_key)

