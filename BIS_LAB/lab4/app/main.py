
import flet as ft
import lab1
import lab3
import lab5

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
                ft.Text('Выберете необходимы вам расчёт: ', text_align='center', weight='bold', size=20),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


    def data_input(data, type):
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                ", ".join(map(lambda f: f.name, e.files)) if e.files else "Нет файла!!!"
            )
            selected_files.update()

        def get_directory_result(e: ft.FilePickerResultEvent):
            selected_files.value = e.path if e.path else "Нет папки с файлами!!!"
            selected_files.update()

        if type == 0:
            pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
            selected_files = ft.Text()
            for i in page.overlay:
                page.overlay.pop()
            page.overlay.append(pick_files_dialog)
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
        else:
            pick_files_dialog = ft.FilePicker(on_result=get_directory_result)
            selected_files = ft.Text()
            for i in page.overlay:
                page.overlay.pop()
            page.overlay.append(pick_files_dialog)
            f = ft.Row(
                [
                    ft.ElevatedButton(
                        "Папка с файлами:",
                        icon=ft.icons.UPLOAD_FILE,
                        on_click=lambda _: pick_files_dialog.get_directory_path(
                        ),
                    ),
                    selected_files,
                ],
            )

        d = ft.Text(data, text_align='center', weight='bold', size=20)



        def calc(e):
            if d.value == 'Оценка стоимости информационных\nресурсов предприятия':
                answer = lab1.calc1(selected_files.value)
                input_data.visible = True
                answer_print.visible = True
                answer_print.value = answer
                input_data.update()
                answer_print.update()

            elif d.value == 'Оценка частот возникновения угроз\nинформационной безопасности':
                answer = lab3.calc2(selected_files.value)
                input_data.visible = True
                answer_print.visible = True
                answer_print.value = 'Результат в файле: '+answer
                input_data.update()
                answer_print.update()
            else:
                answer = lab5.calc3(selected_files.value)
                input_data.visible = True
                answer_print.visible = True
                answer_print.value = answer
                input_data.update()
                answer_print.update()

        r = ft.ElevatedButton(content=ft.Text('Рассчёт: ', text_align='center', weight='bold', size=20), on_click=calc)
        input_data = ft.Text('Результат расчёта: ', text_align='center', weight='bold', size=20, visible=False)
        answer_print = ft.Text(weight='bold', size=12, visible=False)
        col = ft.Row(controls=[
            ft.Container(content=ft.Column(controls=[d, f, r], alignment=ft.MainAxisAlignment.START), height=2100),
            ft.Container(content=ft.Column(controls=[input_data, answer_print], alignment=ft.MainAxisAlignment.START),
                         width=600, height=2100),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        page.add(col)

    def change_navigation_destination(e):
        if e.control.selected_index == 0:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Оценка стоимости информационных\nресурсов предприятия', 1)
        elif e.control.selected_index == 1:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Оценка частот возникновения угроз\nинформационной безопасности', 1)
        else:
            while len(page.controls) != 0:
                page.controls.pop()
            data_input('Расчёт вероятностей реализации угроз\nинформационной безопасности', 0)


    # navigation bar
    page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label="Оценка стоимости информационных\nресурсов предприятия"),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label="Оценка частот возникновения угроз\nинформационной безопасности"),
                ft.NavigationDestination(icon=ft.icons.EDIT_NOTE,
                                         label='Расчёт вероятностей реализации угроз\nинформационной безопасности')
            ],
            height=90,
            on_change=lambda e: change_navigation_destination(e),
    )
    page.update()


ft.app(target=main)