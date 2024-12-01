import os 
import json

json_path = os.path.join(os.path.dirname(__file__), "assets", "recipesAll.json")
with open(json_path, 'r') as file: 
    recipes_data = json.load(file)
    #recipe data has been loaded