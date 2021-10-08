from fractions import Fraction as phs
import sys
from math import log2


def ffl(f):
    return str(f)[:7]

def main(list_phs):
    py = [0]*(len(list_phs[0]) - 1)
    for i in range(len(list_phs)):
        # print(list_phs[i][0], end = ' ')
        px = list_phs[i][0]
        for j in range(1, len(list_phs[i])):
            py[j-1] += px * list_phs[i][j]
    hy = 0
    for i, v in enumerate(py):
        print(f"p(y{i}) = {ffl(float(v))}")
        hy += v*log2(1/v)

    hx = 0
    for i in range(len(list_phs)):
        hx += (list_phs[i][0] * log2(1/list_phs[i][0]))
    print(f"H(X)  = {ffl(hx)}")
    print(f"H(Y)  = {ffl(hy)}")

    hy_x = 0
    for i in range(len(list_phs)):
        # print(list_phs[i][0], end = ' ')
        px = list_phs[i][0]
        for j in range(1, len(list_phs[i])):
            if px*list_phs[i][j] != 0: 
                hy_x += (px*list_phs[i][j] * log2(1/list_phs[i][j]))
    print(f"H(Y|X)= {ffl(hy_x)}")

    hx_y = hx + hy_x - hy
    print(f"H(X|Y)= {ffl(hx_y)}")

    hxy = hx + hy_x
    print(f"H(X,Y)= {ffl(hxy)}")

    ixy = hx + hy - hxy
    print(f"I(X,Y)= {ffl(ixy)}")


if __name__ == "__main__":
    l = [[phs(num) for num in line.split(' ')] for line in open('dmc.txt', 'r')]
    main(l)
    
""" dmc.txt
1/4 1/3 2/3  x1  y1|x1  y2|x1
3/4 3/4 1/4  x2  y1|x2  y2|x2

0.18100 0.23400 0.36100 0.40500
0.81900 0.30300 0.30300 0.39400
"""