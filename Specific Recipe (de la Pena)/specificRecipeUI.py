import flet as ft
from specificRecipe import RecipeManager
from flet import FontWeight


class RecipeCard:
    """Recipe card for overview."""

    def __init__(self, recipe, on_click):
        self.recipe = recipe
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
                                        value=self.recipe["name"],
                                        size=18,
                                        weight=FontWeight.BOLD,
                                        max_lines=1,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.LOCATION_PIN, size=20, color=ft.colors.BLUE_300),
                                            ft.Text(self.recipe["origin"], size=14),
                                        ],
                                        spacing=2,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(
                                                ft.icons.LOCAL_FIRE_DEPARTMENT, size=20, color=ft.colors.BLUE_300
                                            ),
                                            ft.Text(f"Difficulty: {self.recipe['difficulty']}", size=14),
                                        ],
                                        spacing=2,
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Icon(ft.icons.TIMER, size=20, color=ft.colors.BLUE_300),
                                            ft.Text(self.recipe["prep_time"], size=14),
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
        recipe_details_container.content = ft.Column(
            controls=[
                ft.Container(
                    width=400,
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
                ft.Text(
                    value=recipe["name"],
                    size=24,
                    weight=FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=10, thickness=2),
                ft.Text(f"Origin: {recipe['origin']}", size=18),
                ft.Text(f"Difficulty: {recipe['difficulty']}", size=18),
                ft.Text(f"Prep Time: {recipe['prep_time']} minutes", size=18),
                ft.Divider(height=10, thickness=2),
                ft.Text(
                    "Ingredients:",
                    size=20,
                    weight=FontWeight.BOLD,
                ),
                ft.ListView(
                    controls=[ft.Text(f"- {ingredient}", size=16) for ingredient in recipe.get("ingredients", [])],
                    spacing=5,
                ),
                ft.Divider(height=10, thickness=2),
                ft.Text(
                    "Steps:",
                    size=20,
                    weight=FontWeight.BOLD,
                ),
                ft.ListView(
                    controls=[
                        ft.Text(f"{idx + 1}. {step}", size=16) for idx, step in enumerate(recipe.get("steps", []))
                    ],
                    spacing=5,
                ),
                ft.ElevatedButton(
                    text="Back to Recipes",
                    on_click=lambda e: display_recipe_list(),
                    bgcolor=ft.colors.GREEN,
                    color=ft.colors.WHITE,
                    width=200,
                ),
            ],
            spacing=10,
        )
        stack.controls = [recipe_details_page]
        page.update()

    # Pages
    recipe_list_page = ft.Container(content=recipe_list_view, expand=True)
    recipe_details_page = recipe_details_container

    # Add the stack with the default page
    stack.controls = [recipe_list_page]
    page.add(stack)

    # Load the recipe list initially
    display_recipe_list()


ft.app(target=main)
