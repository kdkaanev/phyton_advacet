from collections import deque

seats = [x for x in input().split(', ')]
first_numbers = deque([int(x) for x in input().split(', ')])
second_numbers = deque([int(x) for x in input().split(', ')])
rotations = 0
taken_seats = []

while len(taken_seats) < 3 and rotations < 10:

    n1 = first_numbers.popleft()
    n2 = second_numbers.pop()
    wanted_seat = chr(n1 + n2)
    for seat in taken_seats:
        if seat[-1] == wanted_seat:
            continue
    for seat in seats:
        if seat[-1] == wanted_seat:
            taken_seats.append(seat)
            seats.remove(seat)
            break

    else:
        first_numbers.append(n1)
        second_numbers.appendleft(n2)
    rotations += 1
print('Seat matches: ', end='')
print(*taken_seats, sep=', ')
print(f'Rotations count: {rotations}')
