from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #   timeout  使用了类似冒泡排序的思想
        n = len(nums)
        nums[0] = nums[0] * nums[0]
        for i in range(n):
            new_num = nums[i] * nums[i]
            for k in range(0, i):
                if k == i - 1 and new_num >= nums[k]:
                    nums[i] = new_num
                if new_num < nums[k]:
                    for j in range(i, k - 1, -1):
                        nums[j] = nums[j - 1]
                    nums[k] = new_num
                    break
        return nums

    def advanced(self, nums: List[int]) -> List[int]:
        #  timeout  换用直接插入排序思想，依然不行
        n = len(nums)
        nums[0] = nums[0] * nums[0]
        for i in range(1, n):
            nums[i] = nums[i] * nums[i]
            for k in range(i, 0, -1):
                if nums[k - 1] > nums[k]:
                    nums[k - 1], nums[k] = nums[k], nums[k - 1]
                else:
                    break
        return nums

    def advancedagain(self, nums: List[int]) -> List[int]:
        #  timeout 折半插入排序， 略有提升但依然超时
        n = len(nums)
        nums[0] = nums[0] * nums[0]
        for i in range(1, n):
            temp = nums[i] * nums[i]
            low, high = 0, i - 1
            while low <= high:
                mid = int((high + low) / 2)
                if temp > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            for k in range(i - 1, high, -1):
                nums[k + 1] = nums[k]
            nums[low] = temp
        return nums

    def advancedoncemore(self, nums: List[int]) -> List[int]:
        # success  双指针法，利用了原先的有序性！！
        n = len(nums)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] > nums[j] * nums[j]:
                ans[pos] = nums[i] * nums[i]
                i += 1
            else:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            pos -= 1
        return ans

    def bai(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])


if __name__ == '__main__':
    z = [-4, -1, 0, 3, 10]
    so = Solution()
    print(so.advancedoncemore(z))
