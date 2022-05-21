clothes_box = input()
rack_capacity = int(input())
#clothes_stack = [int(ch) for ch in clothes_box if ch != ' ']
clothes_stack = [int(ch) for ch in clothes_box.split(' ')]
rack_number = 1
rack = []

while clothes_stack:
    clothes = clothes_stack.pop()
    rack.append(clothes)
    if rack_capacity < sum(rack):
        rack = []
        rack.append(clothes)
        rack_number += 1
print(rack_number)

