# check the similarities in the table and group them and create a json array from the result
import csv
import json
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# read the data from a csv document.json
file_path = 'Users/regina.kanya/Documents/'
data = []
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append((row[0], row[1], row[2]))
        #how many rows do you want to read?

# grouping the data in a specific way which I needed
grouped = {}

for Names, Brand, ref in data:
    for grouped_brand, group in grouped.items():
        if Brand == grouped_brand:
            for existing_name, existing_ref in group.items():
                if existing_ref is True:
                    continue
                if similar(existing_ref, ref) > 0.8:
                    group[existing_name] = True
                    break
            else:
                group[Names] = True
            break
    else:
        grouped[Brand] = {Names: True}  #it will display true, you can changes it another value

# create a json document.json
# you can create a different local path, not in this project
with open('output.json', 'w') as jsonfile:
    json.dump(grouped, jsonfile, indent=4)
