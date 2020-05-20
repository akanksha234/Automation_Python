import csv
from pathlib import Path

file_to_read = Path('../Files/addresses.csv')

with open( file_to_read, newline='') as addresses_doc:
    addresses_doc_dict = csv.DictReader(addresses_doc)
    for row in addresses_doc_dict:
        print(row)