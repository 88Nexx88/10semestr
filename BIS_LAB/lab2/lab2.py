from calculations import *
from data import set_1, set_2

print('Исходные данные.')
print('\nНечёткое отношение для первого режима работы ИС')
print_with_stats(set_1)
print('\nНечёткое отношение для второго режима работы ИС')
print_with_stats(set_2)
print()

# 1.1.	Дополнения обоих отношений.
# Показывает степень безразличия угрозы относительно уязвимости,
# т.е. то какая существует возможность возникновения угрозы при
# отсутствии данной уязвимости в первом и втором режимах функционирования ИС.
print('''1.1.	Дополнения обоих отношений.
Показывает степень безразличия угрозы относительно уязвимости, т.е. то какая существует возможность возникновения угрозы при отсутствии данной уязвимости в первом и втором режимах функционирования ИС.
''')
print('Дополнение для первого режима работы ИС')
print_with_stats(addition_calculation(set_1))
print()
print('Дополнение для второго режима работы ИС')
print_with_stats(addition_calculation(set_2))
print()

# 1.2.	Пересечение отношений по двум методам: метод произведений и метод минимума.
# Показывает абсолютную, не зависящую от условий эксплуатации, критичность
# уязвимостей для возникновения угроз.
print('''1.2.	Пересечение отношений.
Показывает абсолютную, не зависящую от условий эксплуатации, критичность уязвимостей для возникновения угроз
''')
print('Метод произведений:')
print_with_stats(intersection_calculation_multiplication_method(set_1, set_2))
print()
print('Метод минимума:')
print_with_stats(intersection_calculation_min_method(set_1, set_2))
print()
print('Метод минимума наиболее чувствителен\n')
# 1.3.	Объединение отношений по двум методам: метод граничной суммы и метод максимума.
# Показывает то, с какой вероятностью при наличии уязвимости
# данная угроза возникнет в ИС при том, что режим функционирования
# ИС изменится с первого на второй или со второго на первый.
print('''1.3.	Объединение отношений.
Показывает то, с какой вероятностью при наличии уязвимости данная угроза возникнет в ИС при том, что режим функционирования ИС изменится с первого на второй или со второго на первый.
''')
print('Метод граничной суммы.')
print_with_stats(union_calculation_bound_sum_method(set_1, set_2))
print()
print('Метод максимума.')
print_with_stats(union_calculation_max_method(set_1, set_2))
print()
print('Метод граничной наиболее чувствителен\n')

# 1.4.	Концентрацию степени 2 для первого отношения.
# Показывает критичность повторного возникновения угрозы в первом режиме функционирования ИС.
print('''1.4.	Концентрация степени 2 для первого отношения.
Показывает критичность повторного возникновения угрозы в первом режиме функционирования ИС.
''')
print_with_stats(con_2_calculation(set_1))
print()


# 1.5.	Алгебраическую сумму отношений.
# Показывает критичность уязвимости при отсутствии осведомленности злоумышленника
# о режимах функционирования ИС.
print('''1.5.	Алгебраическая сумма отношений.
Показывает критичность уязвимости при отсутствии осведомленности злоумышленника о режимах функционирования ИС.
''')
print_with_stats(algebraic_sum_calculation(set_1, set_2))
print()

# 1.6.	Дизъюнктивную сумму отношений.
# Показывает критичность уязвимости для возникновения угрозы в том случае,
# если режим функционирования ИС не изменяется в анализируемый период времени.
print('''1.6.	Дизъюнктивная сумма отношений.
Показывает критичность уязвимости для возникновения угрозы в том случае, если режим функционирования ИС не изменяется в анализируемый период времени.
''')
print_with_stats(disjunctive_sum_calculation(set_1, set_2))
print()
print('Отсутствие осведомленности злоумышленника о режиме функционировании ИС,\nзначительно критичнее, нежели если режим функц. ИС не изменяется в анализируемый период времени\n')


