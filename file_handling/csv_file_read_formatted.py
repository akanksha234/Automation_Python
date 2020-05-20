from pathlib import Path
import csv

csv_file = Path('../Files/sample_csv.csv')

with open( csv_file, newline='') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        for key in row.keys():
            print (row[key])
