import numpy as np

R = np.array([["成都", "巴西利亚"],
              ["普利茅斯", "乌斯怀亚"],
              ["巴西利亚", "普利茅斯"],
              ["大溪地", "乌斯怀亚"]])

# print(list(filter(lambda x: x not in list(set(R[:, 0])), list(set(list(set(R[:, 1])) + (list(set(R[:, 0]))))))))
print(list(set(list(set(R[:, 1]))).difference(set(list(set(R[:, 0]))))))
