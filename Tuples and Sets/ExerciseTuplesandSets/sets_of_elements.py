numbers = input().split(' ')
n, m = int(numbers[0]), int(numbers[1])

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
    #number = input()
    #n_set.add(number)

for _ in range(m):
    m_set.add(input())
    #number = input()
    #m_set.add(number)
new_set = n_set.intersection(m_set)
[print(num) for num in new_set]
