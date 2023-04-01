from typing import List


def advanced(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    d = dict()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0 and not (i, j) in d:
                for k1 in range(m):
                    if matrix[k1][j] != 0:
                        matrix[k1][j] = 0
                        d.setdefault((k1, j), 1)
                for k2 in range(n):
                    if matrix[i][k2] != 0:
                        matrix[i][k2] = 0
                        d.setdefault((i, k2), 1)
    print(matrix)


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    flag = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0 and flag[i][j] == 0:
                for k1 in range(m):
                    if matrix[k1][j] != 0:
                        matrix[k1][j] = 0
                        flag[k1][j] = 1
                for k2 in range(n):
                    if matrix[i][k2] != 0:
                        matrix[i][k2] = 0
                        flag[i][k2] = 1
    print(matrix)


if __name__ == '__main__':
    z = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    advanced(z)
