from pprint import pprint

import numpy as np

from data import *
from typing import Dict
from models import ImportanceCoefficient, DegreeOfCompliance

#
# Парсинг коэффициентов важности характеристики
#
_importance_coefficients_temp = [i.strip() for i in
                                 importance_coefficients_str.replace('\n', '').replace(',', '.').split(';')][:-1]

#
# Парсинг степеней соответствия характеристики СЗИ требованиям ИБ
#
_degrees_of_compliance_temp = [i.strip() for i in vars_data_str.replace('\n', ' ').replace(',', '.').split(' ')][1:-1]


#
# Общий парсер пределов достаточности
#
def split_limits(arr: str, n):
    arr = arr.replace(',', '.').split()
    return np.array(np.array_split(arr, np.ceil(len(arr) / n))).astype(float)


#
# Парсинг пределов достаточности для угрозы конфиденциальности
#
limit_sufficiency_konf = split_limits(limit_sufficiency_konf_str, 7)

#
# Парсинг пределов достаточности для угрозы целостности
#
limit_sufficiency_integrity = split_limits(limit_sufficiency_integrity_str, 7)

#
# Парсинг пределов достаточности для угрозы доступности
#
limit_sufficiency_availability = split_limits(limit_sufficiency_availability_str, 7)

#
# Парсинг пределов достаточности для угрозы целостности СОИ
#
limit_sufficiency_integrity_soi = split_limits(limit_sufficiency_integrity_soi_str, 6)

#
# Преобразуем коэффициенты важности характеристики в объект (ImportanceCoefficient) и складываем в словарь
#
importance_coefficients_map: Dict[str, ImportanceCoefficient] = {}
for i in range(0, len(_importance_coefficients_temp), 3):
    # получаем номер характеристики и ее коэффициент важности
    pp, descr, coefficient = _importance_coefficients_temp[i:i + 3]
    # создаем объект и помещаем в словарь
    importance_coefficients_map[pp] = ImportanceCoefficient(pp, descr, coefficient)

#
# Преобразуем степени соответствия характеристики СЗИ требованиям ИБ в объект (DegreeOfCompliance) и
# складываем в словарь, и группируем по механизмам:
#  {
#       "Номер механизма 1":
#           {
#               "Номер характеристики 1.1" : object1(DegreeOfCompliance),
#               "Номер характеристики 1.2" : object2(DegreeOfCompliance)
#               .........................................................
#           }
#       ....................
#  }
#
degrees_of_compliance_map: Dict[str, Dict[str, DegreeOfCompliance]] = {}
for i in range(0, len(_degrees_of_compliance_temp), 2):
    # получаем номер характеристики и значение степени соответствия
    pp, value = _degrees_of_compliance_temp[i: i + 2]
    # извлекаем номер механизма
    mechanism_number = pp.split('.')[0]
    # находим уровень строгости дя данной характеристики
    type_rigor = alternative_characterization_descriptions[pp]
    # добавляем группу механизма если не добавлена ранее
    if mechanism_number not in degrees_of_compliance_map.keys():
        degrees_of_compliance_map[mechanism_number] = {}
    # Создаем объект и помещаем в словарь
    degrees_of_compliance_map[mechanism_number].update({pp: DegreeOfCompliance(pp, value, type_rigor)})
