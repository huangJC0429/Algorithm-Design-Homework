import math
import matplotlib.pyplot as plt


class CP:
    def init_sort(self, P, n):
        X = list(P)
        Y = list(P)
        #  根据横坐标排序
        X.sort()
        Y = sorted(Y, key=lambda last: last[-1])
        return X, Y, n

    def closest_pair(self, X, Y, n):
        if n <= 3:
            return CP().brute_force(X, n)
        mid = n // 2
        Y_left = []
        Y_right = []
        for p in Y:
            if p in X[:mid]:
                Y_left.append(p)
            else:
                Y_right.append(p)
        dis_left = CP().closest_pair(X[:mid], Y_left, mid)
        dis_right = CP().closest_pair(X[mid:], Y_right, n - mid)
        min_dis = min(dis_left, dis_right)
        strip = []
        for (x, y) in Y:
            if abs(x - X[mid][0]) < min_dis:
                strip.append((x, y))
        #  检查最近的6个
        min_d = min_dis
        for i, (x, y) in enumerate(strip):
            for j in range(i + 1, 6):
                if i + j < len(strip):
                    temdis = CP().compute_distance(strip[i], strip[j])
                    if temdis < min_d:
                        min_d = temdis
        return min(min_dis, min_d)

    def brute_force(self, X, n):
        min_d = CP().compute_distance(X[0], X[1])
        for i, (x, y) in enumerate(X):
            for j in range(i + 1, n):
                if CP().compute_distance(X[i], X[j]) < min_d:
                    min_d = CP().compute_distance(X[i], X[j])
        return min_d

    def compute_distance(self, a, b):
        return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))


if __name__ == "__main__":
    data = [(8, 48), (10, 3), (14, 27), (9, 25),
              (12, 13), (8, 19), (12, 30), (25, 30),
              (9, 12), (13, 10), (9, 9), (15, 6),
              (22, 32), (5, 32), (23, 9), (19, 25),
              (14, 1), (11, 25), (26, 26), (12, 19),
              (18, 9), (27, 13), (32, 13), (15, 16)]

    for i in data:
        plt.scatter(i[0], i[1])
    plt.show()
    X, Y, n = CP().init_sort(data, len(data))
    print("最近点对距离为:", CP().closest_pair(X, Y, n))
