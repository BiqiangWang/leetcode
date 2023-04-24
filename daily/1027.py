from functools import cache
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        @cache
        def dfs(i: int):
            max_len = {}
            for j in range(i - 1, -1, -1):
                d = nums[i] - nums[j]
                if d not in max_len:
                    max_len[d] = dfs(j).get(d, 1) + 1  # get方法特殊用法，第二个参数表示不存在时的默认值
            return max_len

        return max(max(dfs(i).values()) for i in range(1, len(nums)))
