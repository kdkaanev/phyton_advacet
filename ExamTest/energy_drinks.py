from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
limit_caffeine = 300
current_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()
    if caffeine * drink <= limit_caffeine:
        current_caffeine += caffeine * drink
        limit_caffeine = 300 - current_caffeine
    else:
        energy_drinks.append(drink)
        current_caffeine  = max(current_caffeine - 30, 0)
        limit_caffeine = 300 - current_caffeine

if energy_drinks:
    result = [str(d) for d in energy_drinks]
    print(f"Drinks left: {', '.join(result)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {current_caffeine} mg caffeine.")
