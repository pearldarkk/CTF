import numpy as np
import numpy.linalg as linalg


def Vol(A):
    return round(abs(linalg.det(A)))


if __name__ == '__main__':
    A = np.array([[6, 2, -3], [5, 1, 4], [2, 7, 1]])
    print(Vol(A))