from collections import deque

food_quantity = int(input())
orders = input().split(' ')
queue = deque([int(o) for o in orders])
max_order = max(queue)
print(max_order)
for order in queue:
    if order <= food_quantity:
        food_quantity -= order
        queue.popleft()
    else:
        break
print()
