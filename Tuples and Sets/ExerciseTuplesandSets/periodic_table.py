n = int(input())
chemical_elements = set()
'''
for _ in range(n):
    chemical_compound  = [co for co in input().split(' ')]
    for element in chemical_compound:
        chemical_elements.add(element)
[print(element) for element in chemical_elements]
'''

for _ in range(n):
    compound = set(element for element in input().split(' '))
    chemical_elements = chemical_elements.union(compound)
[print(element) for element in chemical_elements]
