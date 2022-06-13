n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - i - 1])
primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)
absolut_diference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(absolut_diference)
