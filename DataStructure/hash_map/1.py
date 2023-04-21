from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if num not in d:
                d[target - num] = i
            else:
                return [d[num], i]
