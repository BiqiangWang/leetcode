from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        a, b = set(), set()
        ans = -1
        for num in nums:
            if num > 0:
                if -num in a:
                    a.discard(-num)
                    ans = max(ans, num)
                else:
                    b.add(num)
            else:
                if -num in b:
                    b.discard(-num)
                    ans = max(ans, -num)
                else:
                    a.add(num)
        return ans