import flet as ft
from flet import *
from abc import ABC, abstractmethod

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
                content=ft.Column(
                    [
                        ft.Text(f"{self.__recipe['name']}", size=30, weight=FontWeight.BOLD),
                        ft.Text(f"Origin: {self.__recipe['origin']}", size=15),
                        ft.Text(f"Difficulty: {self.__recipe['difficulty']}", size=15),
                        ft.Text(f"Prep Time: {self.__recipe['prep_time']}", size=15),
                    ],
                    spacing=1,
                ),
                padding=15,
                width=360,
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

        if self.__container.content is None:
            self.__container.content = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    def updateRecipeCards(self, recipeList):
        self.__container.content.controls.clear()  # Clear old recipes
        for recipe in recipeList["value"]:
            newCard = RecipeCard(recipe)
            print("All card views made succesfully!")
            self.__container.content.controls.append(newCard.getCardView())
            print("Card views appended successfully!")
            
        self.__container.content.update()  # Refresh the UI