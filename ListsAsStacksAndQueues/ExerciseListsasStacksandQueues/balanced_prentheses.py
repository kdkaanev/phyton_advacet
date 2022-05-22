bracket_string = input()
bracket_stack = []
balanced = True
pairs = {
    '(':')',
    '{':'}',
    '[':']'
}
for ch in bracket_string:
    if ch in '({[':
        bracket_stack.append(ch)
    else:
        last_opening_bracket = bracket_stack.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
            break
if balanced:
    print('YES')
else:
    print('NO')


