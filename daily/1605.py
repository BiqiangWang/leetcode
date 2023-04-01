from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        arr = [[0] * n for _ in range(m)]
        i, j = 0, 0
        while i < m and j < n:
            arr[i][j] = min(rowSum[i], colSum[j])
            if rowSum[i] < colSum[j]:
                colSum[j] -= rowSum[i]
                i += 1
            else:
                rowSum[i] -= colSum[j]
                j += 1
        return arr


if __name__ == '__main__':
    a, b = [3, 8], [4, 7]
    so = Solution()
    print(so.restoreMatrix(a, b))
