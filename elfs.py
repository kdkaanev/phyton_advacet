from collections import deque

elfs_energy = deque(int(x) for x in input().split(' '))
materials = [int(x) for x in input().split()]
total_energy = 0
total_toys = 0
count =0
while True:
    if  not elfs_energy or materials:
        break
    elf = elfs_energy.popleft()
    box = materials.pop()
    if count % 3 == 0:
       
       if elf <= box * 2:
           elfs_energy.append(elf * 2)
           materials.append(box)
       else:
          total_toys += 2
          total_energy += elf - box
          elfs_energy.append(elf + 1)
    if count % 5 == 0:
        
          