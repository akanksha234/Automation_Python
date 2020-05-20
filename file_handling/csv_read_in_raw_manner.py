from pathlib import Path

csv_file = Path('../Files/sample_csv.csv')


with open(csv_file) as file:
    print( file.read() )
