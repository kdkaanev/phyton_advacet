text = 're ple blu pop e pur d'
colors = text.split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
output = []
while colors:
    first_string = colors.pop(0)
    if len(colors) > 1:
        second_string = colors.pop(-1)
        substring = first_string + second_string
    else: substring =first_string
    if substring in main_colors or substring in secondary_colors:
        output.append(substring)
    else:
        first_string = first_string[:-1]
        second_string = second_string[:-1]
        if first_string :
            colors.insert(len(colors)//2, first_string)
        if second_string:
            colors.insert(len(colors)//2,second_string)
print()