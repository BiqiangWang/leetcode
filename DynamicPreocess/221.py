from typing import List


def maximalSquare(matrix: List[List[str]]) -> int:
    m, n = len(matrix), len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    def check(x0, y0, line, col):
        if line >= m or col >= n:
            return False
        for a in range(line):
            if a >= x0 and matrix[a][col] == '0':
                return False
        for b in range(col):
            if b >= y0 and matrix[line][b] == '0':
                return False
        if matrix[line][col] == '0':
            return False
        return True

    ans = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                now = 1
                if i > 0 and j > 0 and dp[i - 1][j - 1] > 2:
                    now = dp[i-1][j-1] - 1
                pos_x = i + now
                pos_y = j + now
                while check(i, j, pos_x, pos_y):
                    now += 1
                    pos_x += 1
                    pos_y += 1
                dp[i][j] = now
                ans = max(ans, now)
    print(dp)
    return ans * ans


if __name__ == '__main__':
    z = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    zz = [["1","1","1","1","0"],
          ["1","1","1","1","0"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["0","0","1","1","1"]]
    print(maximalSquare(zz))
