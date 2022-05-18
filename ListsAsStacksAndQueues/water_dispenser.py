
'''
1.quantity of water- input int
2. until 'start'=> input name of people who wanted water
  add name to queue
3. until 'end' => input command
    if command is 'litrers' = int
        if liters is < = quanity of water => print name and remove from queue
        and reduce water quanity
        else print person must wait and remove to queue
    if command is 'refill {liters}
        add liters to quanity water
4. in the end print quanity water


'''
from collections import deque
water_quantity = int(input())
queue = deque()
while True:
    command = input()
    if command == 'Start':
        break
    queue.append(command)
while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill '):
        data = command.split(' ')
        water_quantity += int(data[1])
    else:
        liters = int(command)
        name = queue.popleft()
        if liters <= water_quantity:
            water_quantity -= int(command)
            print(f"{name} got water" )
        else:
            print(f"{name} must wait" )

print(f"{water_quantity} liters left")









