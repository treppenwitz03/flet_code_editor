import flet as ft

from codeeditor import Codeeditor


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=Codeeditor(
                    tooltip="My new Codeeditor Control tooltip",
                    value = "My new Codeeditor Flet Control", 
                ),),

    )


ft.app(main)
