from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def f(i: int, j: int):
            if i > j:
                return -1
            mid = int((i + j) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return f(mid + 1, j)
            else:
                return f(i, mid - 1)

        return f(0, len(nums) - 1)

    def advanced(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


if __name__ == '__main__':
    z, v = [-1, 0, 3, 5, 9, 12], 9
    so = Solution()
    print(so.search(z, v))
