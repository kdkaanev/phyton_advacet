n = int(input())
stack = []
for _ in range(n):
    command = input()
    if command == '2' and stack:
            stack.pop()
    elif command.startswith('1 '):
        data = command.split(' ')
        number = int(data[1])
        stack.append(number)
    elif command == '3' and stack:
        print(max(stack))
    elif command == '4' and stack:
        print(min(stack))
#stack.reverse()
stack_revers = []
while stack:
    stack_revers.append(stack.pop())
print(', '.join(map(str, stack_revers)))

