import numpy as np

Items = [(1, 1, 1), (2, 6, 2), (3, 18, 5), (4, 22, 6), (5, 28, 7)]

if __name__ == '__main__':
    M = np.zeros((6, 12))
    for w in range(12):
        M[0, w] = 0
    for i in range(1, 6):
        for w in range(1, 12):
            wi = Items[i - 1][2]
            if wi > w:
                M[i, w] = M[i - 1, w]
            else:
                M[i, w] = max(M[i - 1, w], Items[i - 1][1] + M[i - 1, w - wi])
    print("背包最大Value为:", M[5, 11])
