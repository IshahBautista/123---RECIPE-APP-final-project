import flet as ft
from flet import *
from utils.searchBarUI import CustomSearchBar
from utils.recipeCard import *
from utils.filtersView import * 
    
#can cook Recipes
def get_cancookrecipesview(page: ft.Page):
    page.title = "Can Cook Recipe View"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    #iphone16pro? size
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    #use a mutable object (dictionary) so that its value can be
    #carried over across the different files and classes
    recipeListMutable = {"value": None}

    #Contians the cards for the recipes
    RecipeContainer = ft.Container(
        width=400,
        height=500,
        padding=10,
        margin=5,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=3,
            )
    )   

    displayrecipes = DisplayRecipesfromSearch(RecipeContainer)
    recipeSearchBar = CustomSearchBar(recipeListMutable, displayrecipes)
    
    #for the filters 
    allfilteroptions = FilterOptions()
    originType = FilterType("Origin", allfilteroptions.getOriginOptions())
    originFilter = DropDownFilter(originType)
    difficultyType = FilterType("Difficulty", allfilteroptions.getDifficultyOptions())
    difficultyFilter = DropDownFilter(difficultyType)
    preptimeFilter = SliderFilter()

    #contains the dropdown for the filters
    FilterContainer = ft.Container(
        width=400,
        height=250,
        padding=10,
        margin=5,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
        content=ft.Column(
            controls=[
                originFilter.build(),
                difficultyFilter.build(),
                preptimeFilter.build(),
            ]
        )
    )

    Header = ft.Container(
        width=400,
        height=60,
        padding=10,
        margin=5,
        border_radius=15,
        bgcolor=ft.colors.GREY_100,
        content=ft.Row(
            controls=[

            ]
        )
    )

    return ft.View(
        route="/cancookrecipesview",
        controls=[
            Header,
            ft.Row(
                controls=[recipeSearchBar],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            FilterContainer,
            RecipeContainer
        ]
    )