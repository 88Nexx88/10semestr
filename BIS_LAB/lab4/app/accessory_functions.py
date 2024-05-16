from enums import TypeRigor


# Основная линейная функция
def _f(x, shift):
    return (1 / 3) * (x - shift)


# Обертка над основной функцией которая зеркалит ее (is_positive=False), и ограничивает [0:1].
def _f_direction(x, shift, is_positive: bool = True):
    res = _f(x, shift)
    if is_positive:
        return 0 if res <= 0 else 1 if res >= 1 else res
    res *= -1
    return 0 if res <= 0 else 1 if res >= 1 else res


# Функции принадлежности, по степени строгости:

# средняя
def medium_af(x):
    return _f_direction(x, 2) if x <= 5 else _f_direction(x, 8, is_positive=False)


# низкая
def low_af(x):
    return _f_direction(x, 4, is_positive=False)


# высокая
def high_af(x):
    return _f_direction(x, 6)


# ниже среднего
def below_medium_af(x):
    return _f_direction(x, 5, is_positive=False)


# выше среднего
def above_medium_af(x):
    return _f_direction(x, 5)


# очень низкая
def very_low_af(x):
    # return _f_direction(x, 2, is_positive=False)
    return low_af(x) ** 2


# очень высокая
def very_high_af(x):
    # return _f_direction(x, 8)
    return high_af(x) ** 2


# не выше среднего
def not_above_medium_af(x):
    # return _f_direction(x, 8, is_positive=False)
    return 1 - above_medium_af(x)


# не ниже среднего
def not_below_medium_af(x):
    # return _f_direction(x, 4)
    return 1 - below_medium_af(x)


def type_rigor_matching(t: TypeRigor, value: float) -> float:
    match t:
        case TypeRigor.HIGH:
            return high_af(value)
        case TypeRigor.LOW:
            return low_af(value)
        case TypeRigor.MEDIUM:
            return medium_af(value)
        case TypeRigor.VERY_HIGH:
            return very_high_af(value)
        case TypeRigor.VERY_LOW:
            return very_low_af(value)
        case TypeRigor.ABOVE_MEDIUM:
            return above_medium_af(value)
        case TypeRigor.BELOW_MEDIUM:
            return below_medium_af(value)
        case TypeRigor.NOT_ABOVE_MEDIUM:
            return not_above_medium_af(value)
        case TypeRigor.NOT_BELOW_MEDIUM:
            return not_below_medium_af(value)
        case _:
            return value
