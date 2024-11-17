import flet as ft
from flet import *
from searchBarUI import CustomSearchBar
from recipeCard import RecipeCard


# NEED TO CONNECT THE SEARCH BAR TO THE DISPLAY RECIPE SOMEHOW? 

class DisplayRecipesfromSearch:
    def __init__(self, container):
        self.__container = container

    def updateRecipeCards(self, recipeList):
        self.__container.controls.clear()  # Clear old recipes
        for recipe in recipeList:
            newCard = RecipeCard(recipe)
            self.__container.controls.append(newCard.getCardView())
        self.__container.update()  # Refresh the UI


def main(page: ft.Page):
    page.title = "All Recipes View"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    RecipeContainer = ft.Container(
        width=400,
        height=600,
        padding=10,
        margin=5,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
        content=ft.Column(scroll=ft.ScrollMode.ALWAYS)
    )

    recipeSearchBar = CustomSearchBar()

    FilterContainer = ft.Container(
        width=400,
        height=150,
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
