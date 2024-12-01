import flet as ft
from flet import *
from utils.searchBarUI import CustomSearchBar
from utils.recipeCard import *
from utils.filtersView import * 
from utils.header import Header
from config import json_path, recipes_data

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
    recipeListMutable = {"value": recipes_data}

    def initializeRecipeCards(recipeList):
            recipeListCards = []
            for recipe in recipeList["value"]:
                newCard = RecipeCard(recipe)
                recipeListCards.append(newCard.getCardView())
                print("Card views appended successfully!")
            
            return recipeListCards
    
    recipeListCards = initializeRecipeCards(recipeListMutable)

    #Contians the cards for the recipes
    RecipeContainer = ft.Container(
        width=400,
        height=540,
        padding=10,
        margin=2,
        border_radius=20,
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=3,
            controls=recipeListCards
            )
    )   

    displayrecipes = DisplayRecipesfromSearch(RecipeContainer)
    recipeSearchBar = CustomSearchBar(recipeListMutable, displayrecipes)
    
    # for the filters 
    allfilteroptions = FilterOptions()
    originType = FilterType("Origin", allfilteroptions.getOriginOptions())
    originFilter = SelectionFilter(originType)
    difficultyType = FilterType("Difficulty", ["Easy", "Moderate", "Intermediate", "Advanced", "Expert"])
    difficultyFilter = SelectionFilter(difficultyType)
    preptimeFilter = SliderFilter()

    # contains the dropdown for the filters
    FilterContainer = ft.Container(
        width=400,
        height=145,
        padding=5,
        margin=2,
        border_radius=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.LOCATION_PIN,
                            size=30,
                            color=ft.colors.BLUE_500,
                            
                        ),
                        originFilter.build(),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.LOCAL_FIRE_DEPARTMENT,
                            size=30,
                            color=ft.colors.BLUE_500,
                            
                        ),
                        difficultyFilter.build(),
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.TIMER,
                            size=30,
                            color=ft.colors.BLUE_500,
                            
                        ),
                        preptimeFilter.build(),
                    ],
                ),
            ],
            spacing=0,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    cancookrecipeHeader = Header("What you can cook", page)

    viewPage = ft.View(
        route="/cancookrecipesview",
        controls=[
            ft.Column(
                controls=[
                    cancookrecipeHeader.build(),
                    ft.Divider(),
                    ft.Row(
                        controls=[recipeSearchBar],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    FilterContainer,
                    ft.Divider(),
                    RecipeContainer,
                ]
            )
        ]
    )

    return viewPage