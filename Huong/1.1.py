# Tao mot ma tran bang python roi check giong 1
matrix = []


def creatematrix():
    row = []
    for char in range(ord('a'), ord('h')):
        for digit in range(ord('1'), ord('8')):
            cell = chr(char) + chr(digit)
        row.append(cell)
        matrix.append(row)


def check(pos):
    for i in range(8):
        for j in range(8):
            if pos == matrix[i][j]:
                return True
    return False


creatematrix()
cell = str(input("nhap o: "))
print(check(cell))