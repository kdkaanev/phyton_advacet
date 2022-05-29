text = input()
symbols = {}
for ch in text:
    if ch not in symbols:
        symbols[ch] = 0
    symbols[ch] += 1
for key,value in sorted(symbols.items()):
    print(f'{key}: {value} time/s')
