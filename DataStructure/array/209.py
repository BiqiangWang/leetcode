from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        begin, end, value = 0, 0, nums[0]
        n = len(nums)
        ans = n + 1
        while end < n:
            if value >= target:
                ans = min(ans, end - begin + 1)
                value -= nums[begin]
                begin += 1
            else:
                if end != n - 1:
                    value += nums[end + 1]
                end += 1
        return ans if ans != n + 1 else 0


if __name__ == '__main__':
    z, v = [2, 3, 1, 2, 4, 3], 7
    so = Solution()
    print(so.minSubArrayLen(v, z))
