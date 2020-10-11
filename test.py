import numpy as np

a = np.random.randint(0, 3, 3).tolist()
print(a)

b = np.arange(0, 3)
print(b)
np.random.shuffle(b)
b = b.tolist()
print(b)

l = [1, 3, 6, 8]
print(l.index(5))