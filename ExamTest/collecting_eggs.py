from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]
box = 50
full_boxes = 0

while True:
    if not eggs or not papers:
        break
    egg = eggs.popleft()
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    if egg <= 0:
        continue
    paper = papers.pop()
    assembled = egg + paper
    if assembled <= box:
        full_boxes += 1
if full_boxes > 0:
    print(f"Great! You filled {full_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")

