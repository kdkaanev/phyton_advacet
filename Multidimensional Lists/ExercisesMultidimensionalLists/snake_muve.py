rows, columns = [int(x) for x in input().split()]
string = input()
matrix = []

for j in range(1,rows+1):
    new_string = ''
    for i in range(columns):
        new_string += string[i]
    string = string[columns:] + new_string
    if j % 2== 0:
        new_string = new_string[::-1]
    
    matrix.append(new_string)
[print(x) for x in matrix]
    
