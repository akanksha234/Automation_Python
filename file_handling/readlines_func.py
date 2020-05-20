"""
the readlines() function returns a list of lines contained by the file.
the readline() function returns only one line, as reading whole file at once can cause issues
"""

with open("..\Files\how_many_lines.txt") as lines_doc:
    first_line = lines_doc.readline()
    for line in lines_doc.readlines():
        print(line, end=' ')

print("\n\nFirst line is ----> ", first_line)
