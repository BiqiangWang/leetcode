from typing import List


def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if obstacleGrid[i][0] != 1:
            dp[i][0] = 1
        else:
            break
    for i in range(n):
        if obstacleGrid[0][i] != 1:
            dp[0][i] = 1
        else:
            break
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp)
    return dp[m - 1][n - 1]


if __name__ == '__main__':
    # t = [[0,0,0],[0,1,0],[0,0,0]]
    t = [[0,1],[0,0]]
    print(uniquePathsWithObstacles(t))
