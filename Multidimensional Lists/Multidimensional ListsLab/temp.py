import sys
from io import StringIO
test_input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9

'''
#test_input2 = '''2, 4
#10, 11, 12, 13
#14, 15, 16, 17

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)










n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    for colunm in range(n):
        if row == colunm:
            primary_diagonal.append(matrix[row][colunm])
        if row == n - colunm -1:
            secondary_diagonal.append(matrix[row][colunm])

                    
                    
                    
                    
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     