def output(even, odd):
    if sum(even) == sum(odd):
        value = even.union(odd)
    elif sum(even) > sum(odd):
        value = even.symmetric_difference(odd)
    else:
        value = even.difference(odd)
    return value

n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n + 1):
    result = 0
    name = input()
    for ch in name:
        result += ord(ch)
    result //= row
    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

final = output(even_set, odd_set)
print_list = [str(num) for num in final]
print(', '.join(print_list))

