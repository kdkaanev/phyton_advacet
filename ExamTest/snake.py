n = int(input())
area = [[x for x in input()] for r in range(n)]
food_quantity = 0


def set_position(n):
    for r in range(n):
        for c in range(n):
            if area[r][c] == 'S':
                return (r, c)


def check_out(poss, n):
    r, c = poss
    return 0 <= r < n and 0 <= c < n


def check_burrow(s, a):
    row, colum = s
    return a[row][colum] == 'B'


def move(com, poss):
    r, c = poss
    if com == 'up':
        poss = (r - 1, c)
    elif com == "down":
        poss = (r + 1, c)
    elif com == "left":
        poss = (r, c - 1)
    elif com == "right":
        poss = (r, c + 1)
    return poss


while True:
    if food_quantity >= 10:
        print('You won! You fed the snake.')
        break

    command = input()
    initial_coordinate = set_position(n)
    state = move(command, initial_coordinate)
    r, c = state
    if not check_out(state, n):
        r, c = initial_coordinate
        area[r][c] = '.'
        print('Game over!')
        break
    if check_burrow(state, area):
        area[initial_coordinate[0]][initial_coordinate[1]] = '.'
        area[state[0]][state[1]] = '.'
        for r in range(n):
            for c in range(n):
                if area[r][c] == 'B':
                    area[r][c] = 'S'

        continue

    elif area[r][c] == '*':
        food_quantity += 1

    area[state[0]][state[1]] = 'S'
    area[initial_coordinate[0]][initial_coordinate[1]] = '.'
print(f"Food eaten: {food_quantity}")
for line in area:
    print(''.join(line))
