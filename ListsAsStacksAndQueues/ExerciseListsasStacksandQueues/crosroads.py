import queue
from collections import deque

green_light = int(input())
yellow_light = int(input())
command = input()
is_crash = False
cars = deque()
passed = 0
last_car = ''
while True:
    green_time = green_light
    yellow_time = yellow_light
    if command == 'END' or is_crash:
        break
    elif command == 'green':
        while True and cars:
            if green_time > 0:
                car = cars.pop()
                if car <= green_time:
                    green_time -= car
                    passed += 1
                elif car > green_time + yellow_time:
                    is_crash = True
                    index = green_time + yellow_time
                    break
                else:
                    passed += 1
                    break
            else:
                break
    else:
        car_model = len(command)
        cars.appendleft(car_model)
        last_car = command
    command = input()
if is_crash:
    print(f"A crash happened!")
    print(f"{last_car} was hit at {last_car[index]}.")
else:
    print(f"Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")

