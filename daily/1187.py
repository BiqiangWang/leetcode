from bisect import bisect_left
from functools import cache
from typing import List

from numpy import inf


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dp(i: int, pre: int) -> int:
            if i < 0: return 0
            res = dp(i - 1, arr1[i]) if arr1[i] < pre else inf
            k = bisect_left(arr2, pre) - 1
            if k >= 0:  # 替换
                res = min(res, dp(i - 1, arr2[k]) + 1)
            return res

        ans = dp(len(arr1) - 1, inf)
        return ans if ans < inf else -1
