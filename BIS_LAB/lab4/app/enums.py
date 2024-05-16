from enum import Enum


# Уровни строгости
class TypeRigor(Enum):
    HIGH = 1  # Высокий
    LOW = 2  # Низкий
    MEDIUM = 3  # Средний
    VERY_HIGH = 4  # Очень высокий
    # значение высокого в квадрат
    VERY_LOW = 5  # Очень низкий
    ABOVE_MEDIUM = 6  # Выше среднего
    BELOW_MEDIUM = 7  # Ниже среднего
    # 1-выше среднего
    NOT_ABOVE_MEDIUM = 8  # НЕ выше среднего
    NOT_BELOW_MEDIUM = 9  # НЕ ниже среднего
    TYPE_1 = 10  # Количественная, тип 1
    TYPE_2 = 11  # Количественная, тип 2
    TYPE_3 = 12  # Количественная, тип 3
