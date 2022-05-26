numbers = list(map(float, input().split(' ')))
# numbers = list(map(float, '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'.split(' ')))
numbers_dict = {}

for number in numbers:
    if number not in numbers_dict:
        numbers_dict[number] = 1
    else:
        numbers_dict[number] += 1

for key, value in numbers_dict.items():
    print(f"{key:.1f} - {value} times")
