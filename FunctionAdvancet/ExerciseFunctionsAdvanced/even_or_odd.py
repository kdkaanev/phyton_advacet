def even_odd(*args):
    result = []
    command = args[-1]
    check = 0 if command == 'even' else 1
    for i in range(len(args) - 1):
        if args[i] % 2 == check:
            result.append(args[i])

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
