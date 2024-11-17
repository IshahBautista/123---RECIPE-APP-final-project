import flet as ft
from flet import *

class RecipeCard:
    def __init__(self, recipe):
        self.__cardView = None
        self.__recipe = recipe
        self.build()
    
    def getCardView(self):
        return self.__cardView
    
    def build(self):
        self.cardView = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(f"{self.__recipe['name']}", size=35, weight=FontWeight.BOLD),
                        ft.Text(f"Origin: {self.__recipe['origin']}", size=20),
                        ft.Text(f"Difficulty: {self.__recipe['difficulty']}", size=20),
                        ft.Text(f"Prep Time: {self.__recipe['prep_time']}", size=20),
                    ],
                    spacing=5,
                ),
                padding=15
            )
        )
        return self.cardView   

