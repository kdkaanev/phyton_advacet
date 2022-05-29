lines = int(input())
longest_intersection = set()

for _ in range(lines):
    first_range = set()
    second_range = set()
    data = input().split('-')
    range_one = [int(x) for x in data[0].split(',')]
    range_two = [int(y) for y in data[1].split(',')]
    for i in range(range_one[0], range_one[1] + 1):
        first_range.add(i)
    for j in range(range_two[0], range_two[1] + 1):
        second_range.add(j)
    intersection = first_range.intersection(second_range)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection
longest_intersection_list = [num for num in longest_intersection]
print(f'Longest intersection is {longest_intersection_list} with length {len(longest_intersection_list)}')

