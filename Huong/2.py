#bai 1
def rookDefaultPosition():
    # quan 1
    print("Quan xe den: " + chessboard[0][0])
    # quan 2
    print("Quan xe den 2: " + chessboard[0][7])
    # quan 3
    print("Quan xe trang 1: " + chessboard[7][0])
    # quan 4
    print("Quan xe trang 1: " + chessboard[7][7])


def rookDefaultPosition2():
    # quan den
    print("Quan xe den: " + chessboard[0][0] + ", " + chessboard[0][7])
    # quan trang
    print("Quan xe trang: " + chessboard[7][0] + ", " + chessboard[7][7])


def rookDefaultPosition3():
    # 4 quan den
    print("4 quan xe: " + chessboard[0][0] + "," + chessboard[0][7] + ", " +
          chessboard[7][0] + ", " + chessboard[7][7])


# bai 2
def cellPrint():
    print("Ban co: ")
    for row in chessboard:
        for cell in row:
            print(cell, end=', ')
        print()


def cellPrint2():
    print("Ban co: ")
    for i in range(8):
        for j in range(8):
            print(chessboard[i][j], end=' ')
        print()


def cellPrint3():
    print("Ban co: ")
    for i in range(8):
        for j in range(8):
            print(chessboard[i][j], end='|')
        print()
        print('___' * 8)


# bai 3
def whiteCell():
    print("Cac o trang: ")
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    print(chessboard[i][j], end=' ')
            if i % 2 == 1:
                if j % 2 == 1:
                    print(chessboard[i][j], end=' ')
    print()


def whiteCell2():
    print("Cac o trang: ")
    for i in range(8):
        if i % 2 == 0:
            for j in range(8):
                if j % 2 == 0:
                    print(chessboard[i][j], end=' ')
        else:
            for j in range(8):
                if j % 2 == 1:
                    print(chessboard[i][j], end=' ')
    print()


def whiteCell3():
    print("Cac o trang: ")
    for i in range(8):
        if i % 2 == 0:
            for j in range(0, 8, 2):
                if j % 2 == 0:
                    print(chessboard[i][j], end=' ')
        else:
            for j in range(1, 8, 2):
                print(chessboard[i][j], end=' ')
    print()


# bai 4


# bai 4
def createMatrix():
    print("Theo goc nhin cua ben cam quan trang, ban co: ")
    matrix = []
    for digit in range(ord('8'), ord('1') - 1, -1):
        row = []
        for char in range(ord('a'), ord('h') + 1):
            cell = chr(char) + chr(digit)
            row.append(cell)
        matrix.append(row)

    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()


def createMatrix2():
    print("Theo goc nhin cua ben cam quan trang, ban co: ")
    matrix = []
    for digit in range(ord('8'), ord('1') - 1, -1):
        row = []
        for char in range(ord('a'), ord('h') + 1):
            cell = chr(char) + chr(digit)
            row.append(cell)
        matrix.append(row)

    for i in range(8):
        for j in range(8):
            print(matrix[i][j], end=' ')
        print()


# tao ban co
chessboard = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
              ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
              ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
              ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
              ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
              ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
              ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
              ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

rookDefaultPosition()
cellPrint()
# cellPrint2()
# cellPrint3()
whiteCell()
whiteCell2()
whiteCell3()
createMatrix()
