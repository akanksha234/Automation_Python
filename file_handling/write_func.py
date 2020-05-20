"""
write to the file giving w as additional argument as the deafult argument is r
"""
from pathlib import Path
file_to_create = Path('../Files/bad_bands.txt')

with open(file_to_create,'w') as bad_bands_doc:
    bad_bands_doc.write("No bands that I can rememeber of: \n But there is "
                        "a singer called badshah who irritates me by his lyrics. ")
