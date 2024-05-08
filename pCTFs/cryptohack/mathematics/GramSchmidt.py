from sage.all_cmdline import *  # import sage library

V = matrix(QQ, [[4.0, 1.0, 3.0, -1.0], [2.0, 1.0, -3.0, 4.0],
                [1.0, 0.0, -2.0, 7.0], [6.0, 2.0, 9.0, -5.0]])
# print(V.gram_schmidt())
print(round(V.gram_schmidt()[0][3][1],5))


# Self-implement:
# import numpy as np


# def gram_schmidt(v):
#     """Orthogonalize a set of vectors stored as the columns of matrix A."""
#     # Get the number of vectors.
#     u = [v[0]]

#     for vi in v[1:]:
#         mi = [np.dot(vi, uj) / np.dot(uj, uj) for uj in u]
#         u += [vi - sum([mij * uj for (mij, uj) in zip(mi, u)])]
#     return u


# if __name__ == "__main__":
#     v = [
#         np.array([4, 1, 3, -1]),
#         np.array([2, 1, -3, 4]),
#         np.array([1, 0, -2, 7]),
#         np.array([6, 2, 9, -5]),
#     ]
#     u = gram_schmidt(v)
#     print(round(u[3][1], 5))