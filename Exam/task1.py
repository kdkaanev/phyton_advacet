from collections import deque

egg_size = [int(x) for x in input().split(', ')]
egg_size.reverse()
paper_size = deque([int(x) for x in input().split(', ')])
fill_boxes = 0

while True:
    if not egg_size or not paper_size:
        break

    egg = egg_size.pop()
    if egg <= 0:
        continue
    paper = paper_size.pop()
    if egg == 13:
        first = paper_size.popleft()
        paper_size.appendleft(paper)
        paper_size.append(first)
        continue
    if egg + paper <= 50:
        fill_boxes += 1
if fill_boxes > 0:
    print(f'Great! You filled {fill_boxes} boxes.')

    if len(paper_size) > 0:
        boxes = [str(x) for x in paper_size]
        left = ', '.join(boxes)
        print(f"Pieces of paper left: {left}")

    elif len(egg_size) > 0:
        egg_size.reverse()
        eggs = [str(x) for x in egg_size]
        print(f'Eggs left: {", ".join(eggs)}')

else:
    print(f"Sorry! You couldn't fill any boxes!")
