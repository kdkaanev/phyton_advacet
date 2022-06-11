import re

with open('text.txt', 'r') as words:
    words = words.read().split()

words_count = {
    word: 0 for word in words
}

with open('input_text.txt') as text:
    for line in text:
        word_in_text = [w.lower() for w in re.findall(r'\b\S+\b', line)]
        for word in words:
            words_count[word] += word_in_text.count(word.lower())

words_count_sorted = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
[
    print(f'{w} - {c}') for w, c in words_count_sorted
]
