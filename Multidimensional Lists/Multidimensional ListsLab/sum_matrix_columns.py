import sys
from io import StringIO
test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0

'''
test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''
sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)

rows, columns = [int(x) for x in input().split(', ')]
matrix =[[int(x) for x in input().split(' ')] for colum in range(rows)]
result = []

for colum_index in range(columns):
    columns_sum = 0
    for row_index in range(rows):
        columns_sum += matrix[row_index][colum_index]
    result.append(columns_sum)
[print(x) for x in result]
