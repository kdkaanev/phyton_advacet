

n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
print([num for element in matrix for num in element])
