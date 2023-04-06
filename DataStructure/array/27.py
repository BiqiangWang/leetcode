from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1

        return count


if __name__ == '__main__':
    z, v = [4, 5, 5], 5
    so = Solution()
    print(so.removeElement(z, v))
