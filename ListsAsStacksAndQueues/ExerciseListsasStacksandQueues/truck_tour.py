from collections import deque

pumps_number = int(input())
circle = deque()
for _ in range(pumps_number):
    circle.append([int(p) for p in input().split(' ')])
for attempt in range(pumps_number):
    failed= False
    trunk = 0
    for petrol, distance in circle:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break
    if failed:
        circle.append(circle.popleft())
    else:
        print(attempt)
        break


