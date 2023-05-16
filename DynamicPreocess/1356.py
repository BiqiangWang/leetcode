from cmath import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1

        @cache
        def dfs(i: int, j: int):  # 表示用i + 1天完成0~j项工作
            if i == 0:
                return max(jobDifficulty[:j + 1])

            res, mx = inf, 0
            for k in range(j, i - 1, -1):
                mx = max(mx, jobDifficulty[k])  # 记录当天最大难度
                res = min(res, mx + dfs(i - 1, k - 1))

            return res

        return dfs(d - 1, n - 1)

