from typing import List


def advanced(matrix: List[List[int]]) -> int:
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    dp = matrix[0].copy()
    ans = float('inf')
    for i in range(1, n):
        new_dp = [0] * n
        for j in range(0, n):
            if j == 0:
                new_dp[j] = matrix[i][j] + min(dp[j], dp[j + 1])
                if i == n-1:
                    ans = min(ans, new_dp[j])
            elif j == n - 1:
                new_dp[j] = matrix[i][j] + min(dp[j], dp[j - 1])
                if i == n-1:
                    ans = min(ans, new_dp[j])
            else:
                new_dp[j] = matrix[i][j] + min(dp[j], dp[j - 1], dp[j + 1])
                if i == n-1:
                    ans = min(ans, new_dp[j])
        dp = new_dp
    return ans


def minFallingPathSum(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    if m == 1:
        return matrix[0][0]
    dp = [[0] * n for _ in range(m)]
    ans = float('inf')
    for i in range(n):
        dp[0][i] = matrix[0][i]
    for i in range(1, m):
        for j in range(0, n):
            if j == 0:
                dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                if i == m-1:
                    ans = min(ans, dp[i][j])
            elif j == n - 1:
                dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
                if i == m-1:
                    ans = min(ans, dp[i][j])
            else:
                dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])
                if i == m-1:
                    ans = min(ans, dp[i][j])
            print(dp)
    return ans


if __name__ == '__main__':
    z = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    # z = [[-1]]
    arr = [1, 2]
    for i, char in enumerate(arr):
        print("haha")
    print(advanced(z))
