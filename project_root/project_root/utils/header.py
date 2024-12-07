import flet as ft
from flet import Container, IconButton, Text, Page

class Header:
    def __init__(self, titleName:str, page:ft.Page):
        self.__titleName = titleName
        self.__page = page
        self.header = None

    def build(self):
        self.header = ft.Container(
                width=440,
                height=70,
                margin=0,
                padding=0,
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK,
                            icon_color=ft.colors.GREY_800,
                            icon_size=25,
                            on_click=lambda _: self.__page.go('/'),
                        ),
                        ft.Text(
                            value=self.__titleName,
                            size=25,
                            style=ft.TextStyle(
                                color= ft.colors.GREY_800,
                                weight=ft.FontWeight.BOLD
                            )
                        )
                    ],
                    alignment=ft.CrossAxisAlignment.START,
                )
            )
        return self.header
