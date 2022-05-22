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
    elif not bracket_stack:
        balanced = False
    else:
        last_opening_bracket = bracket_stack.pop()
        if pairs[last_opening_bracket] != ch:
            balanced = False
    if not balanced:
        break
if  not balanced or bracket_stack:
    print('NO')
else:
    print('YES')


