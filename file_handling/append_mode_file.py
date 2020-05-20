from pathlib import Path

file_to_append = Path("../Files/generalised.txt")

with open(file_to_append, 'a') as doc:
    doc.write('it still is\n')
