rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for row in range(rows)]

top_matrix = []
max_points = float('-inf')

for row in range(rows - 2):
    for column in range(columns - 2):
        current_points = 0
        submatrix = []
        for n in range(row, row + 3):
            for m in range(column, column + 3):
                submatrix.append(matrix[n][m])
        current_points += sum(submatrix)
        if current_points > max_points:
            max_points = current_points
            top_matrix = submatrix
total_sum = sum(top_matrix)
format_topmatrix = []
while top_matrix != []:
    format_topmatrix.append(top_matrix[:3])
    top_matrix = top_matrix[3:]
print(f'Sum = {total_sum}')
for element in format_topmatrix:
    print(' '.join([str(x)for x in element]))
