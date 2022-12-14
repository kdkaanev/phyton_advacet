n = int(input())
battlefield = [[x for x in input()] for r in range(n)]
mine = 0
destroyed_cruiser = 0


def set_position(num):
    for r in range(num):
        for c in range(num):
            if battlefield[r][c] == 'S':
                return r, c


def move(com, r, c):
    poss = r, c
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
    if mine > 2:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break
    if destroyed_cruiser == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break
    command = input()
    r,c  = set_position(n)
    state = move(command,r, c)
    row, col = state
    if battlefield[row][col] == '-':
        battlefield[row][col] = 'S'
        battlefield[r][c] = '-'
        continue
    elif battlefield[row][col] == '*':
        mine += 1
        battlefield[row][col] = 'S'
        battlefield[r][c] = '-'
    elif battlefield[row][col] == 'C':
        destroyed_cruiser += 1
        battlefield[row][col] = 'S'
        battlefield[r][c] = '-'

for line in battlefield:
    print(''.join(line))
