import os 
import json

json_path = os.path.join(os.path.dirname(__file__), "assets", "recipesAll.json")
pantry_path = os.path.join(os.path.dirname(__file__), "assets", "pantry.json")

class ConfigContent:
    def __init__(self):
        self.recipes_data = []
        self.pantry_list = []
        self.update_recipeContent()
        self.update_pantryContent()

    def update_recipeContent(self):
        with open(json_path, 'r') as file: 
            self.recipes_data = json.load(file)
            #recipe data has been loaded

    def update_pantryContent(self):
        with open(pantry_path, 'r') as file: 
            self.pantry_list = json.load(file)
            #pantry data has been loaded

    def getRecipeContent(self):
        return self.recipes_data
    
    def getPantryContent(self):
        return self.pantry_list

configData = ConfigContent()
recipes_data = configData.getRecipeContent()
pantry_data = configData.getPantryContent()

def updateRecipeCaller():
    print("updating recipes")
    configData.update_recipeContent()
    recipes_data = configData.getRecipeContent()
    return recipes_data

def updatePantryCaller():
    print("updating pantry")
    configData.update_pantryContent()
    pantry_data = configData.getPantryContent()
    return pantry_data