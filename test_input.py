import sys
from io import StringIO

test_input1 = '''5 4
A A B D
A A B B
I J B B
C C C G
C C K P



'''
# test_input2 = '''2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
