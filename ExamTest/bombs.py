from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casing = [int(x) for x in input().split(', ')]

bomb = {
    40: ['Datura Bombs', 0],
    60: ['Cherry Bombs', 0],
    120: ['Smoke Decoy Bombs', 0]
}


def pouch_check(a, b, c):
    return all(x >= y for x, y in zip((a, b, c), (3, 3, 3)))


while True:
    bomb_pouch = pouch_check(bomb[40][1], bomb[60][1], bomb[120][1])
    if not bomb_effects or not bomb_casing:
        print("You don't have enough materials to fill the bomb pouch.")
        break
    if bomb_pouch:
        print("Bene! You have successfully filled the bomb pouch!")
        break

    eff = bomb_effects.popleft()
    cas = bomb_casing.pop()

    for key, value in bomb.items():
        if key == eff + cas:
            value[1] += 1
            break
    else:
        bomb_effects.appendleft(eff)
        if cas >= 5:
            bomb_casing.append(cas - 5)
bombs = []
for key, value in bomb.items():
    bombs.append(str(value[0]) + ': ' + str(value[1]))

if not bomb_effects:
    print('Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')

if not bomb_casing:
    print('Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casing])}')

for bomb in sorted(bombs):
    print(bomb)
