import pandas as pd


def parse():
    data1 = '''
    1	0	0	1	1	1	0	1
    0	0	0	1	1	0	1	0
    1	0	1	1	0	0	1	0
    1	1	0	1	0	1	0	1
    1	1	1	1	1	1	0	1
    1	0	1	0	0	0	1	0
    1	0	1	1	1	0	0	1
    '''

    data1_list = list(data1.strip())
    data1_matrix = []
    data_row = []
    for i in range(len(data1_list)):
        if data1_list[i] == '\n':
            data1_matrix.append(data_row)
            data_row = []
        elif data1_list[i] != '\t' and data1_list[i] != ' ':
            data_row.append(data1_list[i])
    data1_matrix.append(data_row)


    data2 = '''
    1	0	1	0	0	1	1	1
    1	0	0	0	0	0	0	1
    1	0	0	1	1	1	1	1
    1	1	1	1	0	0	1	1
    1	1	1	0	0	0	1	1
    0	1	1	0	1	0	1	0
    0	1	1	0	1	0	0	1
    '''

    data2_list = list(data2.strip())
    data2_matrix = []
    data_row = []
    for i in range(len(data2_list)):
        if data2_list[i] == '\n':
            data2_matrix.append(data_row)
            data_row = []
        elif data2_list[i] != '\t' and data2_list[i] != ' ':
            data_row.append(data2_list[i])
    data2_matrix.append(data_row)
    data1_ = pd.DataFrame(data1_matrix, columns=(range(1, len(data1_matrix[0])+1)), index=(range(1, len(data1_matrix)+1)))

    data2_ = pd.DataFrame(data2_matrix, columns=(range(1, len(data2_matrix[0])+1)), index=(range(1, len(data2_matrix)+1)))
    print('Data 1')
    print(data1_)

    print()

    print('Data 2')
    print(data2_)

    return data1_, data2_