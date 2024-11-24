import flet as ft
from flet import *

class SelectionChip(ft.UserControl):
    def __init__(self, chipname: str):
        super().__init__()
        self.chipname = chipname
        self.selected = False  # Track selection state
        self.container = None  # Store reference to container
        self.widthval = 70
        # change the width of the chip if the string length is too long
        if len(self.chipname) > 7:
            self.widthval = 100

    def build(self):
        def toggle_button(e: ft.ControlEvent):
            self.selected = not self.selected
            self.container.bgcolor = ft.colors.GREEN_400 if self.selected else ft.colors.WHITE10
            self.container.border = (ft.border.all(2, ft.colors.GREEN_500)) if self.selected else (ft.border.all(2, ft.colors.GREY_400)) 
            print("Chip Pressed!")
            self.update()

        self.container = ft.Container(
            content=ft.Text(self.chipname),
            padding=5,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE10,
            width= self.widthval,
            height=35,
            border_radius=20,
            border=ft.border.all(2, ft.colors.GREY_400),
            on_click=toggle_button,
        )
        
        return self.container