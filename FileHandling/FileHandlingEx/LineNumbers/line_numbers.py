def number_of_chars(line):
    import re
    punctuation = "\W+"

    punctuation_marks = re.findall(punctuation, line)
    punctuation_marks = [ch for ch in punctuation_marks if ch != ' ']
    letter_count = 0
    for ch in line:
        if ch.isalpha():
            letter_count += 1
    return f'({letter_count})({len(punctuation_marks)})'


with open('./text.txt', 'r') as text, open('./output.txt', 'w') as output:
    for index, line in enumerate(text):
        output.write(f'Line {index + 1}: {line.strip()} {number_of_chars(line)}\n')


