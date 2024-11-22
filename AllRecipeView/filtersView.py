import flet as ft
from flet import *
from searchBarUI import recipes_data

class FilterType:
    def __init__(self, filterName: str, filterOptions: list[str]):
        self.__filterName = filterName
        self.__filterOptions = filterOptions

    def getfilterName(self):
        return self.__filterName

    def getfilterOptions(self):
        return self.__filterOptions

class DropDownFilter(ft.Control):
    def __init__(self, filterType: FilterType):
        super().__init__()
        self.__filterType = filterType
        self.filterdd = None

    def build(self):
        self.filterdd = ft.Dropdown(
            elevation=10,
            width=380,
            border_radius=10,
            border_color=ft.colors.GREY_400,
            bgcolor=ft.colors.GREY_300,
            color=ft.colors.GREY_900,
            padding=1,
            hint_text=self.__filterType.getfilterName(),
            hint_style=ft.TextStyle(color=ft.colors.GREY_900, 
                                    size=14),
            options=[
                ft.dropdown.Option(f"{filteroption}")
                for filteroption in self.__filterType.getfilterOptions()
            ],
        )
        return self.filterdd

class SliderFilter(ft.Control):
    def __init__(self):
        super().__init__()
        self.filterslider = None
    
    def build(self):
        def handle_change(e: ControlEvent):
            pass

        self.filterslider = ft.Container(
            width=380,
            border_radius=10,
            bgcolor=ft.colors.GREY_300,
            content=ft.Slider(
                        width=370,
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
        self.__DifficultyOptions = []
        self.__OriginOptions = []
        self.setOptions()

    def setOptions(self):
        for recipe in recipes_data:
            if recipe["origin"] not in self.__OriginOptions:
                self.__OriginOptions.append(recipe["origin"])
            
            if recipe["difficulty"] not in self.__DifficultyOptions:
                self.__DifficultyOptions.append(recipe["difficulty"])

        self.__OriginOptions.sort()

    def getOriginOptions(self):
        return self.__OriginOptions

    def getDifficultyOptions(self):
        return self.__DifficultyOptions
