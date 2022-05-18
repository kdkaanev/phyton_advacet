from collections import deque
kids_string = input()
toss_number = int(input())

kids = deque(kids_string.split(' '))
counter = 0
while len(kids) > 1:
    counter += 1
    kid = kids.popleft()
    if counter < toss_number:
        kids.append(kid)
    else:
        print(f"Removed {kid}")
        counter =0
print(f"Last is {' '.join(kids)}")
