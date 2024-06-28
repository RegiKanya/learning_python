import json

file_path = 'new_file.json'
with open(file_path, 'r') as file:
    data = json.load(file)
key = "surveyId"
value = [item[key] for item in data]
print(value)