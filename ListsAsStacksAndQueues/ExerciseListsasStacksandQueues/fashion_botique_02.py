clothes_box = input()
rack_capacity = int(input())
clothes_stack = [int(ch) for ch in clothes_box.split(' ')]
current_capacity = rack_capacity
rack = 1
while clothes_stack:
    clothes = clothes_stack[-1]
    if clothes < current_capacity:
        clothes_stack.pop()
        current_capacity -= clothes
    else:
        rack += 1
        current_capacity = rack_capacity
        clothes_stack.pop()
print(rack)
