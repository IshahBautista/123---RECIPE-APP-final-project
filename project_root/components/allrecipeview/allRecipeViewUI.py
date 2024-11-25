import flet as ft
from flet import *
from utils.searchBarUI import CustomSearchBar
from utils.recipeCard import *
from utils.filtersView import * 
    
#All Recipes
def get_allrecipesview(page: ft.Page):
    page.title = "All Recipes View"
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
        height=510,
        padding=10,
        margin=2,
        border_radius=20,
        bgcolor=ft.colors.GREY_200,
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            spacing=3,
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
                preptimeFilter.build(),
            ],
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

    Header = ft.Container(
        width=440,
        height=50,
        margin=0,
        padding=10,
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color=ft.colors.GREY_800,
                    icon_size=25,
                ),
                ft.Text(
                    value='All Recipes',
                    size=25,
                    style=ft.TextStyle(
                        color= ft.colors.GREY_800,
                        font_family=ft.FontWeight.BOLD
                    )
                )
            ],
            alignment=ft.CrossAxisAlignment.START,
        )
    )

    return ft.View(
        route="/allrecipesview",
        controls=[
            ft.Column(
                controls=[
                    Header,
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