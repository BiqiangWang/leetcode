from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = - prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
        dp[i][1] = dp[i - 1][0] + prices[i]
        dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
    return max(dp[n - 1][1], dp[n - 1][2])


if __name__ == '__main__':
    v = [1, 2, 3, 0, 2]
    print(maxProfit(v))
