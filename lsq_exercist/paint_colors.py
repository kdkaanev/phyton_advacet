text = input()
colors = text.split()
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
output = []
mixed_color = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']

}
while colors:
    first_string = colors.pop(0)
    second_string = colors.pop(-1) if colors else ''
    substring = first_string + second_string
    if substring in main_colors or substring in secondary_colors:
        output.append(substring)
        continue
    substring = second_string + first_string
    if substring in main_colors or substring in secondary_colors:
        output.append(substring)
        continue

    first_string = first_string[:-1]
    second_string = second_string[:-1]
    if first_string:
        colors.insert(len(colors) // 2, first_string)
    if second_string:
        colors.insert(len(colors) // 2, second_string)
result = []

for color in output:
    if color in main_colors:
        result.append(color)
        continue
    is_colected = True
    for help_color in mixed_color[color]:
        if help_color not in output:
            is_colected =False
            break
    if is_colected:
        result.append(color)
print(result)
