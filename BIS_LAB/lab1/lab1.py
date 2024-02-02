from tools import parse

import pandas as pd
import numpy as np


data1, data2 = parse()
data1 = data1.astype('int64')
data2 = data2.astype('int64')
data1_ = data1.values
data2_ = data2.values
print()
print('1. Для обоих отношений вычислить:')
print('1.1.	Пересечение отношений. Определяет, какие причинно-следственные связи между уязвимостями и угрозами являются устойчивыми и не зависят от режима функционирования. ')
peres_ = []
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(data1_[s][i] * data2_[s][i])
    peres_.append(row)
peres = pd.DataFrame(peres_, columns=(range(1, len(peres_[0])+1)), index=(range(1, len(peres_)+1)))
print(peres)

print()
obedin_ = []
print('1.2.	Объединение отношений. Определяет общий спектр причинно-следственных связей между уязвимостями и угрозами во всех режимах функционирования ИС. ')
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(max(data1_[s][i], data2_[s][i]))
    obedin_.append(row)
obedin = pd.DataFrame(obedin_, columns=(range(1, len(obedin_[0])+1)), index=(range(1, len(obedin_)+1)))
print(obedin)

print()
print('1.3.	Обращения обоих отношений. Позволяет выявить спектр уязвимостей, которые могут присутствовать в ИС, но не выявлены обследованием, если произошёл инцидент – была реализована угроза. ')
obrash_ = np.matrix.transpose(data1_)
obrash_1 = pd.DataFrame(obrash_, columns=(range(1, len(obrash_[0])+1)), index=(range(1, len(obrash_)+1)))
print('data1')
print(obrash_1)

obrash_ = np.matrix.transpose(data2_)
print('data2')
obrash_2 = pd.DataFrame(obrash_, columns=(range(1, len(obrash_[0])+1)), index=(range(1, len(obrash_)+1)))
print(obrash_2)
print()
print('1.4.	Композицию отношений.')

for i in range(len(data1_)):
    row = []
    for j in range(len(data1_[s])):
        row.append(data1_[s][i] * data2_[s][i])
    peres_.append(row)