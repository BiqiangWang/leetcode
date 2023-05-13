from cmath import inf
from itertools import pairwise
from typing import List


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base, d = 0, 0
        mx, mn = -inf, inf
        for a, b in pairwise(nums):
            base += abs(a - b)
            mx = max(min(a, b), mx)
            mn = min(max(a, b), mn)
            d = max(d, abs(nums[0] - b) - abs(a - b), abs(nums[-1] - a) - abs(a - b))
        return base + max(d, 2 * (mx - mn))
