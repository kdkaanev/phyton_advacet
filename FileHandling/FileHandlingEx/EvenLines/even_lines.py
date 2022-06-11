symbols = {"-", ",", ".", "!", "?"}
even_lines = []
reading_file = open('text.txt', 'r')

for index, lines in enumerate(reading_file):

    for symbol in symbols:
        if symbol in lines:
            lines = lines.replace(symbol, '@')
    if index % 2 == 0:
        even_lines.append(lines)
for lines in even_lines:
    s = lines.split()[::-1]
    l = []
    for i in s:
        l.append(i)
    print(" ".join(l))
