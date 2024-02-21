from statistics import median, mean

import numpy as np
from data import m, data, number_dimensions
from tabulate import tabulate
from itertools import combinations

dimensions = np.array(data)


def system_solver(list_equations):
    left_side = np.array([i[1:] for i in list_equations]).astype(float)
    right_side = np.array([i[:1] for i in list_equations]).astype(float)
    X, residuals, _, _ = np.linalg.lstsq(left_side, right_side, rcond=None)
    return X



headers_table = ['№ ИЗМЕРЕНИЕ', *[f'ПАР.{(i + 1)}' for i in range(m)], 'РЕЗУЛЬТАТ ИЗМЕРЕНИЯ']
main_table = tabulate([[i + 1, *data[i][1:], *data[i][:1]] for i in range(len(data))], headers_table,
                      tablefmt="simple")
wrap_table = tabulate([[main_table]], ['ИСХОДНЫЕ ДАННЫЕ'], tablefmt='simple')
print(wrap_table)
itog = system_solver(data)
print('Рассчёт: ')
for x, i in enumerate(itog):
    print(f"ПАР.{x + 1} -> {i}")
print()

_temp_list = [i + 1 for i in range(number_dimensions)]
_all_combinations = []
for r in range(m + 1, number_dimensions):
    _all_combinations.extend(combinations(_temp_list, r))



def combination_calculations():
    result = []
    for n, i in enumerate(_all_combinations):
        x = system_solver([data[dim - 1] for dim in i])
        result.append([n + 1, i, x])
    return result


combination_result = combination_calculations()


headers_comb_table = ['№ КОМБИНАЦИЯ', '№ ИЗМЕРЕНИЕ', *[f'ПАР.{(i + 1)}' for i in range(m)]]
comb_rows = [[comb[0], comb[1], *[i for i in comb[2]]] for comb in combination_result]
main_comb_table = tabulate(comb_rows, headers_comb_table,
                           tablefmt="simple")
wrap_comb_table = tabulate([[main_comb_table]], ['КОМБИНАЦИИ ИЗМЕРЕНИЙ'], tablefmt="simple")

print(wrap_comb_table)
pi = []
for i in range(m):
    pi.append([j[2][i][0] for j in combination_result])

for x, i in enumerate(pi):
    # print(tabulate([[f"ПАРАМЕТР.{x + 1}"], [f'Значение {itog[x]}'], [f'Минимум => {min(i)}'], [f'Максимум => {max(i)}'], [f'Среднее=> {mean(i)}'], [f'Медиана=> {median(i)}']], tablefmt="simple"))
    print(tabulate([[f"ПАРАМЕТР.{x + 1}"], [f'Значение {itog[x]}'],
                    [f'Среднее=> {mean(i)}'], [f'Медиана=> {median(i)}']], tablefmt="simple"))
    # print(f"ПАР.{x + 1} мин => {min(i)} макс => {max(i)} ср=> {mean(i)} медиана=> {median(i)}")
