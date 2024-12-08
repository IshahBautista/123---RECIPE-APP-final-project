import json
import os
from config import json_path, recipes_data

def load_recipes():
    # Loads the current list of recipes from the JSON file
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    # Saves the list of recipes to the JSON file
    with open(json_path, "w") as f:
        json.dump(recipes, f, indent=4)

def add_recipe(recipes, new_recipe):
    # Adds a new recipe to the list and save it
    if any(recipe['name'].lower() == new_recipe['name'].lower() for recipe in recipes):
        raise ValueError(f"A recipe with the name '{new_recipe['name']}' already exists.")
    recipes.append(new_recipe)
    save_recipes(recipes)