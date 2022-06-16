n = int(input())

matrix = [[x for x in list(input())] for _ in range(n)]
count =0
for r in range(n - 2):
    for c in range(n - 1):
        if matrix[r][c] == 'K':
            if matrix[r + 2][c + 1] == 'K':
                matrix[r + 2][c + 1] = '0'
                count += 1
for r in range(n - 1):
    for c in range(n - 2):
        if matrix[r][c] == 'K':
            if matrix[r + 1][c + 2] == 'K':
                matrix[r + 1][c + 2] = '0'
                count += 1

print(count)
