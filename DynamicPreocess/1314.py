from typing import List


def matrixBlockSum(mat: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    dp = mat.copy()
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + mat[i][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + mat[0][i]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i][j]
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i - k <= 0:
                line_begin = 0
            else:
                line_begin = i - k
            if j - k <= 0:
                col_begin = 0
            else:
                col_begin = j - k
            if i + k >= m:
                line_end = m - 1
            else:
                line_end = i + k
            if j + k >= n:
                col_end = n - 1
            else:
                col_end = j + k
            if line_begin == 0:
                duplicate1 = 0
            else:
                duplicate1 = dp[line_begin - 1][col_end]
            if col_begin == 0:
                duplicate2 = 0
            else:
                duplicate2 = dp[line_end][col_begin - 1]
            if col_begin == 0 or line_begin == 0:
                integrate = 0
            else:
                integrate = dp[line_begin - 1][col_begin - 1]
            ans[i][j] = dp[line_end][col_end] - duplicate1 - duplicate2 + integrate
    print(ans)


if __name__ == '__main__':
    z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    v = 1
    print(matrixBlockSum(z, v))
