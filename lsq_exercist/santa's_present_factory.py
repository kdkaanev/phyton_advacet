from collections import deque

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
is_considered = False

toy = {
    150:['Doll',0],
    250:['Wooden train',0],
    300:['Teddy bear',0],
    400:['Bicycle',0]

}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()
    if magic == 0:
        materials.append(material)
        continue
    if material == 0:
        magics.append(magic)
        continue
    x = material * magic
    if x in toy.keys():
        toy[x][1] += 1
    elif x < 0:
        result = material + magic
        materials.append(result)
    else:
        result = material + 15
        materials.append(result)

if toy[150][1] > 0 and toy[250][1] > 0:
    is_considered = True
if toy[300][1] > 0 and toy[400][1] > 0:
    is_considered = True
if is_considered:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")
presents = {}
for key,value in toy.items():
    presents[value[0]] = value[1]
presents_sorted = {key: value for key, value in sorted(presents.items())}
for toy,number in presents_sorted.items():
    if number > 0:
        print(f'{toy}: {number}')





