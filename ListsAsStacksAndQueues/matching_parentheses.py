exprecion = input()
s = []
for i in range(len(exprecion)):
    if exprecion[i] == '(':
        s.append(i)
    elif exprecion[i] == ')':
        start_index = s.pop()
        end_index = i + 1
        print(exprecion[start_index:end_index])
