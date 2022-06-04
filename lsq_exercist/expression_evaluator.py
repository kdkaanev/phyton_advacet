from collections import deque

expresion = input().split()
integers = deque()
operators = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,

}

for symbol in expresion:
    if symbol in '*+-/':
        while len(integers) > 1:
            left = integers.popleft()
            right = integers.popleft()
            result = operators[symbol](left, right)
            integers.appendleft(result)
    else:
        integers.append(int(symbol))
[print(x) for x in integers]
