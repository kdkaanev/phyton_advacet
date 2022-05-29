one = input().split(' ')
two = input().split(' ')
n = int(input())
sequence_one = set()
for num in one:
    sequence_one.add(num)
sequence_two = set()
for num in two:
    sequence_two.add(num)
for _ in range(n):
    command = input()
    data = command.split(' ')
    if 'Add First' in command:
        for i in range(2,len(data)):
            sequence_one.add(data[i])
    elif 'Add Second' in command:
        for i in range(2,len(data)):
            sequence_two.add(data[i])
    elif 'Remove First' in command:
        for i in range(2,len(data)):
            sequence_one.remove(data[i])
    elif 'Remove Second' in command:
        for i in range(2,len(data)):
            if data[i] in sequence_two:
                sequence_two.remove(data[i])
    elif 'Check Subset' in command:
        if sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one):
            print(True)
        else:
            print(False)
first =  [elem1 for elem1 in sorted(sequence_one)]
second = [elem2 for elem2 in sorted(sequence_two)]
print(', '.join(first))
print(', '.join(second))
