import flet as ft
from flet import *
from components.allrecipeview.allRecipeViewUI import *
from components.cancookrecipeview.canCookRecipeViewUI import *
from components.homepage.homepage import *

def main(page: ft.Page):
    page.title = "Recipe App"
    
    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()

        if page.route == "/":
            page.views.append(get_home_view(page))
        elif page.route == "/allrecipesview":
            page.views.append(get_allrecipesview(page))
        elif page.route == "/cancookrecipesview":
            page.views.append(get_cancookrecipesview(page))
        
        page.update()

    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    #Default Route is the HomePage
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main)

