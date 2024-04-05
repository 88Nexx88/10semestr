import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.options.display.max_columns = 50

data = '''
98	68	99	71	98	82	43	84	36	98	82	82	62	97	55 98	53	25	75	84	29	59	48	44	38	52	
58	14	69	84	95	19	11	86	77	69	18	84	27	63	28 20	24	31	46	96	72	71	57	79	57	18
80	42	97	17	33	18	40	77	48	62	72	63	27	36	64 25	28	53	82	17	52	65	10	31	86	69
84	76	34	58	17	79	51	34	33	15	94	92	78	84	21 68   35	94	75	20	83	55	90	70	34	89
'''
methods_similar = 'евклидово,манхэттенское'
methods_union = 'одиночной связи,полных связей,Уорда'
max_cl = 5

data = data.replace('\t', ' ').split('\n')[1:-1]
matrix = []
for data_row in data:
    row = []
    for i in data_row.split(' '):
        if i != '':
          row.append(int(i))
    matrix.append(row)


df = pd.DataFrame(matrix, columns=(range(1, len(matrix[0])+1)), index=(range(1, len(matrix)+1)))

print(df, '\n')
print(f'Методы рассчёта: {methods_similar.split(",")}\nМетоды класстеризации: {methods_union.split(",")}')