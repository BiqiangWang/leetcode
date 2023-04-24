from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        res = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 对nums[i]去重
            for j in range(i + 3, n):
                if n - 1 > j > i + 2 and nums[j] == nums[j + 1]:
                    continue
                l, r = i + 1, j - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return res

    def fourSum_advanced(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        res = []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 对nums[i]去重
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            for j in range(i + 3, n):
                if j < n - 1 and nums[j] == nums[j + 1]:
                    continue
                if nums[j] + nums[i] + nums[j - 1] + nums[j - 2] < target:
                    continue
                if nums[j] + nums[i + 1] + nums[i + 2] + nums[i] > target:
                    break
                l, r = i + 1, j - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return res


if __name__ == '__main__':
    z = [-1, 2, 2, -5, 0, -1, 4]
    v = 3
    so = Solution()
    print(so.fourSum(z, v))
