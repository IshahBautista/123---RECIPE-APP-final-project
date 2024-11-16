import flet as ft
from flet import *
from searchBarUI import CustomSearchBar

def main(page: ft.Page):
    page.title = "All Recipes View"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    recipeSearchBar = CustomSearchBar()

    FilterContainer = ft.Container(
        width=400,
        height=150,
        padding=10,
        margin=5,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
    )

    RecipeContainer = ft.Container(
        width=400,
        height=600,
        padding=10,
        margin=5,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[recipeSearchBar],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                FilterContainer,
                RecipeContainer
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
