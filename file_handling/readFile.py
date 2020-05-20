"""
reading a file with read and file object

"""

with open("..\Files\welcome.txt") as text_file:
    text_data = text_file.read()

print(text_data)