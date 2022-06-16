n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]
command = input()
while command != 'END':
    data = command.split()
    action = data[0]
    row, col, value = [int(x) for x in data [1:]]
    if 0 <= row <= n - 1 and 0 <= col <= n - 1:
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
    else:
            print('Invalid coordinates')
    command = input()
for element in matrix:
    print(' '.join([str(x)for x in element]))
