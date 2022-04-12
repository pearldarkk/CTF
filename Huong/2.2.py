matrix = []


def creatematrix():
    for digit in range(ord('8'), ord('1') - 1, -1):
        row = []
        for char in range(ord('a'), ord('h') + 1):
            cell = chr(char) + chr(digit)
            row.append(cell)
        matrix.append(row)

creatematrix()
for row in matrix:
    for cell in row:
        print(cell, end=' ')
    print()
