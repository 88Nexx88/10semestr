from tabulate import tabulate

from calculations import calculation_mechanism_quality_indicators, calculation_probabilities_threat_realization
from data_converters import limit_sufficiency_konf, limit_sufficiency_integrity_soi, limit_sufficiency_availability, \
    limit_sufficiency_integrity

import flet as ft
def calc3(file_dir):
    all_table = []
    answer = ''
    print('\n\t\t\t Показатели качества механизмов')
    mechanism_quality_indicators = list(calculation_mechanism_quality_indicators())
    print(tabulate(mechanism_quality_indicators, tablefmt="grid"))

    all_table.append([ft.DataColumn(ft.Text(header)) for header in ['Номер', 'Показатели качества механизмов', 'Значение']])
    rows = []
    for row in mechanism_quality_indicators:
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(r)) for r in row]))
    all_table.append(rows)
    answer+='\n\t\t\t Показатели качества механизмов\n'
    answer+=tabulate(mechanism_quality_indicators, tablefmt="grid")
    answer+='\n'
    mechanism_quality_indicators_values = [i[2] for i in mechanism_quality_indicators]

    #
    # Расчет вероятностей реализации угроз конфиденциальности
    #

    print('\n\t\t\t Вероятность реализации угроз конфиденциальности')
    answer+='\n\t\t\t Вероятность реализации угроз конфиденциальности\n'
    print(tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_konf,
    ), tablefmt="grid"))
    answer+=tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_konf,
    ), tablefmt="grid")

    all_table.append(
        [ft.DataColumn(ft.Text(header)) for header in ['Номер', 'Вероятность реализации угроз конфиденциальности', 'Значение']])
    rows = []
    for row in calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_konf,
    ):
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(r)) for r in row]))
    all_table.append(rows)

    #
    # Расчет вероятностей реализации угроз целостности
    #

    print('\n\t\t\t Вероятность реализации угроз целостности')
    answer+='\n\t\t\t Вероятность реализации угроз целостности\n'
    print(tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity,
    ), tablefmt="grid"))
    answer+=tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity,
    ), tablefmt="grid")

    all_table.append(
        [ft.DataColumn(ft.Text(header)) for header in
         ['Номер', 'Вероятность реализации угроз целостности', 'Значение']])
    rows = []
    for row in calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity,
    ):
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(r)) for r in row]))
    all_table.append(rows)

    answer+='\n'
    #
    # Расчет вероятностей реализации угроз доступности
    #

    print('\n\t\t\t Вероятность реализации угроз доступности')
    answer+='\n\t\t\t Вероятность реализации угроз доступности\n'
    print(tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_availability,
    ), tablefmt="grid"))
    answer+=tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_availability,
    ), tablefmt="grid")

    answer += tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity,
    ), tablefmt="grid")

    all_table.append(
        [ft.DataColumn(ft.Text(header)) for header in
         ['Номер', 'Вероятность реализации угроз доступности', 'Значение']])
    rows = []
    for row in calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity,
    ):
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(r)) for r in row]))
    all_table.append(rows)

    answer+='\n'
    #
    # Расчет вероятностей реализации угроз целостности СОИ.
    #
    print('\n\t\t\t Вероятность реализации угроз целостности СОИ')
    answer+='\n\t\t\t Вероятность реализации угроз целостности СОИ\n'
    answer+=tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity_soi,
    ), tablefmt="grid")
    print(tabulate(calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity_soi,
    ), tablefmt="grid"))
    answer+='\n'

    all_table.append(
        [ft.DataColumn(ft.Text(header)) for header in
         ['Номер', 'Вероятность реализации угроз целостности СОИ', 'Значение']])
    rows = []
    for row in calculation_probabilities_threat_realization(
        mechanism_quality_indicators_values,
        limit_sufficiency_integrity_soi,
    ):
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(r)) for r in row]))
    all_table.append(rows)

    return all_table

