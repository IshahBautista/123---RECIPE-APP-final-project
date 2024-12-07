import flet as ft
from flet import *
from utils.searchBarUI import CustomSearchBar
from utils.recipeCard import *
from utils.filtersView import * 
from utils.header import Header
from services.filters.filterReceiver import filterReceiver
from config import updatePantryCaller, updateRecipeCaller

#All Recipes
def get_allrecipesview(page: ft.Page):
    page.title = "All Recipes View"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    #iphone16pro? size
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    #these are to update in the case of adding a new recipe, adding to pantry, etc.
    recipes_data = updateRecipeCaller() #updates the recipe data

    #use a mutable object (dictionary) so that its value can be
    #carried over across the different files and classes
    recipeListMutable = {"value": recipes_data}
    activeFilterListMutable = {"origin": [],
                             "difficulty": [],
                             "preptime": None} 
    filteredRecipeListMutable = {"originrecipes": [],
                             "difficultyrecipes": [],
                             "preptimerecipes": []} 


    def initializeRecipeCards(recipeList):
            recipeListCards = []
            for recipe in recipeList["value"]:
                newCard = RecipeCard(recipe)
                recipeListCards.append(newCard.getCardView())
            
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

    displayrecipes = DisplayRecipesfromSearch(RecipeContainer, filteredRecipeListMutable) #from file recipeCard.py
    recipeSearchBar = CustomSearchBar(recipeListMutable, displayrecipes, activeFilterListMutable) #from file searchBar.py
    
    # for the filters 
    #make the receiver
    receiver = filterReceiver(activeFilterListMutable, recipeListMutable, filteredRecipeListMutable, displayrecipes)

    allfilteroptions = FilterOptions()
    originType = FilterType("Origin", allfilteroptions.getOriginOptions())
    originFilter = SelectionFilter(originType, receiver)
    difficultyType = FilterType("Difficulty", ["Easy", "Moderate", "Intermediate", "Advanced", "Expert"])
    difficultyFilter = SelectionFilter(difficultyType, receiver)
    preptimeFilter = SliderFilter(receiver)

    # contains the dropdown for the filters
    FilterContainer = ft.Container(
        width=400,
        height=170,
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
                        originFilter.build(), #object
                    ],
                ),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.LOCAL_FIRE_DEPARTMENT,
                            size=30,
                            color=ft.colors.BLUE_500,
                            
                        ),
                        difficultyFilter.build(), #object
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
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    allrecipeHeader = Header("All Recipes", page)

    return ft.View(
        route="/allrecipesview",
        controls=[
            ft.Column(
                controls=[
                    allrecipeHeader.build(),
                    ft.Row(
                        controls=[recipeSearchBar], #object
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    FilterContainer, 
                    ft.Divider(),
                    RecipeContainer,
                ]
            )
        ]
    )