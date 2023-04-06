from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:

    def mergeStones(self, stones: List[int], k: int) -> int:
        """
            这种方法应该是最容易想到的思路，但实际上，由于并未考虑全局性，会存在局部最优的问题
            错误示例： [6, 4, 4, 6]
        """

        n = len(stones)
        if n == 1:
            return stones[0]
        if n % (k - 1) != 1 and k != 2:
            return -1

        cost = 0
        while len(stones) > 1:
            pos, min_weight = 0, 0
            for i in range(k):
                min_weight += stones[i]
            for i in range(1, len(stones) - k + 1):
                cur = 0
                for j in range(k):
                    cur += stones[i + j]
                if cur < min_weight:
                    min_weight = cur
                    pos = i
            print(stones, min_weight, pos)
            for i in range(pos + 1, len(stones) - k + 1):
                stones[i] = stones[i + k - 1]
            stones[pos] = min_weight
            cost += min_weight
            stones = stones[0: len(stones) - k + 1]

        return cost

    def advanced(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + stones[i - 1]
        # s = list(accumulate(stones, initial=0))
        @lru_cache
        def dfs(i: int, j: int, p: int) -> int:
            if p == 1:
                if i == j:
                    return 0
                else:
                    return dfs(i, j, k) + s[j + 1] - s[i]
            return min(dfs(i, m, 1) + dfs(m + 1, j, p - 1) for m in range(i, j, k - 1))

        return dfs(0, n - 1, 1)


if __name__ == '__main__':
    z, v = [3, 2, 4, 1], 2
    so = Solution()
    print(so.advanced(z, v))
