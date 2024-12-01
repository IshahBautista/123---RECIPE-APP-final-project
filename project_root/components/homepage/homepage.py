import flet as ft
from flet import *
from utils.recipeCard import *
from utils.filtersView import * 
from utils.navButton import NavigationButton

class RecipeContainer:
    def __init__(self, RecipeListCards):
        self.__recipeListCards = RecipeListCards
        self.container = self.build()

    def build(self):
        self.container = ft.Container(
            width=420,
            height=250,
            padding=10,
            margin=0,
            border_radius=20,
            content=ft.Row(
                scroll=ft.ScrollMode.ALWAYS,
                spacing=3,
                controls=self.__recipeListCards
            )
        )

        return self.container

def get_home_view(page: ft.Page):
    page.title = "HomePage"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    def initializeRecipeCards(recipeList):
            recipeListCards = []
            for recipe in recipeList:
                newCard = RecipeCardHorizontal(recipe)
                recipeListCards.append(newCard.getCardView())
                print("Card views appended successfully!")
            
            return recipeListCards
    
    #initialize the objects and components being used
    recipeListCards = initializeRecipeCards(recipes_data)

    #scrollable recipe containers
    Container1 = RecipeContainer(recipeListCards).container
    Container2 = RecipeContainer(recipeListCards).container

    addRecipeButton = NavigationButton(ft.icons.ADD_ROUNDED, "/add_recipeview", page)
    pantryButton = NavigationButton(ft.icons.KITCHEN, "/pantryview", page)
    surpriseButton = NavigationButton(ft.icons.SOUP_KITCHEN_SHARP, "/specific_recipeview", page)

    #is where the navigation buttons are kept
    NavButtonContainer = ft.Container(
        width=400,
        height=100,
        padding=2,
        margin=0,
        border_radius=20,
        content=ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                addRecipeButton.build(),
                pantryButton.build(),
                surpriseButton.build(),
            ]
        ),
        alignment=ft.alignment.center
    )

    #this contains the 2 recipe containers
    BottomBar = ft.Container(
        width=400,
        padding=5,
        margin=0,
        border_radius=20,
        content=ft.Column(
            controls=[
                 #container for the recipes the user can cook rn
                 ft.Container(
                    bgcolor=ft.colors.GREY_100,
                    border_radius=15,
                    padding=5,
                    content=
                    ft.Column(
                        controls=[
                            ft.Text(
                                value='Recipes you Can Cook',
                                size=30,
                                style=ft.TextStyle(
                                    color=ft.colors.GREY_800,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),

                            Container1, #contains the recipe cards

                            ft.TextButton(
                                text="View All",
                                on_click=lambda _: page.go("/cancookrecipesview"),
                                icon=ft.icons.ARROW_DROP_DOWN,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                    ),
                 ),

                #container for all the recipes 
                ft.Container(
                    bgcolor=ft.colors.GREY_100,
                    border_radius=15,
                    padding=5,
                    content=
                    ft.Column(
                        controls=[
                            ft.Text(
                                value='All Recipes',
                                size=30,
                                style=ft.TextStyle(
                                    color=ft.colors.GREY_800,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),

                            Container2, #contains the recipe cards

                            ft.TextButton(
                                text="View All",
                                on_click=lambda _: page.go("/allrecipesview"),
                                icon=ft.icons.ARROW_DROP_DOWN,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                    ),
                 ),

            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        )
    )

    return ft.View(
        route="/",  # serves as the default route
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        padding=5,
                        alignment=ft.alignment.center,
                        content=ft.Row(
                             height=50,
                             controls=[
                                  
                             ]
                        )
                    ),
                    ft.Divider(
                        thickness=3,
                    ),
                    # Format the Buttons for navigation to pantry, surprise me, and add recipes
                    NavButtonContainer,
                    BottomBar,
                ],
            ),
        ]
    )
