from collections import deque

jobs = deque([3, 1, 10, 1, 2])
idx = 0
cycles = 0
target = jobs[idx]


while True:
    for i in range(len(jobs)):
        current = jobs.popleft()


print()
