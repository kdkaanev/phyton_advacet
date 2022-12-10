n = int(input())
car_number = input()
race_route = [[x for x in input().split(' ')] for r in range(n)]
end = False
distance = 0
car_row, car_col = 0, 0


def coordinate(direction, car_row, car_col):
    if direction == 'left':
        return car_row, car_col - 1
    elif direction == 'right':
        return car_row, car_col + 1
    elif direction == 'up':
        return car_row - 1, car_col
    elif direction == 'down':
        return car_row + 1, car_col


def tunel(matrix, num):
    for row in range(num):
        for coll in range(num):
            if matrix[row][coll] == 'T':
                matrix[row][coll] = '.'
                break
        else:
            continue
        break

    return row, coll


while True:

    order = input()
    if order == 'End':
        end = True
        race_route[car_row][car_col] = 'C'
        break
    car_row, car_col = coordinate(order, car_row, car_col)
    if race_route[car_row][car_col] == '.':
        distance += 10
    elif race_route[car_row][car_col] == 'T':
        race_route[car_row][car_col] = '.'
        distance += 30
        car_row, car_col = tunel(race_route, n)
    elif race_route[car_row][car_col] == 'F':
        distance += 10
        race_route[car_row][car_col] = 'C'
        break

if end:
    print(f"Racing car {car_number} DNF.")
else:
    print(f"Racing car {car_number} finished the stage!")

print(f"Distance covered {distance} km.")
for line in race_route:
    print(''.join(map(str, line)))
