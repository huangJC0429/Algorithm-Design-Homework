coins = [1, 2, 5]
amount = 11

#  本题类似背包问题，用相同的DP方法可解
f = [float('inf')] * (amount + 1)
f[0] = 0
for c in coins:
    for j in range(c, amount + 1):
        f[j] = min(f[j], f[j - c] + 1)
print(f[amount] if f[amount] != float('inf') else -1)

