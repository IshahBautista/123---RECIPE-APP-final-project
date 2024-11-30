import flet as ft
import re
from AddRecipeBackend import load_recipes, add_recipe, save_recipes

def configure_page(page: ft.Page):
    page.title = "Add Recipe"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

def main(page):
    configure_page(page)
    # Load existing recipes
    recipes = load_recipes()

    window_title = ft.Text("Add a Recipe", size=26, color="#403D39", weight=ft.FontWeight.BOLD)
    window_divider = ft.Divider(height=10, thickness=5, color="orange")

    name_label = ft.Text("Recipe Name:", size=15, color="#252422", weight=ft.FontWeight.W_700)
    name_input = ft.CupertinoTextField(placeholder_text="eg. Sinigang", focused_color = "orange")
    
    origin_label = ft.Text("Origin:", size=15, color="#252422", weight=ft.FontWeight.W_700)
    origin_input = ft.CupertinoTextField(placeholder_text="eg. Philippines", focused_color = "orange")

    prep_time_label = ft.Text("Preparation Time (in minutes):", size=15, color="#252422", weight=ft.FontWeight.W_700)
    prep_time_input = ft.CupertinoTextField(placeholder_text="eg. 40", focused_color = "orange")

    ingredients_label = ft.Text("Ingredients (comma separated):", size=15, color="#252422", weight=ft.FontWeight.W_700)
    ingredients_input = ft.CupertinoTextField(placeholder_text="eg. Pork, Tamarind, etc.", focused_color = "orange", multiline=True, min_lines=1, max_lines=100)

    steps_label = ft.Text("Steps (comma separated):", size=15, color="#252422", weight=ft.FontWeight.W_700)
    steps_input = ft.CupertinoTextField(placeholder_text="eg. Prepare ingredients, etc.", focused_color = "orange", multiline=True, min_lines=1, max_lines=100)
    
    error_message = ft.Text(color="red", size=12)

    def on_submit(e):
        error_message.value = ""
        page.update()
        
        # Get the input values
        name = name_input.value
        origin = origin_input.value
        prep_time = prep_time_input.value
        ingredients = ingredients_input.value.split(",")
        steps = steps_input.value.split(",")
        preprocessedname = re.sub(r'[^a-zA-Z0-9]', '', name.lower())

        # Validation
        if not prep_time.isdigit():
            error_message.value = "Preparation time must be an integer."
            page.update()
            return
        
        if not origin.replace(" ", "").isalpha():
            error_message.value = "Origin must contain only letters and spaces."
            page.update()
            return
        
        if not name:
            error_message.value = "Recipe name cannot be empty."
            page.update()
            return
        
        if any(recipe['name'].lower() == name.lower() for recipe in recipes):
            error_message.value = f"A recipe with the name '{name}' already exists."
            page.update()
            return
        
        # Write the new recipe
        new_recipe = {
            "name": name,
            "origin": origin,
            "prep_time": prep_time,
            "difficulty": "Difficulty", # Needs to be implemented
            "ingredients": [ingredient.strip() for ingredient in ingredients],
            "steps": [step.strip() for step in steps],
            "preprocessedname": preprocessedname
        }

        # Add the new recipe to the list
        recipes.append(new_recipe)

        # Save the updated recipes to the file
        save_recipes(recipes)
        
        # When recipe is submitted, show message and clear inputs
        page.add(ft.Text(f"Recipe '{name}' added successfully!", color="green"))
        name_input.value = ""
        origin_input.value = ""
        prep_time_input.value = ""
        ingredients_input.value = ""
        steps_input.value = ""
        page.update()

    submit_button = ft.FilledButton(text="Submit Recipe", style=ft.ButtonStyle(color="white", bgcolor="orange"), on_click=on_submit)

    form_column = ft.Column(
        controls=[
            window_title,
            window_divider,
            name_label, name_input,
            origin_label, origin_input,
            prep_time_label, prep_time_input,
            ingredients_label, ingredients_input,
            steps_label, steps_input,
            error_message
        ],
        spacing=15, 
        expand=True  
    )

    scrollable_area = ft.ListView(
        controls=[form_column],
        auto_scroll=True,  
        expand=True
    )

    main_column = ft.Column(
        controls=[
            scrollable_area,
            submit_button
        ],
        expand=True,
        
    )
    
    page.add(main_column)

ft.app(target=main)