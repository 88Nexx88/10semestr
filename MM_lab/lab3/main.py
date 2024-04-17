import math

data1 = '3 8 98 83 99 79 80 81 84 81'
data2 = '3 8 10 10 10 18 11 18 09 14'
data3 = '3 8 23 22 27 36 24 25 21 40'

data1 = '6 9 87 90 77 83 87 82 81 97 97'
data2 ='6 9 10 15 14 09 07 8 10 15 12'
data3 ='6 9 22 27 33 31 23 28 31 36 30'

R = 4

per_ocenki_par = [int(i)/100 for i in data1.split(' ')[2:]]
x = per_ocenki_par
per_koef_avtor_exs = [int(i)/100 for i in data2.split(' ')[2:]]
v = per_koef_avtor_exs
koef_rassogl_ocen_exs = [int(i)/100 for i in data3.split(' ')[2:]]
k = koef_rassogl_ocen_exs
print(f'Вариант: {data1.split(" ")[0]}\nКол-во экспертов: {data1.split(" ")[1]}')
print(f'''Первичные оценки параметров, данных экспертной группой {per_ocenki_par}
''')
print(f'''Первичные коэффициенты авторитета экспертов {per_koef_avtor_exs}
''')
print(f'''Коэффициенты рассогласования оценок экспертов {koef_rassogl_ocen_exs}
''')

utochn = [round(1/2*(v[i]+(v[i]/k[i]**(1/2))), R) for i, val in enumerate(v)]

print(f'''
–	уточнения коэффициентов авторитета экспертов
{utochn}''')

skorek = [round(utochn[i]/sum(utochn), R) for i, val in enumerate(utochn)]
print(f'''
–   скорректированные коэффициенты авторитета
{skorek}''')


p_A1 = round(sum(per_ocenki_par) / len(per_ocenki_par), R)
print(f'''
–	значение оцениваемого экспертами параметра как среднее арифметическое оценок экспертов
{p_A1}''')

current_v = v.copy()
sum_ = 0
for i in range(len(per_ocenki_par)-1):
    for j in range(i+1, len(per_ocenki_par)):
        if current_v[i] - current_v[j] != 0:
            h_ij = ((max(current_v) - current_v[i]) /
                    (current_v[i] - current_v[j]))*(per_ocenki_par[i] - per_ocenki_par[j]) +per_ocenki_par[i]
        else:
            h_ij = (per_ocenki_par[i] + per_ocenki_par[j]) / 2
        if h_ij < 1 and h_ij > 0:
            sum_+=h_ij
        else:
            sum_+=1 if h_ij>=1 else 0
p_A2 = round(2 * math.factorial((len(v) - 2)) / math.factorial(len(v)) * sum_, R)
print(f'''
–	агрегированное значение оцениваемого экспертами параметра без коррекции коэффициентов авторитета экспертов
{p_A2}''')


current_v = skorek.copy()
sum_ = 0
for i in range(len(per_ocenki_par)-1):
    for j in range(i+1, len(per_ocenki_par)):
        h_ij = ((max(current_v) - current_v[i]) /
                (current_v[i] - current_v[j]))*(per_ocenki_par[i] - per_ocenki_par[j]) +per_ocenki_par[i]
        if h_ij < 1 and h_ij > 0:
            sum_+=h_ij
        else:
            sum_+= 1 if h_ij>=1 else 0
p_A3 = round(2 * math.factorial((len(v) - 2)) / math.factorial(len(v)) * sum_, R)
print(f'''
–	агрегированное значение оцениваемого экспертами параметра с коррекцией коэффициентов авторитета экспертов.
{p_A3}''')


print('Анализ: ')
print(per_ocenki_par)
print(p_A1)

print()
print(per_ocenki_par)
print(v)
print(p_A2)


print()
print(per_ocenki_par)
print(skorek)
print(p_A3)




























input('\n\n\n\n\n\n\n\n\nP.S. (нажми для доп инфы)')
print('''\033[30;47m\P.S.
Суть показать почему изменились оценки например у меня:

0.85

0.74

0.69

Сравниваем по парно в каждой группе типо:
Для оценки p_A2 – агрегированное значение оцениваемого экспертами параметра без коррекции коэффициентов авторитета экспертов
[0.98, 0.83, 0.99, 0.79, 0.8, 0.81, 0.84, 0.81]
[0.1, 0.1, 0.1, 0.18, 0.11, 0.18, 0.09, 0.14]

0.98 - 0.83 меньше а значение не изменилось
0.1 - 0.1

0.98 - 0.99 больше а значение не изменилось
0.1 - 0.1

0.98 - 0.79 меньше а значение изменилось сильно, отсюда будет уменьшее значения оценки p_A2
0.1 - 0.18
итд
в моём случае у всех в принципе значение меняется в меньшую сторону отсюда и будет уменьшение агрегированной оценки
и нет никаких пар значений у который сильно меняется значение, из-за чего был бы рост:
Это у  меня:
0.98 - 0.84 1
0.1 - 0.09 2

сильное уменьшение 1 / очень низкое уменьшение 2

А если б было:
Например:
0.98 - 0.84
0.19 - 0.09

уменьшение / уменьшение
и таких пар было много то скорее значение агрегированное увеличилось
''')


print('Например на варианте 4 где наоборот учеличилось: ')
data2 = '4 7 13 19 16 14 14 16 08'
data3 = '4 7 31 30 24 23 22 35 30'
data1 = '4 7 80 92 93 93 91 97 79'


per_ocenki_par = [int(i)/100 for i in data1.split(' ')[2:]]
x = per_ocenki_par
per_koef_avtor_exs = [int(i)/100 for i in data2.split(' ')[2:]]
v = per_koef_avtor_exs
koef_rassogl_ocen_exs = [int(i)/100 for i in data3.split(' ')[2:]]
k = koef_rassogl_ocen_exs
print(f'Вариант: {data1.split(" ")[0]}\nКол-во экспертов: {data1.split(" ")[1]}')
print(f'''Первичные оценки параметров, данных экспертной группой {per_ocenki_par}
''')
print(f'''Первичные коэффициенты авторитета экспертов {per_koef_avtor_exs}
''')
print(f'''Коэффициенты рассогласования оценок экспертов {koef_rassogl_ocen_exs}
''')

utochn = [round(1/2*(v[i]+(v[i]/k[i]**(1/2))), R) for i, val in enumerate(v)]

print(f'''
–	уточнения коэффициентов авторитета экспертов
{utochn}''')

skorek = [round(utochn[i]/sum(utochn), R) for i, val in enumerate(utochn)]
print(f'''
–   скорректированные коэффициенты авторитета
{skorek}''')


p_A1 = round(sum(per_ocenki_par) / len(per_ocenki_par), R)
print(f'''
–	значение оцениваемого экспертами параметра как среднее арифметическое оценок экспертов
{p_A1}''')

current_v = v.copy()
sum_ = 0
for i in range(len(per_ocenki_par)-1):
    for j in range(i+1, len(per_ocenki_par)):
        if current_v[i] - current_v[j] != 0:
            h_ij = ((max(current_v) - current_v[i]) /
                    (current_v[i] - current_v[j]))*(per_ocenki_par[i] - per_ocenki_par[j]) +per_ocenki_par[i]
        else:
            h_ij = (per_ocenki_par[i] + per_ocenki_par[j]) / 2
        if h_ij < 1 and h_ij > 0:
            sum_+=h_ij
        else:
            sum_+=1 if h_ij>=1 else 0
p_A2 = round(2 * math.factorial((len(v) - 2)) / math.factorial(len(v)) * sum_, R)
print(f'''
–	агрегированное значение оцениваемого экспертами параметра без коррекции коэффициентов авторитета экспертов
{p_A2}''')


current_v = skorek.copy()
sum_ = 0
for i in range(len(per_ocenki_par)-1):
    for j in range(i+1, len(per_ocenki_par)):
        h_ij = ((max(current_v) - current_v[i]) /
                (current_v[i] - current_v[j]))*(per_ocenki_par[i] - per_ocenki_par[j]) +per_ocenki_par[i]
        if h_ij < 1 and h_ij > 0:
            sum_+=h_ij
        else:
            sum_+= 1 if h_ij>=1 else 0
p_A3 = round(2 * math.factorial((len(v) - 2)) / math.factorial(len(v)) * sum_, R)
print(f'''
–	агрегированное значение оцениваемого экспертами параметра с коррекцией коэффициентов авторитета экспертов.
{p_A3}''')


print('Анализ: ')
print(per_ocenki_par)
print(p_A1)

print()
print(per_ocenki_par)
print(v)
print(p_A2)


print()
print(per_ocenki_par)
print(skorek)
print(p_A3)