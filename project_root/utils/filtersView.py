import flet as ft
from flet import *
from .selectionChip import SelectionChip
from config import json_path, recipes_data

class FilterType:
    def __init__(self, filterName: str, filterOptions: list[str]):
        self.__filterName = filterName
        self.__filterOptions = filterOptions

    def getfilterName(self):
        return self.__filterName

    def getfilterOptions(self):
        return self.__filterOptions

class SelectionFilter(ft.Control):
    def __init__(self, filterType: FilterType):
        super().__init__()
        self.__filterType = filterType
        self.__cardsList = [SelectionChip(filteroption) for filteroption in self.__filterType.getfilterOptions()]
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
    def __init__(self):
        super().__init__()
        self.filterslider = None
    
    def build(self):
        def handle_change(e: ControlEvent):
            pass

        self.filterslider = ft.Container(
            width=350,
            border_radius=10,
            content=ft.Slider(
                        width=400,
                        min=5,
                        max=90,
                        divisions=17,
                        label="≤ {value} mins.",
                        on_change=handle_change,
                        active_color=ft.colors.BLUE_500
                    )
        )
        
        return self.filterslider
    
class FilterOptions:
    def __init__(self):
        self.__OriginOptions = []
        self.setOptions()

    def setOptions(self):
        for recipe in recipes_data:
            if recipe["origin"] not in self.__OriginOptions:
                self.__OriginOptions.append(recipe["origin"])

        self.__OriginOptions.sort()

    def getOriginOptions(self):
        return self.__OriginOptions

