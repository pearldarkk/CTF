f = open("shiftNbases.txt", "r")
cipher = f.read().split()
f.close()

base = [8, 10, 16, 10]
text = ""
for i in range(0, len(cipher)):
    text += chr(int(cipher[i], base[i % 4]))

text = text.replace('ISP_IN_YOUR_AREA', '')

plain = ''
shiftkey = '19051890'
for i in range(0, len(text)):
    if i % 2 == 0:
        plain += chr(ord(text[i]) + int(shiftkey[i % 8]))
    else:
        plain += chr(ord(text[i]) - int(shiftkey[i % 8]))

print(plain)