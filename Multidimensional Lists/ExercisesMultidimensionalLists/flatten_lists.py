

string = input().split('|')
revers_list = []

for i in range(len(string) -1, -1, -1):
    current_element = string[i].strip().split()
    revers_list.extend(current_element)
print(' '.join(revers_list))