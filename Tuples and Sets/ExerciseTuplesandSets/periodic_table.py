n = int(input())
chemical_elements = set()
for _ in range(n):
    chemical_compound  = [co for co in input().split(' ')]
    for element in chemical_compound:
        chemical_elements.add(element)
[print(element) for element in chemical_elements]
