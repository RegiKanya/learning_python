#ha swagger response body-ból gyorsan ki kell olvasni valami:

import json

file_path = '/Users/kanyaregina/Documents/Ewiser/Others/swagger.json'

with open(file_path, 'r') as f:
    data = json.load(f)

#megkeresni egy kulcshoz tartozó értékeket
#list = [entry["paths"] for entry in data["paths"]]
#print(list)

#kiszedni magát a kulcsokat, ami mindig más néven van
list = list(data.get('paths', {}).keys())

for path in list:
    print(path)