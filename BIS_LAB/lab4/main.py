
import flet as ft


def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.GREEN,
    )
    page.title = "БИАС 4"
    page.theme_mode = "light"
    page.window_maximized = True
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = "always"
    # navigation appbar
    page.appbar = ft.AppBar(
        leading=ft.Row([ft.Container(width=4)]),
        leading_width=60,
        title=ft.Text("Инструментальный комплекс оценок", color="#FFFFFF"),
        center_title=False,
        bgcolor=ft.colors.GREEN_400,
        actions=[
            ft.Container(width=10)
        ],
    )
    page.add(
        ft.Column(
            [
                ft.Text('Нажмите кнопку:', text_align='center', weight='bold', size=20),
                ft.Text('(Выберите файлы для соответствующих расчётов\n или воспользуйтесь файлами по умолчанию)', text_align='center', size=15),
                ft.ElevatedButton(content=ft.Text('Расчёт', text_align='center', weight='bold', size=20))
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


    def data_input(data):
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Нет файла!!!"
            )
            print(e.files[0].path)
            selected_files.update()

        pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
        selected_files = ft.Text()
        page.overlay.append(pick_files_dialog)
        d = ft.Text(data, text_align='center', weight='bold', size=20)
        f = ft.Row(
                [
                    ft.ElevatedButton(
                        "Файл:",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.pick_files(
                            allow_multiple=True
                        ),
                    ),
                    selected_files,
                ],
        )
        r = ft.ElevatedButton(content=ft.Text('Рассчёт', text_align='center', weight='bold', size=20))
        input_data = ft.Text()
        col = ft.Row(controls=[
            ft.Container(content=ft.Column(controls=[d, f, r])),
            input_data
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        page.add(col)


    def change_navigation_destination(e):
        if e.control.selected_index == 0:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Оценка стоимости информационных\nресурсов предприятия')
        elif e.control.selected_index == 1:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Агрегирование экспертных\nоценок')
        elif e.control.selected_index == 2:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Оценка частот возникновения угроз\nинформационной безопасности')
        elif e.control.selected_index == 3:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Оценка нечётких\nпоказателей')
        else:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Расчёт вероятностей реализации угроз\nинформационной безопасности')


    # navigation bar
    page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label="Оценка стоимости информационных\nресурсов предприятия"),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label="ne vhodit Агрегирование экспертных\nоценок"),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label="Оценка частот возникновения угроз\nинформационной безопасности"),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label='ne vhodit Оценка нечётких\nпоказателей'),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label='Расчёт вероятностей реализации угроз\nинформационной безопасности')
            ],
            height=90,
            on_change=lambda e: change_navigation_destination(e),
    )
    page.update()


ft.app(target=main)