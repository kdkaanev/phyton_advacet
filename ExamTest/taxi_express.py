from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    customer = customers.popleft()
    taxi = taxis.pop()
    if customer <= taxi:
        total_time += customer
    else:
        customers.appendleft(customer)

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print('Customers left: ', end='')
    print(*customers, sep=', ')


