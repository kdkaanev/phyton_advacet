
def bunny(field, n):
    for row in range(n):
        for col in range(n):
            if field[row][col] == 'B':
                bunny_position = row, col
                break
    return bunny_position


def up(r, c, n, field):
    up_point = 0
    up_route = []
    for i in range(r - 1, -1, -1):
        if field[i][c] == 'X':
            break
        up_route.append([i, c])
        up_point += int(field[i][c])
    result = 'up', up_route, up_point
    return result


def down(r, c, n, field):
    down_point = 0
    down_route = []
    for i in range(r + 1, n):
        if field[i][c] == 'X':
            break
        down_route.append([i, c])
        down_point += int(field[i][c])
    return 'down', down_route, down_point


def left(r, c, n, field):
    left_point = 0
    left_route = []
    for i in range(c - 1, -1, -1):
        if field[r][i] == 'X':
            break
        left_route.append([r, i])
        left_point += int(field[r][i])
    return 'left', left_route, left_point


def right(r, c, n, field):
    right_point = 0
    right_route = []
    for i in range(c + 1, n):
        if field[r][i] == 'X':
            break
        right_route.append([r, i])
        right_point += int(field[r][i])
    return 'right', right_route, right_point


def best_way(u, d, l, r):
    best_direction = ''
    best_route = []
    best_point = float('-inf')
    all_dict = {
        u[0]: [u[1], u[2]],
        d[0]: [d[1], d[2]],
        l[0]: [l[1], l[2]],
        r[0]: [r[1], r[2]]
    }
    for d, v in all_dict.items():
        if v[1] > best_point:
            best_point = v[1]
            best_direction = d
            best_route = v[0]
    result =  best_direction,best_route, best_point
    return result


n = int(input())
field = [[x for x in input().split()] for _ in range(n)]
r = bunny(field, n)[0]
c = bunny(field, n)[1]
u = up(r, c, n, field)
d = down(r, c, n, field)
l = left(r, c, n, field)
r = right(r, c, n, field)

print(best_way(u,d,l,r)[0])
for coordinat in best_way(u,d,l,r)[1]:
    print(coordinat)
print(best_way(u,d,l,r)[2])
