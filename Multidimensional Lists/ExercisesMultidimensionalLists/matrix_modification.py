n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]
commnd = input()
while commnd != 'END':
    data = commnd.split()
    action, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])
    if 0 <= row <= n and 0 <= col <= n:                                                                                                                   
        if action == 'Add':
            matrix[row][col] += value
        elif action == 'Subtract':
            matrix[row][col] -= value
        else:
            print('Invalid coordinates')
    commnd = input()
