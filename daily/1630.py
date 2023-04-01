from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ans = [False] * n
        for i in range(n):
            sub = nums[l[i]:r[i] + 1]
            sub = sorted(sub)
            print(sub)

            def f(arr: List[int]) -> bool:
                m = len(arr)
                if m < 2:
                    return False
                elif m == 2:
                    return True
                for k in range(2, m):
                    if arr[k - 1] - arr[k - 2] != arr[k] - arr[k - 1]:
                        return False
                return True

            if f(sub):
                ans[i] = True

        return ans


if __name__ == '__main__':
    z, v, p = [4, 6, 5, 9, 3, 7], [0, 0, 2], [2, 3, 5]
    so = Solution()
    print(so.checkArithmeticSubarrays(z, v, p))
