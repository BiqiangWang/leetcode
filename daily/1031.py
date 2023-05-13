from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        start, end = 0, firstLen
        res = 0
        while end < len(nums) + 1:
            arr1 = nums[start:end]
            sum1 = sum(arr1)
            for l in range(secondLen, start):
                arr2 = nums[l - secondLen:l]
                res = max(res, sum1 + sum(arr2))
            for l in range(end, len(nums) - secondLen + 1):
                arr2 = nums[l: l + secondLen]
                res = max(res, sum1 + sum(arr2))
            start += 1
            end += 1
        return res


if __name__ == '__main__':
    z = [12, 8, 12, 18, 19, 10, 17, 20, 6, 8, 13, 1, 19, 11, 5]
    x, c = 3, 6
    so = Solution()
    print(so.maxSumTwoNoOverlap(z, x, c))
