import numpy as np
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.display.max_columns = 50
def addition_calculation(set_: np.ndarray) -> np.ndarray:
    return np.ones_like(set_) - set_


def intersection_calculation_multiplication_method(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    return set_1 * set_2


def intersection_calculation_min_method(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    new_array = []
    for row_index, row in enumerate(set_1):
        new_array.append([min(value, float(set_2[row_index, col_index])) for col_index, value in enumerate(row)])
    return np.array(new_array)


def union_calculation_bound_sum_method(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    new_array = []
    for row_index, row in enumerate(set_1):
        new_array.append(
            [value + float(set_2[row_index, col_index]) if value + float(set_2[row_index, col_index]) < 1 else 1 for
             col_index, value in enumerate(row)])
    return np.array(new_array)


def union_calculation_max_method(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    new_array = []
    for row_index, row in enumerate(set_1):
        new_array.append([max(value, float(set_2[row_index, col_index])) for col_index, value in enumerate(row)])
    return np.array(new_array)


def con_2_calculation(set_: np.ndarray) -> np.ndarray:
    return set_ * set_


def algebraic_sum_calculation(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    return (set_1 + set_2) - (set_1 * set_2)


def disjunctive_sum_calculation(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    # тут возможна замена методов объединения и пересечения
    # intersection_calculation_multiplication_method | intersection_calculation_min_method
    # union_calculation_bound_sum_method | union_calculation_max_method
    return union_calculation_max_method(
        intersection_calculation_min_method(set_1, addition_calculation(set_2)),
        intersection_calculation_min_method(set_2, addition_calculation(set_1))
    )


def print_with_stats(set_: np.ndarray):
    s = pd.DataFrame(set_, columns=(range(1, len(set_[0]) + 1)), index=(range(1, len(set_) + 1)))
    s['sum_row'] = set_.sum(1)
    columns = s.columns.tolist()
    sums = [s[column].sum() for column in columns]
    new_row = pd.Series({column: sums[i] for i, column in enumerate(columns)})
    s.loc['sum_col'] = new_row
    s['sum_row'].loc['sum_col'] = '-'
    print(s)
    print()
    # print('\nsum columns \t', set_.sum(0), '=> ', round(sum(set_.sum(0)), 4))
    # print('sum rows \t\t', set_.sum(1), '=> ', round(sum(set_.sum(1)), 4))
    print(f'Cумма всего:  {round(sum(set_.sum(1)), 4)}')
