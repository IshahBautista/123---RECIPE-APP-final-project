import flet as ft
from flet import Container

class NavigationButton:
    def __init__(self, icon: str, destination: str, page: ft.Page):
        self.__icon = icon
        self.__destination = destination
        self.__page = page
        self.navbutton = self.build 

    def buttonPressed(self, e):
        self.__page.go(self.__destination)

    def mouseHover(self, e):
        # Toggle background color on hover
        self.navbutton.bgcolor = ft.colors.BLUE_100 if e.data == "true" else ft.colors.GREY_200
        self.navbutton.border = (ft.border.all(3, ft.colors.BLUE_400)) if e.data == "true" else (ft.border.all(3, ft.colors.GREY_400))
        self.navbutton.content = (ft.Icon(self.__icon, color=ft.colors.WHITE, size=40)) if e.data == "true" else (ft.Icon(self.__icon, color=ft.colors.BLUE_300, size=40))
        self.navbutton.update() 

    def build(self):
        # Create the button
        self.navbutton = ft.Container(
            width=90,
            height=90,
            border_radius=10,
            bgcolor=ft.colors.GREY_200,
            border=ft.border.all(3, ft.colors.GREY_400),
            on_click=self.buttonPressed,  
            on_hover=self.mouseHover,  
            content=ft.Icon(self.__icon, color=ft.colors.BLUE_300, size=40),
        )

        return self.navbutton
