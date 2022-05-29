def output(even, odd):
    sum_even = sum(even)
    sum_odd =  sum(odd)
    if sum_even == sum_odd:
        value = odd.union(even)
    elif sum_even >sum_odd:
        value = odd.symmetric_difference(even)
    else:
        value = odd.difference(even)
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
print(*final, sep=', ')
