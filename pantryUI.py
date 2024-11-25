import flet as ft
from pantrybackendfile import PantryManager

def main(page: ft.Page):
    page.title = "Pantry Manager"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 440
    page.window_height = 956
    page.window_resizable = False

    # Initialize PantryManager
    pantry_manager = PantryManager.create()

    # UI Components
    ingredient_input = ft.TextField(
        label="Enter Ingredient",
        hint_text="e.g., Sugar, Flour",
        text_align=ft.TextAlign.CENTER,
        autofocus=True,
        expand=True,
        on_submit=lambda e: add_ingredient(None)  # Trigger add_ingredient on Enter
    )
    feedback_text = ft.Text("", size=14, color=ft.colors.DEEP_ORANGE_400)

    pantry_list = ft.ListView(
        spacing=10,
        padding=10,
        auto_scroll=True,  
        expand=True  
    )

    def update_pantry():
        """Update the pantry display."""
        pantry_list.controls.clear()
        for item in pantry_manager.get_pantry_list():
            pantry_list.controls.append(
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Text(item, size=16, expand=True),
                            ft.IconButton(
                                icon=ft.icons.CLOSE,
                                icon_color=ft.colors.RED,
                                tooltip="Remove",
                                on_click=lambda e, ingredient=item: remove_ingredient(ingredient),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        spacing=10,
                    ),
                    padding=10,
                    border_radius=10,
                    bgcolor=ft.colors.LIGHT_GREEN_50,  # Light green background for each ingredient
                    shadow=ft.BoxShadow(blur_radius=6, spread_radius=2, color=ft.colors.BLACK12),
                    animate=ft.animation.Animation(400, "ease_in_out"),
                )
            )
        pantry_list.update()

    def add_ingredient(e):
        """Add ingredient to the pantry."""
        ingredient = ingredient_input.value.strip()
        if ingredient:
            pantry_manager.add_to_pantry(ingredient)
            ingredient_input.value = ""
            ingredient_input.update()
            feedback_text.value = f"'{ingredient.capitalize()}' added!"
            feedback_text.color = ft.colors.GREEN
            feedback_text.update()
            update_pantry()
            clear_feedback()

    def remove_ingredient(ingredient):
        """Remove ingredient from the pantry."""
        pantry_manager.remove_from_pantry(ingredient)
        feedback_text.value = f"'{ingredient.capitalize()}' removed!"
        feedback_text.color = ft.colors.RED
        feedback_text.update()
        update_pantry()
        clear_feedback()

    def clear_feedback():
        """Clear feedback message."""
        feedback_text.value = ""
        feedback_text.update()

    # Layout
    page.add(
        ft.Column(
            [
                ft.Text("Pantry Manager", size=28, weight="bold", text_align=ft.TextAlign.CENTER),
                feedback_text,
                ft.Row(
                    [
                        ingredient_input,
                        ft.ElevatedButton(
                            "Add",
                            on_click=add_ingredient,
                            bgcolor="green",
                            color="white",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(height=20, thickness=2),
                ft.Text("Your Pantry", size=22, weight="bold"),
                ft.Container(
                    content=pantry_list,
                    bgcolor=ft.colors.LIGHT_GREEN_50,  
                    border_radius=10,
                    padding=10,
                    height=460, 
                    shadow=ft.BoxShadow(
                        blur_radius=8, spread_radius=2, color=ft.colors.BLACK12
                    ),
                ),
            ],
            expand=True,
        )
    )

    update_pantry() # Update pantry on initialization

ft.app(target=main)


