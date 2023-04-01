from typing import List


def __init__(self, matrix: List[List[int]]):
    m, n = len(matrix), (len(matrix[0]) if matrix else 0)
    self.sums = [[0] * (n + 1) for _ in range(m)]
    _sums = self.sums

    for i in range(m):
        for j in range(n):
            _sums[i][j + 1] = _sums[i][j] + matrix[i][j]


def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    _sums = self.sums
    total = sum(_sums[i][col2 + 1] - _sums[i][col1] for i in range(row1, row2 + 1))
    return total


if __name__ == '__main__':
    z = ["NumMatrix","sumRegion","sumRegion","sumRegion"]
    v = [[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
    __init__(v[0][0])


