from pathlib import Path


FILENAME = "sequences/U5.txt"

file_contents = Path(FILENAME).read_text()
non_header = file_contents.split("\n")[1:-1]
body = "\n".join(non_header)

print(body)
