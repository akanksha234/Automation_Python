import csv
from pathlib import Path

file_to_read = Path('../Files/addresses.csv')
file_to_write = Path('../Files/addresses_dict.csv')

with open(file_to_read) as csv_file:
    csv_reader_dict = csv.DictReader(csv_file, delimiter=';')
    field_names = next(csv_reader_dict)
    #csv_writer needs the field names as the first line in order to
    #make them keys of every column with a delimiter
    with open(file_to_write, 'w') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter='\t')
        #if we want the header too
        csv_writer.writeheader()
        for line in csv_reader_dict:
        #     print(line['Employee E-Mail'])
            csv_writer.writerow(line)