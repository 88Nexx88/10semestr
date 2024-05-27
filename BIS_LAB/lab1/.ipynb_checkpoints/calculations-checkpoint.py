import numpy as np


def intersection_calculation(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    return set_1 * set_2


def union_calculation(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    return np.vectorize(lambda x: 0 if x < 1 else 1)(set_1 + set_2)


def reversal_calculation(set_: np.ndarray) -> np.ndarray:
    return np.transpose(set_)


def composition_calculation(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    res = set_1[:, :len(set_2[0])].tolist()
    for value in set_2[:len(set_1), :]:
        for ind, val in enumerate(res):
            res[ind] = union_calculation(value, val)
    return np.array(res)


def composition_calculation_2(set_1: np.ndarray, set_2: np.ndarray) -> np.ndarray:
    res = np.dot(set_1, set_2)
    return union_calculation(res, np.zeros_like(res))


def completing_calculation(set_: np.ndarray) -> np.ndarray:
    return np.ones_like(set_) - set_


def dual_relation_calculation(set_: np.ndarray) -> np.ndarray:
    return reversal_calculation(completing_calculation(set_))


def print_stat(set_: np.ndarray):
    # print('sum columns \t', set_.sum(0), '=> ', sum(set_.sum(0)))
    print('Сумма для анализа: ', set_.sum(0), ', общая сумма: ', sum(set_.sum(0)))
    # print('sum rows \t\t', set_.sum(1), '=> ', sum(set_.sum(1)))
