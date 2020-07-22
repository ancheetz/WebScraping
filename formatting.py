import json, csv

in_file = csv.DictReader(open('Top_2016.csv'))

for row in in_file:
    print(row)