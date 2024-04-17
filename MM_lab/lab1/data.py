_strData ='''
1 66,8 -5,3 6,3 15,8
2 90,1 8,6 -6,7 25,4
3 -1,7 36,5 14,7 -25,4
4 17,9 23,5 -14,3 10,7
5 141,8 25,4 8,8 25,4
6 82,7 -10,5 42,2 -7,1
7 55,7 16,8 25,4 -25,4
'''
#6
_strData = '''
1 170,0 7,4 -23,2 -48,5
2 56,6 3,7 -11,7 -23,2
3 112,9 1,8 6,4 -12,7
4 -5,8 -4,1 11,7 12,7
5 8,7 -7,4 22,8 23,2
6 492,7 -14,0 28,1 -76,1
'''


_numData = _strData.replace('\n', ' ').replace(',', '.').split(' ')[1:-1]

# parameter quantity
m = 3
#
number_dimensions = 6

_shift = (m + 2)
data = [_numData[i * _shift + 1: i * _shift + _shift] for i in range(number_dimensions)]
print(data)
