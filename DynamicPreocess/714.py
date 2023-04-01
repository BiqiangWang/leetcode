from typing import List


def advanced(prices: List[int], fee: int) -> int:
    hold = -prices[0]
    free = 0
    for i in range(1, len(prices)):
        a = hold
        hold = max(hold, free - prices[i])
        free = max(free, a + prices[i] - fee)
    return free


def maxProfit(prices: List[int], fee: int) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = - prices[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee)
    return dp[n - 1][1]


if __name__ == '__main__':
    v, z = [1, 3, 2, 8, 4, 9], 2
    print(maxProfit(v, z))
