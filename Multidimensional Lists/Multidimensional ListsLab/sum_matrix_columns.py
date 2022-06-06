
rows, columns = [int(x) for x in input().split(', ')]
matrix =[[int(x) for x in input().split(' ')] for colum in range(rows)]
result = []

for colum_index in range(columns):
    columns_sum = 0
    for row_index in range(rows):
        columns_sum += matrix[row_index][colum_index]
    result.append(columns_sum)
[print(x) for x in result]
