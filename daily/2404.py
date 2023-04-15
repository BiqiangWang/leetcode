from collections import Counter
from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = dict()
        max_count, ans = 0, -1
        for num in nums:
            if num % 2 == 0:
                if num not in d:
                    d.setdefault(num, 1)
                else:
                    d[num] += 1
                if d[num] > max_count:
                    ans = num
                    max_count = d[num]
                elif d[num] == max_count:
                    ans = min(ans, num)
        return ans

    def advanced(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_count, ans = 0, -1
        for num in c.keys():
            if not num % 2:
                if c[num] > max_count:
                    ans = num
                    max_count = c[num]
                elif c[num] == max_count and num < ans:
                    ans = num
        return ans



if __name__ == '__main__':
    z = [0, 1, 2, 2, 4, 4, 1]
    so = Solution()
    print(so.advanced(z))
