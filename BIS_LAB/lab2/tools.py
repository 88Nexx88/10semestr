import pandas as pd
import numpy as np

def parse():
    data1 = '''
0,53	0,95	0,62	0,53	0,57	0,15	0,95	0,34	0,43
0,56	0,91	0,48	0,48	0,73	0,96	0,21	0,88	0,14
0,35	0,81	0,97	0,62	0,89	0,16	0,77	0,79	0,28
0,39	0,50	0,63	0,38	0,53	0,87	0,70	0,42	0,10
0,49	0,22	0,97	0,67	0,13	0,17	0,97	0,40	0,59
0,34	0,73	0,21	0,50	0,23	0,44	0,93	0,70	0,60
0,11	0,96	0,12	0,86	0,55	0,42	0,49	0,75	0,65
'''

    data1 = data1.replace(',', '.')
    lines = data1.split('\n')
    numbers = []
    for line in lines:
        if line != '':
            numbers.extend(line.split('\t'))
    numbers = [float(n) for n in numbers]

    matrix1 = np.array(numbers).reshape(7, 9)



    data2 = '''
0,33	0,30	0,93	0,73	0,91	0,71	0,58	0,16	0,47
0,46	0,96	0,14	0,11	0,29	0,86	0,31	0,90	0,64
0,55	0,51	0,25	0,54	0,93	0,81	0,53	0,69	0,45
0,85	0,78	0,13	0,36	0,62	0,47	0,95	0,71	0,58
0,46	0,95	0,90	0,73	0,30	0,76	0,41	0,24	0,20
0,11	0,34	0,28	0,89	0,93	0,84	0,34	0,52	0,43
0,49	0,11	0,16	0,78	0,41	0,89	0,76	0,90	0,18
'''

    data2 = data2.replace(',', '.')
    lines = data2.split('\n')
    numbers = []
    for line in lines:
        if line != '':
            numbers.extend(line.split('\t'))
    numbers = [float(n) for n in numbers]

    matrix2 = np.array(numbers).reshape(7, 9)

    print('Data 1')
    print(matrix1)

    print()

    print('Data 2')
    print(matrix2)

    return matrix1, matrix2

parse()