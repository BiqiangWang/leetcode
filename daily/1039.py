from functools import lru_cache
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:
                return 0
            return min(dfs(i, k) + dfs(k, j) + values[i] * values[j] * values[k] for k in range(i + 1, j))

        return dfs(0, len(values) - 1)


if __name__ == '__main__':
    z = values = [3, 7, 4, 5]
    so = Solution()
    print(so.minScoreTriangulation(z))
