import warnings

import pandas as pd
from itertools import combinations

from calc_similar import CalcSimilar

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.display.max_columns = 50

#Входные данные 3 var
data = '''
98	68	99	71	98	82	43	84	36	98	82	82	62	97	55 98	53	25	75	84	29	59	48	44	38	52	
58	14	69	84	95	19	11	86	77	69	18	84	27	63	28 20	24	31	46	96	72	71	57	79	57	18
80	42	97	17	33	18	40	77	48	62	72	63	27	36	64 25	28	53	82	17	52	65	10	31	86	69
84	76	34	58	17	79	51	34	33	15	94	92	78	84	21 68   35	94	75	20	83	55	90	70	34	89
'''

# data = ''' 6 var
# 98	74	95	24	18	30	78	95	58	74	97	12	52	92	96 98	18	41	46	86	43	31	24	93	49	84	53
# 59	34	10	24	55	27	66	29	57	54	10	13	72	22	42 25	74	88	67	17	18	99	73	42	30	71	17
# 30	86	12	42	55	33	44	54	72	72	80	69	88	75	45 99	13	73	90	84	33	37	47	88	29	85	54
# 37	81	93	12	31	97	49	33	53	36	62	61	76	91	33 34	99	94	69	79	39	86	70	43	47	48	66
# '''
methods_similar = 'евклидово,манхэттенское' #степенное,взвешенное евклидово  | чебышево и несогласия нет в вариантах вроде :)
# methods_similar = 'степенное,взвешенное евклидово'
methods_union = 'одиночной связи,полных связей,Уорда' #центроидный,средних связей
# methods_union = 'одиночной связи,полных связей,центроидный'
max_cl = 5 #максимальный размер кластера

#Если есть доп переменные занесите их в calc_dist






data = data.replace('\t', ' ').split('\n')[1:-1]
matrix = []
for data_row in data:
    row = []
    for i in data_row.split(' '):
        if i != '':
          row.append(int(i))
    matrix.append(row)

df = pd.DataFrame(matrix, columns=(range(0, len(matrix[0]))), index=(range(1, len(matrix)+1))).T

print(df, '\n')
print(f'Макс: {max_cl}')
print(f'Методы рассчёта: {methods_similar.split(",")}\nМетоды класстеризации: {methods_union.split(",")}')


an = ['–	вариации только меры сходства между объектами (три числа для каждого из трёх методов объединения)',
      '–	вариации только метода объединения (два числа для каждой из двух мер сходства между объектами)',
      '–	вариации и мер сходства, и методов объединения (одно чис-ло стабильно устойчивых пар объектов)'
      ]

f_an = [] #[] [] [] три группы в которых ищем 3 числа
s_an = [[], []] #[] [] 2 группы в которых ищем 2 числа
th_an = [] #[] 1 группа в которых ищем 1 числа


for method_un in methods_union.split(","):
    an_1 = []
    i = 0
    for method_sim in methods_similar.split(","):
        labels = range(len(df.index.values))
        answer = CalcSimilar(df.values.tolist(), max_cl, method_sim)
        clusters_matrix = answer.calculate(method_un)
        # для дальнейшего анализа
        an_1.append(clusters_matrix) #добавляем группу каждого вычисления
        s_an[i].append(clusters_matrix) #добавляем группу каждого объединения или в 1 или во 2
        i+=1
        th_an.append(clusters_matrix) #добавляем все

        print(f'Метод {method_un} | {method_sim}')
        print(clusters_matrix)
        print('_______________________')
    f_an.append(an_1)
analyze = [f_an, s_an, th_an]

comb = set(combinations(range(len(df.index)), 2))
result = { x:0 for x in comb}

print(an[0])
for group in range(len(f_an)):
    result = { x:0 for x in comb}
    sum_ = 0
    for pod in f_an[group]:
        for pod1 in pod:
            for i in range(len(pod1)-1):
                for j in range(i+1, len(pod1)):
                    result[(pod1[i], pod1[j])] += 1

    for key, val in result.items():
        if val > 1:
            # print(f'Пара {key} встретились в {val} видах')
            if val == len(f_an[group]):
                sum_+=1
    print(f'Число стабильно устойчивых пар объектов {sum_}')

print(an[1])
for group in range(len(s_an)):
    result = {x: 0 for x in comb}
    sum_ = 0
    for pod in s_an[group]:
        for pod1 in pod:
            for i in range(len(pod1) - 1):
                for j in range(i + 1, len(pod1)):
                    result[(pod1[i], pod1[j])] += 1

    for key, val in result.items():
        if val > 1:
            # print(f'Пара {key} встретились в {val} видах')
            if val == len(s_an[group]):
                sum_ += 1
    print(f'Число стабильно устойчивых пар объектов {sum_}')

print(an[2])
result = { x:0 for x in comb}
for pod in th_an: #[[2, 7, 8, 9, 21], [4, 10, 17, 19, 25], [1, 5, 12, 15], [3, 20, 22, 23], [0, 11, 13, 18], [6, 14, 16, 24]]
    for pod1 in pod:
        for i in range(len(pod1)-1):
            for j in range(i+1, len(pod1)):
                result[(pod1[i], pod1[j])] += 1
sum_ = 0
for key, val in result.items():
    if val > 1:
        # print(f'Пара {key} встретились в {val} видах')
        if val == len(th_an):
            sum_+=1
print(f'Число стабильно устойчивых пар объектов {sum_}')





# labels = df.index.values.tolist()
# answer = CalcSimilar(df.values.tolist(), max_cl, methods_similar.split(",")[0])
# clusters_matrix = answer.near_neighbor()
# print(clusters_matrix)
# print('_______________________')
# clusters_matrix = answer.dist_neighbor()
# print(clusters_matrix)
#
# print('____________________________________________')
#
# answer = CalcSimilar(df.values.tolist(), max_cl, methods_similar.split(",")[1])
# clusters_matrix = answer.near_neighbor()
# print(clusters_matrix)
# print('_______________________')
# clusters_matrix = answer.dist_neighbor()
# print(clusters_matrix)

