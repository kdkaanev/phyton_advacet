from collections import deque

food_portions = [int(x) for x in input().split(', ')]
stamina = deque([int(x) for x in input().split(', ')])
days = 1

peeks = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,

}
conquered_peeks = []
while days <= 7 and peeks:
    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()
    for peek, level in peeks.items():
        if level <= daily_food + daily_stamina:
            conquered_peeks.append(peek)
            del peeks[peek]
            break
        else:
            break
    days += 1

if not  peeks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print('Conquered peaks:')
    for peek in conquered_peeks:
        print(peek)
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
    if conquered_peeks:
        print('Conquered peaks:')
        for peek in conquered_peeks:
            print(peek)
