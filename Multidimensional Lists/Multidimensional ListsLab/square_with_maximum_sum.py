

rows, columns = [int(x) for x in input().split(', ')]
matrix =[[int(x) for x in input().split(', ')] for row in range(rows)]

top_matrix = []
max_points = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_points = 0
        submatrix = []
        for n in range(row, row + 2):
            for m in range(column,column + 2):
                submatrix.append(matrix[n][m])
        current_points += sum(submatrix)
        if current_points > max_points:
            max_points = current_points
            top_matrix = submatrix

for i in range(len(top_matrix)):
    print(top_matrix[i], end=' ')
    if i == 1:
        print()
print()
print(max_points)
