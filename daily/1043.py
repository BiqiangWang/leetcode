from functools import cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def f(i: int):
            if n - i == 0:
                return 0
            ans = mx = 0
            for j in range(i, min(n, i + k)):
                mx = max(mx, arr[j])
                ans = max(ans, (j - i + 1) * mx + f(j + 1))
            return ans
        return f(0)


    def ans2(self, arr: List[int], k: int) -> int:
        @cache
        def dfs(i: int):
            ans = mx = 0
            for j in range(i, max(i - k, -1), -1):
                mx = max(mx, arr[j])
                ans = max(ans, dfs(j - 1) + (i - j + 1) * mx)
            return ans

        return dfs(len(arr) - 1)


if __name__ == '__main__':
    z, v = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4
    so = Solution()
    print(so.maxSumAfterPartitioning(z, v))
