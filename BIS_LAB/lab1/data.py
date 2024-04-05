import numpy as np

set_1_str = '''
1	0	0	1	1	1	0	1
0	0	0	1	1	0	1	0
1	0	1	1	0	0	1	0
1	1	0	1	0	1	0	1
1	1	1	1	1	1	0	1
1	0	1	0	0	0	1	0
1	0	1	1	1	0	0	1
'''

# set_1_str = '''
# 1	1	1
# 1	0	0
# '''

set_2_str = '''
1	0	1	0	0	1	1	1
1	0	0	0	0	0	0	1
1	0	0	1	1	1	1	1
1	1	1	1	0	0	1	1
1	1	1	0	0	0	1	1
0	1	1	0	1	0	1	0
0	1	1	0	1	0	0	1
'''
# set_2_str = '''
# 1	0	1
# 1	1	0
# '''


def str_to_array(str_: str) -> np.ndarray:
    return np.array([list(map(int, i.split('\t'))) for i in str_.replace(',', '.').split('\n')[1:-1]])


set_1 = str_to_array(set_1_str)
set_2 = str_to_array(set_2_str)