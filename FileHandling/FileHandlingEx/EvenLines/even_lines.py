symbols = ["-", ",", ".", "!", "?"]
even_lines = []

reading_file = open('text.txt', 'r')

for index, lines in enumerate(reading_file):
    if index % 2 == 0:
        line = ' '.join(lines.strip().split()[::-1])
        for symbol in symbols:
            if symbol in line:
                line = line.replace(symbol, '@')
        print(line)
reading_file.close()