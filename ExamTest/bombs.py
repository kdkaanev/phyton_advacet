from collections import deque

bomb_effects = deque([5, 25, 25, 115])
bomb_casing = [5, 15, 25, 35]
bomb_pouch = False

bomb = {
    40: ['Datura Bombs', 0],
    60: ['Cherry Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}

while True:
    if not bomb_effects or not bomb_casing:
        print("You don't have enough materials to fill the bomb pouch.")
        break
    if bomb_pouch:
        print("Bene! You have successfully filled the bomb pouch!")
        break
    eff = bomb_effects.popleft()
    cas = bomb_casing.pop()
    mix = eff + cas
    for key, value in bomb.items():
        if key == mix:
            bomb[key][1] += 1
        else:
            bomb_effects.appendleft(eff)
            bomb_casing.append(cas - 5)
