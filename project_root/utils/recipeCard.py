import flet as ft
from flet import *

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
                                        ft.Icon(name=ft.icons.LOCATION_PIN, size=22, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['origin']}", size=15),
                                    ],
                                    spacing=2,
                                ),

                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.LOCAL_FIRE_DEPARTMENT, size=22, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['difficulty']}", size=15),
                                    ],
                                    spacing=2,
                                ),
                                
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.TIMER, size=22, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['prep_time']} minutes", size=15),
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
                                        ft.Icon(name=ft.icons.LOCAL_FIRE_DEPARTMENT, size=20, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['difficulty']}", size=12),
                                    ],
                                    spacing=2,
                                ),
                                
                                ft.Row(
                                    controls=[
                                        ft.Icon(name=ft.icons.TIMER, size=20, color=ft.colors.BLUE_300),
                                        ft.Text(f"{self.__recipe['prep_time']} minutes", size=12),
                                    ],
                                    spacing=2,
                                ),
                            ],
                            spacing=1,
                        ),
                    ],
                    spacing=10
                ),  # Ensure content is a single Control
                padding=7,
                width=140,
                height=270,
            ),
            elevation=3
        )

        return self.__cardView


#This class is responsible for showing the recipe cards into a container
#It is dependent on a container
class DisplayRecipesfromSearch:
    def __init__(self, container, filteredList):
        self.filteredList = filteredList
        self.__container = container

        #just a check to make sure that the container column exists 
        if self.__container.content is None:
            self.__container.content = ft.Column(scroll=ft.ScrollMode.ALWAYS)

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    #checks what recipes should be added as a recipe card
    #updates tjhe mutable recipelist to only include what can be found in the filteredlist
    def filterCheck(self, recipeList):
        originlist = []
        difficultylist = []
        preptimelist = []
        templist = []
        print(f"FILTERED LIST O: {self.filteredList['originrecipes']}")
        print(f"FILTERED LIST D: {self.filteredList['difficultyrecipes']}")
        print(f"FILTERED LIST P: {self.filteredList['preptimerecipes']}")

        #first set of checks to add to the respective lists if the mutable list is not empty
        if self.filteredList['originrecipes'] != []:
            for recipe in recipeList['value']:
                if recipe['preprocessedname'] in self.filteredList['originrecipes']:
                    originlist.append(recipe) #add the recipes data to the templsit

        if self.filteredList['difficultyrecipes'] != []:
            for recipe in recipeList['value']:
                if recipe['preprocessedname'] in self.filteredList['difficultyrecipes']:
                    difficultylist.append(recipe) #add the recipes data to the templsit

        if self.filteredList['preptimerecipes'] != []:
            for recipe in recipeList['value']:
                if recipe['preprocessedname'] in self.filteredList['preptimerecipes']:
                    preptimelist.append(recipe)

        #second set of checks to replace the lists if empty so they can be checked for intersection later
        if self.filteredList['originrecipes'] == []:
            originlist = recipeList['value']
        
        if self.filteredList['difficultyrecipes'] == []:
            difficultylist = recipeList['value']

        if self.filteredList['preptimerecipes'] == []:
            preptimelist = recipeList['value']
        
        #get the intersection of te results from each filter to allow for multifitler checking
        templist = self.intersection(originlist, difficultylist)
        templist = self.intersection(templist, preptimelist)

        return templist
    
    def updateRecipeCards(self, recipeList):
        self.__container.content.controls.clear()  #clear old recipes
        newlist = self.filterCheck(recipeList)

        animated_controls = []
        for recipe in newlist:
            newCard = RecipeCard(recipe)
            animated_card = ft.AnimatedSwitcher(
                content=newCard.getCardView(),
                duration=400,
                transition=ft.AnimatedSwitcherTransition.FADE,
            )
            animated_controls.append(animated_card)

        self.__container.content.controls = animated_controls
        self.__container.content.update()  # Refresh the UI