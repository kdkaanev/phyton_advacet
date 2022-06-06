n, m = [int(x) for x in input().split(', ')]
matrix = []
sum_value = 0
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    sum_value += sum(row)

print(sum_value)
print(matrix)
