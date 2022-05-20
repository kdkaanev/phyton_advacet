n = int(input())
stack = []
for _ in range(n):
    command = input()
    if command == '2':
        if len(stack) > 0:
            stack.pop()
    elif command.startswith('1 '):
        data = command.split(' ')
        number = int(data[1])
        stack.append(number)
    elif command == '3':
        print(max(stack))
    elif command == '4':
        print(min(stack))
stack.reverse()
print(', '.join(map(str, stack)))
