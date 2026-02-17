from pathlib import Path


FILENAME = "sequences/ADA.txt"

file_contents = Path(FILENAME).read_text()
non_header = file_contents.split("\n")[1:-1]
body = "".join(non_header)

print(len(body))