import sys
from io import StringIO

test_input1 = '''one
two
Search
Remove
End


'''

sys.stdin = StringIO(test_input1)



numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The variable number must be an integer')

    line = input()

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary[searched])
    line = input()

line = input()

while line != "End":
    searched = line
    del numbers_dictionary[searched]
    line = input()

print(numbers_dictionary)
