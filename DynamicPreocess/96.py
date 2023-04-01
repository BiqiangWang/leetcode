def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1], dp[0] = 1, 1
    print(dp)
    for i in range(2, n + 1):
        for a in range(0, i):
            dp[i] += dp[a] * dp[i - a - 1]
    print(dp)
    return dp[n]


if __name__ == '__main__':
    z = 3
    print(numTrees(z))
