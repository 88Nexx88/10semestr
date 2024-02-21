_strData ='''
1 66,8 -5,3 6,3 15,8
2 90,1 8,6 -6,7 25,4
3 -1,7 36,5 14,7 -25,4
4 17,9 23,5 -14,3 10,7
5 141,8 25,4 8,8 25,4
6 82,7 -10,5 42,2 -7,1
7 55,7 16,8 25,4 -25,4
'''

_numData = _strData.replace('\n', ' ').replace(',', '.').split(' ')[1:-1]

# parameter quantity
m = 3
#
number_dimensions = 7

_shift = (m + 2)
data = [_numData[i * _shift + 1: i * _shift + _shift] for i in range(number_dimensions)]

# print(data)
