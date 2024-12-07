import flet as ft
from flet import *

def get_home_view(page: ft.Page):
    page.title = "HomePage"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    #iphone16pro? size
    page.window.width = 440
    page.window.height = 956
    page.window.resizable = False

    return ft.View(
        route="/", #serves as the fdefault route
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Welcome to the Recipe App!"),
                    ft.TextButton(
                        text="Go to All Recipes View",
                        on_click=lambda _: page.go("/allrecipesview")
                    ),
                    ft.TextButton(
                        text="Go to Recipes You can Cook View",
                        on_click=lambda _: page.go("/cancookrecipesview")
                    )
                ],
                margin=10,
            ),

        ]
    )
