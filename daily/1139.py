from typing import List


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    max_d = min(m, n)
    for d in range(max_d, 0, -1):
        for i in range(0, m - d + 1):
            for j in range(0, n - d + 1):
                k = 0
                while k < d:
                    if grid[i + k][j] == 0 or grid[i][j + k] == 0 or grid[i + d - 1 - k][j + d - 1] == 0 or \
                            grid[i + d - 1][j + d - 1 - k] == 0:
                        break
                    k += 1
                if k == d:
                    return d * d
    return 0


if __name__ == '__main__':
    z = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(largest1BorderedSquare(z))
