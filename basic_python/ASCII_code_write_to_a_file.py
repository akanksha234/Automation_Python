"""
Checking capitalisation and ASCII value of a letter
and writing it to the file
"""
char_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910"


# with open(r"Files\ASCII File.txt", "w+") as text_file:
#     for char in char_string:
#         ascii_code = ord(char)
#         text_file.write(char + " ---> " + str(ascii_code) + "\n")

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []


index = 9
while len(students_in_poetry) < 6:
    students_in_poetry.append( all_students.pop(index))
    index -= 1

print(students_in_poetry)



