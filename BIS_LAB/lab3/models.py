from accessory_functions import type_rigor_matching
from enums import TypeRigor


# Степень соответствия требованиям
class DegreeOfCompliance:
    def __init__(self, pp, value: str, type_rigor: TypeRigor):
        # Номер характеристики N.M (1.1, 1.2 ...)
        self.pp: str = pp
        # Номер механизма N (1, 2, 3 ...)
        self.mechanism_number = pp.split('.')[0]
        # Тип строгости
        self.type_rigor = type_rigor
        # Степень соответствия требованиям, определяется с
        # помощью функции принадлежности в соответствии с уровнем строгости (type_rigor)
        self.value: float = type_rigor_matching(type_rigor, float(value))

    def __str__(self):
        return f'{self.pp} : {self.value}'


# Коэффициент важности
class ImportanceCoefficient:
    def __init__(self, pp, desc, value):
        # Номер характеристики N.M (1.1, 1.2 ...)
        self.pp: str = pp
        # Номер механизма N (1, 2, 3 ...)
        self.mechanism_number = int(pp.split('.')[0])
        # Описание характеристики
        self.desc: str = desc
        # Весовой коэффициент важности характеристики
        self.value: float = float(value)

    def __str__(self):
        return f'{self.pp} : {self.desc} : {self.value}'
