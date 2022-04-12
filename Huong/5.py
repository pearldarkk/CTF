pos = str(input('Nhap vao vi tri quan tuong: '))


def bishopMove(pos):
    moves = []
    row = ord(pos[2]) - ord('1')
    column = ord(pos[1]) - ord('a')
    for i, j in zip(range(ord(pos[0]),
                          ord('h') + 1), range(ord(pos[1]), ord('9'))):
        cell = chr(ord(i)) + chr(ord(j))
        moves.append(cell)
    print(moves)


bishopMove('ta4')
