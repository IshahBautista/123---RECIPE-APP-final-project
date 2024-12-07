import flet as ft
from flet import *

class SelectionChip(ft.UserControl):
    def __init__(self, chipname: str, receiver, type):
        super().__init__()
        self._receiver = receiver
        self._type = type
        self.chipname = chipname
        self.selected = False  
        self.container = self.build  
        self.widthval = 70
        # change the width of the chip if the string length is too long
        if len(self.chipname) > 7:
            self.widthval = 100
        elif len(self.chipname) > 14:
            self.widthval = 200

    def build(self):
        def toggle_button(e: ft.ControlEvent):
            self.selected = not self.selected
            self.container.bgcolor = ft.colors.GREEN_300 if self.selected else ft.colors.WHITE10
            self.container.border = (ft.border.all(1, ft.colors.GREEN_600)) if self.selected else (ft.border.all(1, ft.colors.GREY_400)) 
            if self.selected:
                print(f"{self.chipname} pressed!")
                self._receiver.appendActiveFilter(self.chipname, self._type)
            else:
                print(f"{self.chipname} unpressed!") 
                self._receiver.removeActive(self.chipname, self._type)
            self.update()

        self.container = ft.Container(
            content=ft.Text(self.chipname),
            padding=5,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE10,
            width= self.widthval,
            height=35,
            border_radius=20,
            border=ft.border.all(1, ft.colors.GREY_400),
            on_click=toggle_button,
        )

        return self.container