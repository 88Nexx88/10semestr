from tools import parse

import pandas as pd
import numpy as np


data1, data2 = parse()
data1 = data1.astype('int64')
data2 = data2.astype('int64')
data1_ = data1.values
data2_ = data2.values
print()
print('''
1. Для обоих отношений вычислить:
''')
print('''
1.1.	Пересечение отношений. Определяет, какие причинно-следственные связи между уязвимостями и угрозами являются устойчивыми и не зависят от режима функционирования.
''')
peres_ = []
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(data1_[s][i] * data2_[s][i])
    peres_.append(row)
peres = pd.DataFrame(peres_, columns=(range(1, len(peres_[0])+1)), index=(range(1, len(peres_)+1)))
peres['comp'] = peres.sum(axis=1)
print(peres)

print()
obedin_ = []
print('''
1.2.	Объединение отношений. Определяет общий спектр причинно-следственных связей между уязвимостями и угрозами во всех режимах функционирования ИС.
''')
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(max(data1_[s][i], data2_[s][i]))
    obedin_.append(row)
obedin = pd.DataFrame(obedin_, columns=(range(1, len(obedin_[0])+1)), index=(range(1, len(obedin_)+1)))

obedin['comp'] = obedin.sum(axis=1)
print(obedin)
print()
print('''
1.3.	Обращения обоих отношений. Позволяет выявить спектр уязвимостей, которые могут присутствовать в ИС,
но не выявлены обследованием, если произошёл инцидент – была реализована угроза.
''')
obrash_ = np.matrix.transpose(data1_)
obrash_1 = pd.DataFrame(obrash_, columns=(range(1, len(obrash_[0])+1)), index=(range(1, len(obrash_)+1)))
print('data1')
obrash_1['comp'] = obrash_1.sum(axis=1)
print(obrash_1)


obrash_ = np.matrix.transpose(data2_)
print('data2')
obrash_2 = pd.DataFrame(obrash_, columns=(range(1, len(obrash_[0])+1)), index=(range(1, len(obrash_)+1)))
obrash_2['comp'] = obrash_2.sum(axis=1)
print(obrash_2)

print('''
1.4.	Композицию отношений.
В рамках поставленной задачи анализа уязвимостей ИС и угроз ИБ композиция имеет следующее практическое применение и вариации формул:
–	«Уязвимость – угроза – уязвимость». Позволяет выявить те пары уязвимостей, которые могут быть использованы злоумышленником совместно.
–	«Угроза – уязвимость ¬– угроза». Позволяет выявить те пары угроз, которые могут возникать совместно.
''')
kompoz_1 = []
for i in range(len(data1_)):
    row = []
    for j in range(len(data1_)):
        row.append(data1_[i][j] * obrash_2.values[i][j])
    kompoz_1.append(row)


kompoz_1_ = pd.DataFrame(kompoz_1, columns=(range(1, len(kompoz_1[0])+1)), index=(range(1, len(kompoz_1)+1)))
kompoz_1_['comp'] = kompoz_1_.sum(axis=1)
print(kompoz_1_)
print()

kompoz_2 = []
for i in range(len(data2_)):
    row = []
    for j in range(len(data2_)):
        row.append(data2_[i][j] * obrash_1.values[i][j])
    kompoz_2.append(row)
kompoz_2_ = pd.DataFrame(kompoz_2, columns=(range(1, len(kompoz_2[0])+1)), index=(range(1, len(kompoz_2)+1)))
kompoz_2_['comp'] = kompoz_2_.sum(axis=1)
print(kompoz_2_)
# все 0 нет связей

print('''
2. Для первого отношения вычислить:''')

print('''2.1.	Дополнение.
Показывает несвязанные пары «уязвимость» – «угроза» в данном режиме функционирования.
''')
dopol_ = []
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(1 - data1_[s][i])
    dopol_.append(row)
dopol = pd.DataFrame(dopol_, columns=(range(1, len(dopol_[0])+1)), index=(range(1, len(dopol_)+1)))
dopol['comp'] = dopol.sum(axis=1)
print(dopol)

print('''
2.2. Двойственное отношение.
Показывает спектр эксплуатируемых угрозой уязвимостей в данном режиме функционирования. 
''')
dvoy_ = []
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(1 - data1_[s][i])
    dvoy_.append(row)
dvoy_ = np.matrix.transpose(np.array(dvoy_))

dvoy = pd.DataFrame(dvoy_, columns=(range(1, len(dvoy_[0])+1)), index=(range(1, len(dvoy_)+1)))
dvoy['comp'] = dvoy.sum(axis=1)
print(dvoy)