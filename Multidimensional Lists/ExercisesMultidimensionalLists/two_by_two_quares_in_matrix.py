rows, columns = (int(x) for x in input().split())
matrix = [[letter for letter in input().split()] for _ in range(rows)]
count_square_matrix = 0
for row in range(rows - 1):
    for column in range(columns - 1):
        square_matrix = []
        for n in range(row, row + 2):
            for m in range(column, column + 2):
                square_matrix.append(matrix[n][m])
        result = all(element == square_matrix[0] for element in square_matrix)
        if (result):
            count_square_matrix += 1
print(count_square_matrix)
