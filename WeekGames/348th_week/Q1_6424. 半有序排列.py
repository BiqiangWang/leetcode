from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        l, r = -1, -1
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 1:
                l = i
            elif num == n:
                r = i
        return l + n - 1 - r - 1 if l >= r else l + n-1 - r