from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len((grid[0]))
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = grid[i][0] + dp[i - 1][0]
    for i in range(1, n):
        dp[0][i] = grid[0][i] + dp[0][i - 1]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # mt = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    mt = [[1]]
    print(minPathSum(mt))
