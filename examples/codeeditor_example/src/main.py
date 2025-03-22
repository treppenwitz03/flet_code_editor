import flet as ft

from codeeditor import CodeEditor, EditorTheme


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        CodeEditor(
            expand=True,
            editor_theme=EditorTheme.DARK,
            font_size=36,
            gutter_width=150
        )
    )


ft.app(main)
