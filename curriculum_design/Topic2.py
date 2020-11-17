coins = [1, 2, 5]
amount = 11

#  本题类似背包问题，用相同的DP方法可解
def fun(coins, m):
    f = [float('inf')] * (m + 1)
    f[0] = 0
    for c in coins:
        for j in range(c, m + 1):
            f[j] = min(f[j], f[j - c] + 1)
            print(f[j])
        print("----------------")
    return f[m] if f[m] != float('inf') else -1


if __name__ == '__main__':
    print(fun(coins, amount))
