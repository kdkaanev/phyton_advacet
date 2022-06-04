from collections import deque

'''
def stack_top(choko):
    result = choko.pop()
    choko.append(result)
    return result
'''

chocolates = [int(x) for x in input().split(', ')]
milk_cup = deque([int(x) for x in input().split(', ')])
milkshake = 0
is_all = False

while True:
    if milkshake == 5:
        is_all = True
    if is_all or not chocolates or not milk_cup:
        break
    else:
        current_cup = milk_cup.popleft()
        current_choko = chocolates.pop()
        if current_choko <= 0 and current_cup <= 0:
            continue
        if current_choko <= 0:
            milk_cup.appendleft(current_cup)
            continue
        if current_cup <= 0:
            chocolates.append(current_choko)
            continue
        if current_choko != current_cup:

            chocolates.append(current_choko - 5)
        elif current_cup == current_choko:
            milkshake += 1

if is_all:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    chocolates = [str(choko) for choko in chocolates]
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")
if milk_cup:
    milk_cup = [(str(milk)) for milk in milk_cup]
    print(f"Milk: {', '.join(milk_cup)}")
else:
    print("Milk: empty")
