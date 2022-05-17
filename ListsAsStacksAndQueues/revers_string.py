input_string = input()
revers_string = ''
s= []
for c in input_string:
    s.append(c)
while s:
    revers_string += s.pop()
print(revers_string)
