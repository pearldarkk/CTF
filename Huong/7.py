def checkConnected(a, b):
    # vector AB
    x = ord(a[0]) - ord(b[0])
    y = ord(a[1]) - ord(b[1])
    if x != 0 and y != 0 and x != y and x != -y:
        return False
    return True


def list(a, b):
    clist = []
    for i, j in zip(range(ord(a[0]),ord(b[0])+1), 
    range(ord(a[1])+1, ord(b[1])+1)):
        cell = chr(i) + chr(j)
        clist.append(cell)
    print(clist)


a = str(input("Nhap a: "))
b = str(input("Nhap b: "))

print(checkConnected(a, b))
if (checkConnected(a, b)):
    list(a, b)
