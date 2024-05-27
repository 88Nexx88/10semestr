
import flet as ft
import pandas as pd

import lab1
import lab3
import lab5

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme_seed=ft.colors.BLUE,
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
        bgcolor=ft.colors.BLUE,
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


    def data_input(data, type_):
        def pick_files_result(e: ft.FilePickerResultEvent):
            selected_files.value = (
                'Файл подгружен!' if e.files else "Нет файла!!!"
            )
            # page.client_storage.set('file', e.path)
            selected_files.update()

        def get_directory_result(e: ft.FilePickerResultEvent):
            selected_files.value = 'Файлы подгружены!' if e.path else "Нет папки с файлами!!!"
            page.client_storage.set('file', e.path)
            selected_files.update()

        if type_ == 0:
            pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
            selected_files = ft.Text(weight='bold', size=20)
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
            selected_files = ft.Text(weight='bold', size=20)
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
            def headers(df: pd.DataFrame) -> list:
                return [ft.DataColumn(ft.Text(header)) for header in df.columns]

            def rows(df: pd.DataFrame) -> list:
                rows = []
                for index, row in df.iterrows():
                    check = 0
                    for i in row:
                        if type(i) == str:
                            check+=1
                    if check != len(row):
                        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(row[header])) for header in df.columns]))
                return rows

            if d.value == 'Оценка стоимости информационных\nресурсов предприятия':
                answer = lab1.calc1(page.client_storage.get('file'))
                input_data.visible = True
                answer_print.visible = True
                answer_table.rows = rows(answer)
                answer_table.columns = headers(answer)
                answer_table.update()
                input_data.update()
                answer_print.update()


            elif d.value == 'Оценка частот возникновения угроз\nинформационной безопасности':
                answer = lab3.calc2(page.client_storage.get('file'))
                input_data.visible = True
                answer_print.visible = True
                answer_table.rows = rows(answer)
                answer_table.columns = headers(answer)
                answer_table.update()
                input_data.update()
                answer_print.update()
            else:
                answer = lab5.calc3(page.client_storage.get('file'))
                input_data.visible = True
                answer_print.visible = True
                answer_tables.controls.append(ft.DataTable(columns=answer[0], rows=answer[1]))
                answer_tables.controls.append(ft.DataTable(columns=answer[2], rows=answer[3]))
                answer_tables.controls.append(ft.DataTable(columns=answer[4], rows=answer[5]))
                answer_tables.controls.append(ft.DataTable(columns=answer[5], rows=answer[6]))
                answer_tables.controls.append(ft.DataTable(columns=answer[7], rows=answer[8]))
                answer_tables.update()
                input_data.update()
                answer_print.update()

        r = ft.ElevatedButton(content=ft.Text('Рассчёт: ', text_align='center', weight='bold', size=20), on_click=calc)
        input_data = ft.Text('Результат расчёта: ', text_align='center', weight='bold', size=20, visible=False)
        answer_print = ft.Text(weight='bold', size=12, visible=False)
        answer_table = ft.DataTable()
        answer_tables = ft.Column()
        col = ft.Row(controls=[
            ft.Container(content=ft.Column(controls=[d, f, r], alignment=ft.MainAxisAlignment.START), height=3000),
            ft.Container(content=ft.Column(controls=[input_data, answer_print, answer_table, answer_tables], alignment=ft.MainAxisAlignment.START),
                         width=800, height=3000),
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