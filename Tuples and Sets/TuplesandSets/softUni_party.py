def is_vip(guest):
    return guest[0].isdigit()


number_of_guest = int(input())
vip_guest = set()
reg_guest = set()

for _ in range(number_of_guest):
    reservation = input()
    if is_vip(reservation):
        vip_guest.add(reservation)
    else:
        reg_guest.add(reservation)

while True:
    guest = input()
    if guest == 'END':
        break
    if is_vip(guest):
        vip_guest.remove(guest)
    else:
        reg_guest.remove(guest)

print(len(vip_guest) + len(reg_guest))
[print(guest) for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(reg_guest)]

