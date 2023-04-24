from functools import cache
from typing import List

from numpy import inf


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def dfs(i: int):
            if i == n:
                return 0
            res, left_w, height = inf, shelfWidth, 0
            for k in range(i, n):
                left_w -= books[k][0]
                if left_w < 0:
                    break
                height = max(height, books[k][1])
                res = min(res, dfs(k + 1) + height)

            return res

        return dfs(0)
    