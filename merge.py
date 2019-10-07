import json 
import os 

file_names = os.listdir("./files/")

JSONS = []

for file_name in file_names:
    with open("./files/"+file_name,'r') as j_file:
        data = json.load(j_file)
        JSONS.append(data)

with open('data.json', 'w') as outfile:
    json.dump(JSONS, outfile)