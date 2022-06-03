from collections import deque


def operation(ex, op):
    if op == '*':
        value = 1
        while ex:

            value *= int(ex.popleft())
        ex = ex.append(value)

    elif op == '+':
        pass
    elif op == '-':
        pass
    elif op == '/':
        pass
    return ex


string_expression = '6 3 * 2 1 * 5 /'
list_expression = string_expression.split(' ')
operators = ["*", "+", "-", "/"]
expression = deque()

for symbol in list_expression:
    if symbol not in operators:
        expression.append(symbol)
    else:
        expression.(operation(expression, symbol))
print()
