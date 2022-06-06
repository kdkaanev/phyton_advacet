
n = int(input())
matrix = [[st for st in input()] for row in range(n)]
symbol = input()
is_ok = False
for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:

            is_ok = True
            break
    if is_ok:
        break
if is_ok:
    print(f"({i}, {j})")
else:
    print(f"{symbol} does not occur in the matrix")
