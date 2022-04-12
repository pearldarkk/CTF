a = str(input('nhap vi tri o co thu nhat: '))
# nhieu hon 2 ky tu thi bao k hop le
a = a.strip()
if len(a) > 2:
    print("Invalid input")
    exit(0)

b = str(input('nhap vi tri o co thu hai : '))
b = b.strip()
if len(b) > 2:
    print("Invalid input")
    exit(0)


def checkDuplicate(pos1, pos2):
    if pos1[0] == pos2[0] or pos1[1] == pos2[1]:
        return True
    else:
        return False


def checkDuplicate2(pos1, pos2):
    if pos1[0] == pos2[0]:
        return True
    if pos1[1] == pos2[1]:
        return True
    return False


if checkDuplicate(a, b):
    print("Trung!")
else:
    print("Khong trung!")
print(checkDuplicate(a, b))
