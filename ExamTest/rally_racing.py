n = int(input())
car_number = input()
race_route = [[x for x in input().split(' ')] for r in range(n)]
end = False
distance = 0
coor = 0, 0
def coordinate(command, r, c):


    if command == 'left':
        c -= 1
    elif command == 'right':
        c += 1
    elif command == 'up':
        r -= 1
    elif command == 'down':
        r += 1
    return r, c


def tunel(matrix, num):
    for row in range(num):
        for coll in range(num):
            if matrix[row][coll] == 'T':
                matrix[row][coll] = '.'




while True:

    order = input()
    if order == 'End':
        end = True
        break
    symbol = race_route[coordinate(order)[0]][coordinate(order)[1]]
    if symbol == '.':
        distance += 10
    elif symbol == 'T':
        symbol = '.'
        distance += 30
        tunel(race_route, n)
    elif symbol == 'F':
        distance += 10
        break

print()





