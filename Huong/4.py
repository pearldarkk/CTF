a = str(input('Nhap vao vi tri quan xe: '))


def rookmove(pos):
    line = int(pos[2])  # '2' -> 2
    col = pos[1]
    res = []
    for x in range(1, 9):
        # Ra4 -> a1..a8
        if x != line:
            res.append(col + str(x))
    for x in 'abcdefgh':
        # Ra4 ->  a4.. h4
        if x != col:
            res.append(x + str(line))

    for cell in res:
        print(cell, end=' ')
    print()


def rookmove2(pos):
    line = pos[2]  # '2' -> 2
    col = pos[1]
    res = []
    for x in '12345678':
        # Ra4 -> a1..a8
        if x != line:
            res.append(col + x)
    for x in 'abcdefgh':
        # Ra4 ->  a4.. h4
        if x != col:
            res.append(x + line)

    for cell in res:
        print(cell, end=' ')
    print()
    # in cach 2
    print(res)


rookmove(a)
rookmove2(a)