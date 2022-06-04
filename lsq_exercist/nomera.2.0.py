set_one = set([int(x) for x in input().split()])
set_two = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    data = input().split(' ')
    command = data[0]
    target = data[1]
    if command == 'Add':
        if target == 'First':
            set_one = set_one.union(int(x) for x in data[2:])
        elif target == 'Second':
            set_two = set_two.union(int(x) for x in data[2:])
    elif command == 'Remove':
        if target == 'First':
            set_one = set_one.difference(int(x) for x in data[2:])
        elif target == 'Second':
            set_two = set_two.difference(int(x) for x in data[2:])
    elif command == 'Check':
        print(set_one.issubset(set_two) or set_two.issubset(set_one))
print(*sorted(set_one), sep=', ')
print(*sorted(set_two), sep=', ')
