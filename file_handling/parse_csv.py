"""
csv module makies parsing files easier,
it handles new lines and commas other than as a separtor
"""

import csv
from pathlib import Path

file_to_read = Path('../Files/sample_csv.csv')
file_to_write = Path('../Files/sample_csv_copy.csv')

#the reader method is expecting a comma as the default value
with open(file_to_read) as csv_file:
    csv_reader = csv.reader(csv_file)
    index = next(csv_reader)
    print(index)
    #returns a list of list containing each value separated by commas
    #to access each column use list[index] for every list in csv_reader
    with open(file_to_write, 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
    # index  = next(csv_reader)  #next is used to step over to the next in the iterator
        for line in csv_reader:
            csv_writer.writerow(line)
            


    # print("columns ----> ", index)
    # print("Number of columns ---> ", len(index))

#Now lets try to write these file to a new file
