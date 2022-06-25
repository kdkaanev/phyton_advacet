from collections import deque

players = deque([x for x in input().split(', ')])

maze = [[x for x in input().split()] for _ in range(6)]

while True:
    player = players.popleft()
    if 'w' in player:
        player = player[:-1]
        players.append(player)
        continue

    row, col = tuple([int(x) for x in input() if x.isdigit()])

    if maze[row][col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif maze[row][col] == "T":
        print(f"{''.join(player)} is out of the game! The winner is {''.join(players)}.")
        break
    elif maze[row][col] == "W":
        print(f"{player} hits a wall and needs to rest.")
        players.append(player + 'w')
    else:
        players.append(player)
