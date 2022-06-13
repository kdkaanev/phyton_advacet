n =int(input())
matrix = [[int(x) for x in input(' ').split()] for row in range(n)]
primary_diagonal = []
secondary_diagonal = []
for r in range(n):
    for c in range(n):
        if r == c:
            primary_diagonal.append(matrix[r][c])
        if r == n - c -1:
            secondary_diagonal.append(matrix[r][c])
primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)
absolut_diference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(absolut_diference)


