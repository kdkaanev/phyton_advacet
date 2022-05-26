from collections import deque

food_quantity = int(input())
orders = input().split(' ')
queue = deque([int(o) for o in orders])
max_order = max(queue)
print(max_order)
while queue:
    order = queue.popleft()
    if order <= food_quantity:
        food_quantity -= order
    else:
        queue.appendleft(order)
        break

if len(queue) == 0:
    print('Orders complete')
else:
    queue_string = [str(x) for x in queue]
    left = ' '.join(queue_string)
    print(f"Orders left: {left}")
