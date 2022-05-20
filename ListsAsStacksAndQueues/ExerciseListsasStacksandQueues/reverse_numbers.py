'''
integers = input()
stack = integers.split(' ')
revers_number = []
while stack:
    revers_number.append(stack.pop())
print(' '.join(revers_number))
'''

numbers = input().split(' ')
while numbers:
    revers_number = numbers.pop()
    print(revers_number, end=' ')
