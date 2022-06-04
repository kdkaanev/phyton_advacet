from collections import deque

symbol = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: abs(a - b),
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

bees = deque([int(x) for x in input().split()])
total_nectar = [int(x) for x in input().split()]
symbols_sequence = deque([x for x in input().split()])
honey = 0

while bees and total_nectar:
    bee = bees.popleft()
    nectar = total_nectar.pop()
    while bee >= nectar:
        nectar = total_nectar.pop()
    current_symbol = symbols_sequence.popleft()
    honey += symbol[current_symbol](bee, nectar)

print(f"Total honey made: {honey}")
if bees:
    bees_left = [str(b) for b in bees]
    print(f"Bees left: {', '.join(bees_left)}")
if total_nectar:
    nectar_left = [str(n) for n in total_nectar]
    print(f"Nectar left: {', '.join(nectar_left)}")


