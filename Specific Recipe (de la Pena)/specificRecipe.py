import json

class RecipeManager:
    def __init__(self, file_path):
        """
        Initialize RecipeManager with a file path for recipes.
        """
        self.file_path = file_path
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """
        Load recipes from the JSON file and return them.
        """
        try:
            with open(self.file_path, "r") as file:
                recipes_data = json.load(file)
                if isinstance(recipes_data, list):
                    return recipes_data  # Return list of recipes
                elif isinstance(recipes_data, dict):
                    return recipes_data.get("recipes", [])  # Handle dict with "recipes" key
                else:
                    print("Invalid JSON format. Expected list or dictionary.")
                    return []
        except Exception as e:
            print(f"Error loading recipes: {e}")
            return []

    def get_all_recipes(self):
        """
        Return all recipes.
        """
        return self.recipes

    def get_recipe_by_name(self, name):
        """
        Find a recipe by its name.
        """
        for recipe in self.recipes:
            if recipe.get("name", "").lower() == name.lower():
                return recipe
        return None
