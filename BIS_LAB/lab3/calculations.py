from typing import List
import functools

import numpy as np

from data import mechanism_names, threats_names
from data_converters import degrees_of_compliance_map, importance_coefficients_map


#
# Расчет показателя качества механизма xq.
# Принимает характеристики этого механизма:
#    ok - весовой коэффициент важности характеристики для всего механизма в целом
#    yk - степень соответствия характеристики требованиям ИБ, т.е. числовой показатель, лежащий в диапазоне [0, 1]
#
def _mechanism_quality_calculation(
        ok: List[float],
        yk: List[float],
) -> float:
    #     формула 3.34
    if len(ok) != len(yk):
        raise Exception('Ошибка в предоставляемых параметрах ::', 'Списки разной длины')
    return sum([ok[index] * yk[index] for index in range(len(ok))])


#
# Расчет вероятностей реализации угроз ИБ.
# Принимает списки:
#   xiq – показатель качества q-го механизма ИБ, т.е. его способность не допустить реализацию
#         i-й угрозы в тех обстоятельствах и в рамках тех ограничений, в которых функционирует данный механизм.
#   biq – предел достаточности q-го механизма для противодействия реализации i-й угрозы при условии,
#         что он является единственным противодействующим данной угрозе.
#
def _probabilities_threat_realization_calc(
        xiq: List[float],
        biq: List[float],
) -> float:
    #     формула 3.33
    if len(xiq) != len(biq):
        raise Exception('Ошибка в предоставляемых параметрах ::', 'Списки разной длины')
    return functools.reduce(lambda a, b: a * b, [1 - (xiq[index] * biq[index]) for index in range(len(biq))])


#
# Вычисляем показатели качества механизмов
#
def calculation_mechanism_quality_indicators():
    for key, value in degrees_of_compliance_map.items():
        _ok = []
        _yk = []
        for i in value.values():
            _yk.append(i.value)
            _ok.append(importance_coefficients_map[i.pp].value)
        yield [key, mechanism_names[i.mechanism_number], _mechanism_quality_calculation(_ok, _yk)]


def calculation_probabilities_threat_realization(mechanism_quality_ind, limit_suff: np.array):
    for j in range(len(limit_suff[0])):
        _xiq = mechanism_quality_ind
        _biq = limit_suff[:, j]
        yield [f'1.{j + 1}', threats_names[f'1.{j + 1}'], _probabilities_threat_realization_calc(_xiq, _biq)]
