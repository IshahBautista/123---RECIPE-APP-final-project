import flet as ft
from flet import *
from abc import ABC, abstractmethod
from config import json_path, recipes_data

#This class is the recipe card itself
#Containing the specific details of a recipe
#One instance/object of this is made per recipe
class RecipeCard:
    def __init__(self, recipe):
        self.__recipe = recipe
        self.__cardView = self.build()
    
    def getCardView(self):
        return self.__cardView
    
    def build(self):
        self.__cardView = ft.Card(
            content=ft.Container(
                content=ft.Row(  # Wrap the list in a Row or Column
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.AMBER_300,
                            width=150,
                            border_radius=8,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(value=f"{self.__recipe['name']}", 
                                        size=20, 
                                        weight=FontWeight.BOLD,
                                        width=170,
                                        overflow=ft.TextOverflow.FADE,
                                        max_lines=2,                                
                                        ),
                                
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.LOCATION_PIN, size=23, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['origin']}", size=15),
                                    ],
                                    spacing=2,
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.LOCAL_FIRE_DEPARTMENT, size=25, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['difficulty']}", size=15),
                                    ],
                                    spacing=2,
                                ),
                                
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.TIMER, size=25, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['prep_time']}", size=15),
                                    ],
                                    spacing=2,
                                ),
                            ],
                            spacing=1,
                        ),
                    ],
                    spacing=10
                ),  # Ensure content is a single Control
                padding=10,
                width=360,
                height=180,
            ),
            elevation=3
        )

        print(f"cardview made for {self.__recipe['name']}")
        return self.__cardView


class RecipeCardHorizontal:
    def __init__(self, recipe):
        self.__recipe = recipe
        self.__cardView = self.build()
    
    def getCardView(self):
        return self.__cardView
    
    def build(self):
        self.__cardView = ft.Card(
            content=ft.Container(
                content=ft.Column(  # Wrap the list in a Row or Column
                    controls=[
                        ft.Container(
                            bgcolor=ft.colors.AMBER_300,
                            width=140,
                            height=100,
                            border_radius=8,
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(value=f"{self.__recipe['name']}", 
                                        size=17, 
                                        weight=FontWeight.BOLD,
                                        ),
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.LOCAL_FIRE_DEPARTMENT, size=23, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['difficulty']}", size=12),
                                    ],
                                    spacing=2,
                                ),

                                
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.TIMER, size=23, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['prep_time']}", size=12),
                                    ],
                                    spacing=2,
                                ),
                            ],
                            spacing=1,
                        ),
                    ],
                    spacing=10
                ),  # Ensure content is a single Control
                padding=5,
                width=140,
                height=270,
            ),
            elevation=3
        )

        print(f"cardview made for {self.__recipe['name']}")
        return self.__cardView


#This class is responsible for showing the recipe cards into a container
#It is dependent on a container
class DisplayRecipesfromSearch:
    def __init__(self, container):
        self.__container = container

        #just a check to make sure that the container column exists 
        if self.__container.content is None:
            self.__container.content = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    def updateRecipeCards(self, recipeList):
        self.__container.content.controls.clear()  #clear old recipes
        for recipe in recipeList["value"]:
            newCard = RecipeCard(recipe)
            self.__container.content.controls.append(newCard.getCardView())
            print("Card views appended successfully!")
            
        self.__container.content.update()  # Refresh the UI