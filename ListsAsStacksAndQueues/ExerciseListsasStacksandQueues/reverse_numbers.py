integers = input()
stack = integers.split(' ')
revers_number = []
while stack:
    revers_number.append(stack.pop())
print(' '.join(revers_number))



