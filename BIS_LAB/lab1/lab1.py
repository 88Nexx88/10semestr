from tools import parse

import pandas as pd
import numpy as np


data1, data2 = parse()
data1 = data1.astype('int64')
data2 = data2.astype('int64')
data1_ = data1.values
print(data1_)
data2_ = data2.values
print(data2_)
print('1. Для обоих отношений вычислить:')
print('1.1.	Пересечение отношений. Определяет, какие причинно-следственные связи между уязвимостями и угрозами являются устойчивыми и не зависят от режима функционирования. ')
peres = []
for s in range(len(data1_)):
    row = []
    for i in range(len(data1_[s])):
        row.append(data1_[s][i] * data2_[s][i])
    peres.append(row)
print(peres)

