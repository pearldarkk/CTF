def checkpos(cell):
    if cell[0] >= 'a' and cell[0] <= 'h':
        if cell[1] >= '1' and cell[1] <= '8':
            return True
    return False


def checkpos1(c):
    if c[0] >= 'a' and c[0] <= 'h' and c[1] >= '1' and c[1] <= '8':
        return True
    return False


cell = str(input('Nhap mot o: '))
cell = cell.strip()
print(checkpos1(cell))
