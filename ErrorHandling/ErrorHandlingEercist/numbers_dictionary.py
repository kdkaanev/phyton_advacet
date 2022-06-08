import sys
from io import StringIO
test_input1 = '''one
1
two
2
Search
one
Remove
two
End

'''
test_input2 = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''
sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)

numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    number = int(input())
    numbers_dictionary[number_as_string] = number
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
