letters = dict()
letter = 97
for i in range(26):
    letters[i] = chr(letter)
    letter += 1
rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    for c in range(columns):
        elements = letters[r] + letters[c + r] + letters[r]
        matrix.append(elements)
format_matrix = []
while matrix != []:
    format_matrix.append(matrix[:columns])
    matrix = matrix[columns:]
for element in format_matrix:
    print(' '.join([str(x)for x in element]))




