from functools import cache
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g = [[] for _ in range(n)]
        for j, m in enumerate(manager):
            if m >= 0:
                g[m].append(j)  # 建树

        @cache
        def dfs(i: int, value: int):
            if informTime[i] == 0:
                return value
            ans = 0
            print(g[i])
            for k in g[i]:
                ans = max(ans, dfs(k, value + informTime[i]))
            return ans

        return dfs(headID, 0)


if __name__ == '__main__':
    z, x, c, v = 7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]
    so = Solution()
    print(so.numOfMinutes(z, x, c, v))
