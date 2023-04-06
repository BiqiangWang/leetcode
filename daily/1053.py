from typing import List


class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i == 0:
                break
            if arr[i - 1] > arr[i]:
                for j in range(n - 1, i - 1, -1):
                    if arr[i - 1] > arr[j] != arr[j - 1]:
                        t = arr[i - 1]
                        arr[i - 1] = arr[j]
                        arr[j] = t
                        return arr
        return arr


if __name__ == '__main__':
    z = [1, 9, 4, 8, 6, 7, 7, 7, 9, 10]
    c = [1, 1, 5]
    so = Solution()
    print(so.prevPermOpt1(c))
