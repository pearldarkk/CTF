from PIL import Image, ImageChops

i1 = Image.open('lemur.png')
i2 = Image.open('flag.png')

p1 = i1.load()
p2 = i2.load()

w, h = i1.size

for i in range(w):
    for j in range(h):
        (r1, g1, b1) = p1[i, j]
        (r2, g2, b2) = p2[i, j]
        r = r1 ^ r2
        g = g1 ^ g2
        b = b1 ^ b2
        p1[i, j] = (r, g, b)

i1.save("merged.png")
        