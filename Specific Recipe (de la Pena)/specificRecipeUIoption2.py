import flet as ft
from specificRecipe import RecipeManager
from flet import FontWeight


class RecipeCard:
    """Recipe card for overview."""

    def __init__(self, recipe, on_click):
        self.recipe = recipe  # Assign the recipe to the class instance
        self.on_click = on_click
        self.card = self.build()

    def build(self):
        return ft.Container(
            content=ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                bgcolor=ft.colors.AMBER_300,
                                width=100,
                                height=100,
                                border_radius=8,
                                alignment=ft.alignment.center,
                                content=ft.Text(
                                    "Image",
                                    weight=FontWeight.BOLD,
                                    size=12,
                                    color=ft.colors.WHITE,
                                ),
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value=self.recipe["name"],  # Correct reference
                                        size=18,
                                        weight=FontWeight.BOLD,
                                        max_lines=1,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.LOCATION_PIN, size=20, color=ft.colors.BLUE_300),
                                            ft.Text(self.recipe["origin"], size=14),  # Correct reference
                                        ],
                                        spacing=2,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                ft.icons.LOCAL_FIRE_DEPARTMENT, size=20, color=ft.colors.BLUE_300
                                            ),
                                            ft.Text(f"Difficulty: {self.recipe['difficulty']}", size=14),  # Correct reference
                                        ],
                                        spacing=2,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.TIMER, size=20, color=ft.colors.BLUE_300),
                                            ft.Text(self.recipe["prep_time"], size=14),  # Correct reference
                                        ],
                                        spacing=2,
                                    ),
                                ],
                                spacing=5,
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=10,
                ),
                elevation=3,
            ),
            on_click=lambda e: self.on_click(self.recipe),
            padding=10,
        )


def main(page: ft.Page):
    page.title = "Recipe Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 440
    page.window.height = 956
    page.scroll = ft.ScrollMode.AUTO

    # Load recipes
    file_path = r"C:\Users\Jaina\OneDrive\Desktop\BSCS2_SEM1\CMSC 123\RECIPE\recipesAll.json"
    recipe_manager = RecipeManager(file_path)

    # Stacked views to emulate pages
    stack = ft.Stack(expand=True)

    # Recipe list page
    recipe_list_view = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    def display_recipe_list():
        """Display the recipe list."""
        recipe_list_view.controls.clear()
        for recipe in recipe_manager.get_all_recipes():
            card = RecipeCard(recipe, on_click=show_recipe_details).card
            recipe_list_view.controls.append(card)
        stack.controls = [recipe_list_page]
        page.update()

    # Recipe details page
    recipe_details_container = ft.Container(padding=10)  # Container with padding for details

    def show_recipe_details(recipe):
        """Show recipe details in a new page."""

        # Visibility controls for Ingredients and Steps
        ingredients_visible = False
        steps_visible = False

        def toggle_ingredients(e):
            nonlocal ingredients_visible
            ingredients_visible = not ingredients_visible
            build_details_page()

        def toggle_steps(e):
            nonlocal steps_visible
            steps_visible = not steps_visible
            build_details_page()

        def build_details_page():
            recipe_details_container.content = ft.Column(
                controls=[
                    # Back Arrow with small padding
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_size=24,
                            tooltip="Back to Recipes",
                            on_click=lambda e: display_recipe_list(),
                        ),
                        padding=ft.Padding(left=0, top=5, right=0, bottom=5),
                        alignment=ft.alignment.center_left,
                    ),
                    # Image Placeholder
                    ft.Container(
                        width=page.window.width - 40,
                        height=200,
                        bgcolor=ft.colors.AMBER_300,
                        alignment=ft.alignment.center,
                        border_radius=10,
                        content=ft.Text(
                            "Image Placeholder",
                            size=16,
                            weight=FontWeight.BOLD,
                            color=ft.colors.WHITE,
                        ),
                    ),
                    # Recipe Title
                    ft.Text(
                        value=recipe["name"],
                        size=26,
                        weight=FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Divider(height=10, thickness=2),
                    # Metadata Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Origin:", size=18, weight=FontWeight.BOLD),
                                        ft.Text(recipe["origin"], size=18),
                                    ],
                                    spacing=10,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Difficulty:", size=18, weight=FontWeight.BOLD),
                                        ft.Text(str(recipe["difficulty"]), size=18),
                                    ],
                                    spacing=10,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Text("Prep Time:", size=18, weight=FontWeight.BOLD),
                                        ft.Text(recipe["prep_time"], size=18),
                                    ],
                                    spacing=10,
                                ),
                            ],
                            spacing=5,
                        ),
                        padding=ft.Padding(10, 5, 10, 5),
                        bgcolor=ft.colors.LIGHT_GREEN_50,
                        border_radius=10,
                    ),
                    ft.Divider(height=10, thickness=2),
                    # Ingredients Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Ingredients", size=22, weight=FontWeight.BOLD),
                                        ft.IconButton(
                                            icon=ft.icons.ARROW_DROP_DOWN if ingredients_visible else ft.icons.ARROW_RIGHT,
                                            on_click=toggle_ingredients,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f"• {ingredient}", size=18)
                                            for ingredient in recipe.get("ingredients", [])
                                        ],
                                    ),
                                    visible=ingredients_visible,
                                ),
                            ],
                            spacing=5,
                        ),
                    ),
                    ft.Divider(height=10, thickness=2),
                    # Steps Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Text("Steps", size=22, weight=FontWeight.BOLD),
                                        ft.IconButton(
                                            icon=ft.icons.ARROW_DROP_DOWN if steps_visible else ft.icons.ARROW_RIGHT,
                                            on_click=toggle_steps,
                                        ),
                                    ],
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(f"{idx + 1}. {step}", size=18)
                                            for idx, step in enumerate(recipe.get("steps", []))
                                        ],
                                    ),
                                    visible=steps_visible,
                                ),
                            ],
                            spacing=5,
                        ),
                    ),
                ],
                spacing=15,
            )
            page.update()

        build_details_page()
        stack.controls = [recipe_details_page]

    # Pages
    recipe_list_page = ft.Container(content=recipe_list_view, expand=True)
    recipe_details_page = recipe_details_container

    # Add the stack with the default page
    stack.controls = [recipe_list_page]
    page.add(stack)

    # Load the recipe list initially
    display_recipe_list()


ft.app(target=main)
