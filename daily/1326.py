from typing import List

# 问题描述：
#   n 表示需要灌溉土地的数目
#   ranges 表示每一个水龙头能够灌溉的范围
#
#   返回可以灌溉整个花园的 最少水龙头数目

# 解决思路：
#   1. 贪心
#   首先对所有的灌溉子区间进行预处理，记录以其为左端点的子区间中最远的右端点，记为 rightMost[i]
#   然后枚举每一个位置，假设当枚举到位置i时，记左端点不大于i的所有子区间的最远右端点为last。
#   此外还需要记录前一个子区间所结束的位置pre，在当前子区间枚举结束（即i==pre)时，标记区间数num+=1，并更新pre的值
#       在枚举过程中不断更新last
#
#   最后返回num
#


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rightMost = list(range(n + 1))
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            rightMost[start] = max(rightMost[start], end)

        last, pre, res = 0, 0, 0  # pre 用于记录上一个使用区间结束的位置
        for i in range(n):
            last = max(last, rightMost[i])
            if i == last:
                return -1
            if i == pre:
                res += 1
                pre = last
        return res


if __name__ == '__main__':
    z, v = 9, [0, 5, 0, 3, 3, 3, 1, 4, 0, 4]
    so = Solution()
    print(so.minTaps(z, v))
