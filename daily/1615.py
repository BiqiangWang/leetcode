from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        arr = [[0] * n for _ in range(n)]
        cnt = [0] * n
        for i, j in roads:
            arr[i][j] = arr[j][i] = 1
            cnt[i] += 1
            cnt[j] += 1
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, cnt[i] + cnt[j] - arr[i][j])
        return res


if __name__ == '__main__':
    a = 4
    b = [[0, 1], [0, 3], [1, 2], [1, 3]]
    so = Solution()
    print(so.maximalNetworkRank(a, b))
