from collections import deque

elfs_energy = deque(int(x) for x in input().split(' '))
materials = [int(x) for x in input().split()]
total_energy = 0
total_toys = 0
day = 0
while True:
    if not elfs_energy or not materials:
        break
    day += 1
    elf = elfs_energy.popleft()
    toy = materials.pop()
    if elf < 5:
        continue
    if elf < toy:
        elfs_energy.append(elf * 2)
        materials.append(toy)
    elif day % 3 == 0:
        if elf < toy * 2:
            elfs_energy.append(elf * 2)
            materials.append(toy)

        elif day % 5 != 0:
            total_energy += toy * 2
            total_toys += 2
            elfs_energy.append(elf - toy + 1)
        elif day % 5 == 0:
            elfs_energy.append(elf - toy)
            total_energy += toy * 2

    else:
        total_energy += toy
        total_toys += 1
        elfs_energy.append(elf - toy + 1)
        if day % 5 == 0:
            total_toys -= 1
            elfs_energy.append(elf - toy)
            total_energy += toy
print()
