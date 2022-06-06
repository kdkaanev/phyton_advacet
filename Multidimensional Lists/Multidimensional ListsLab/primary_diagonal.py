

n = int(input())
matrix = [[int(x) for x in input().split()] for row in range(n)]
result = 0
for colum_index in range(n):
    for row_index in range(n):
        if colum_index == row_index:
            result += matrix[row_index][colum_index]
print(result)


