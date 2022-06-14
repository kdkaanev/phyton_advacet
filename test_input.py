def check(swap, r, c, val):
    return 'swap' in swap and len(swap) == 5 and all(x >= 0 for x in val) and int(swap[1]) <= r and int(
        swap[3]) <= r and int(swap[2]) <= c and int(swap[4]) <= c


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

command = input()
while command != 'END':
    swap = command.split()
    r1, c1, r2, c2 = int(swap[1]), int(swap[2]), int(swap[3]), int(swap[4])
    value = [r1, c1, r2, c2]
    if check(swap, rows, columns, value):

        a = matrix[r1]
        b = matrix[r2]
        x = a.pop(c1)
        a.insert(c1, b[c2])
        b.pop(c2)
        b.insert(c2, x)
        for element in matrix:
            print(' '.join([str(x) for x in element]))
    else:
        print('Invalid input!')

    command = input()
