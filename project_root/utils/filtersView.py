import flet as ft
from flet import *
from .selectionChip import SelectionChip
from config import updatePantryCaller, updateRecipeCaller

class FilterType:
    def __init__(self, filterName: str, filterOptions: list[str]):
        self.__filterName = filterName
        self.__filterOptions = filterOptions

    def getfilterName(self):
        return self.__filterName

    def getfilterOptions(self):
        return self.__filterOptions

class SelectionFilter(ft.Control):
    def __init__(self, filterType: FilterType, receiver):
        super().__init__()
        self.receiver = receiver 
        self.filterType = filterType
        self.__cardsList = [SelectionChip(filteroption, self.receiver, self.filterType) for filteroption in self.filterType.getfilterOptions()]
        self.filterS = self.build()

    def build(self):
        self.filterS = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            width=350,
            height=50,
            spacing=5,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[card for card in self.__cardsList],
        )

        return self.filterS

class SliderFilter(ft.Control):
    def __init__(self, receiver):
        super().__init__()
        self.receiver = receiver
        self.filterslider = None
    
    def build(self):
        def handle_change(e: ControlEvent):
            print(f"value: {e.data}")
            self.receiver.setPrepTimeFilter(e.data)

        self.filterslider = ft.Container(
            width=350,
            border_radius=10,
            content=ft.Slider(
                        width=400,
                        min=5,
                        max=90,
                        divisions=17,
                        label="≤ {value} mins.",
                        on_change_end=handle_change,
                        active_color=ft.colors.BLUE_500
                    )
        )
        
        return self.filterslider
    
class FilterOptions:
    def __init__(self):
        self.__OriginOptions = []
        self.recipes_data = updateRecipeCaller() #updates the recipe data
        self.setOptions()

    def setOptions(self):
        for recipe in self.recipes_data:
            if recipe["origin"] not in self.__OriginOptions:
                self.__OriginOptions.append(recipe["origin"])

        self.__OriginOptions.sort()

    def getOriginOptions(self):
        return self.__OriginOptions

