from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        for i in nums1:
            if i not in d1:
                d1.setdefault(i, 1)
            else:
                d1[i] += 1
        ans = []
        for i in nums2:
            if i in d1 and i not in ans:
                ans.append(i)
        return ans