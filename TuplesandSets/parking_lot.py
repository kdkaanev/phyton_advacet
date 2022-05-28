n = int(input())
parking = set()
for _ in range(n):
    parking_lot_log = input().split(', ')
    direction, car_number = parking_lot_log[0], parking_lot_log[1]
    if direction == 'IN':
        parking.add(car_number)
    elif direction == 'OUT':
        parking.remove(car_number)
if len(parking) > 0:
    [print(car) for car in parking]
else:
    print("Parking Lot is Empty")

