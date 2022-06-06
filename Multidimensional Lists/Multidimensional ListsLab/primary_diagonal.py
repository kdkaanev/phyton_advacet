import sys
from io import StringIO
test_input1 = '''3
11 2 4
4 5 6
10 8 -12

'''
test_input2 = '''3
1 2 3
4 5 6
7 8 9

'''
#sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)

n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
result = 0
for colum_index in range(n):
    for row_index in range(n):
        if colum_index == row_index:
            result += matrix[row_index][colum_index]
print(result)


