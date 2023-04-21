from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = dict()
        for i in nums1:
            for j in nums2:
                if i + j not in d:
                    d.setdefault(i + j, 1)
                else:
                    d[i + j] += 1
        ans = 0
        for i in nums3:
            for j in nums4:
                if -i - j in d:
                    ans += d[-i - j]
        return ans


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    so = Solution()
    print(so.fourSumCount(nums1, nums2, nums3, nums4))