n =int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]
primary_diagonal = []
secondary_diagonal = []
for r in range(n):
    for c in range(n):
        if r == c:
            primary_diagonal.append(matrix[r][c])
        if r == n - c -1:
            secondary_diagonal.append(matrix[r][c])
print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}") 
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}") 


