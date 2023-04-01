from typing import List


class Solution:

    def solu2(self, nums: List[int]):
        print(set(nums) - {0})

    def quick_sort(self, alist, first, last):
        if first >= last:
            # 如果开始等于结尾，即就一个元素
            return
        mid_value = alist[first]
        low = first
        high = last
        # 对于相等的情况都放到low的位置，所以第一个条件是>=.数据尽量放在一边。
        while low < high:
            # hight开始移动,左移所以-1
            while low < high and alist[high] >= mid_value:
                high -= 1  # high游标左走
            alist[low] = alist[high]  # 把大于mid的值放到low的位置
            # low开始移动
            while low < high and alist[low] < mid_value:
                low += 1
            alist[high] = alist[low]
            # high -= 1  # high游标左走
            # 当low=high时从循环退出
            alist[low] = mid_value
            # 或者
            # alist[high] = mid_value

            # 对low左边的列表排序
            self.quick_sort(alist, first, low - 1)
            # 对low右边的列表排序
            self.quick_sort(alist, low + 1, last)

    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        self.quick_sort(nums, 0, n - 1)
        count = 0
        for i in range(n):
            if nums[i] > 0:
                count += 1
                val = nums[i]
                for k in range(i, n):
                    nums[k] -= val
        return count


if __name__ == '__main__':
    z = [1, 5, 0, 3, 5]
    so = Solution()
    print(so.solu2(z))
