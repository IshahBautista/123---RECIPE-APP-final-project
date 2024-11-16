import flet as ft 
from flet import *

import json 

file_path = r'D:\SCHOOL\1STSEM_2NDYR\CMSC123\FINALPROJECT\projectFiles\recipesAll.json'
with open(file_path, 'r') as file: 
    recipes_data = json.load(file)
    #recipe data has been loaded

class CustomSearchBar(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.anchor = None  

    def build(self):
        def close_anchor(e: ControlEvent):
            text = f"{e.control.data}" 
            print(f"Closing view from {text}")
            self.anchor.close_view(text)

        def handle_change(e: ControlEvent):
            print(f"handle_change e.data: {e.data}")

        def handle_submit(e: ControlEvent):
            print(f"handle_submit e.data: {e.data}")

        def handle_tap(e):
            print(f"handle_tap")
            self.anchor.open_view()

        self.anchor = ft.SearchBar(
            view_elevation=4,
            divider_color=ft.colors.AMBER,
            bar_hint_text="Search colors...",
            view_hint_text="Choose a color from the suggestions...",
            on_change=handle_change,
            on_submit=handle_submit,
            on_tap=handle_tap,
            controls=[
                ft.ListTile(                
                    title=ft.Text(recipe['name']), #for what will be shown in the last
                    on_click=close_anchor, 
                    data = recipe['name'] #for e.control.data
                )
                for recipe in recipes_data
            ],
        )
        return self.anchor

def main(page: Page):
    page.title = "Search Bar"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    customSearchBar = CustomSearchBar()
    #page layout here
    page.add(
        ft.Column(
            [
                customSearchBar
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(main)