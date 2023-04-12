from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        c1 = stones[-2] - stones[0] - n + 2
        c2 = stones[-1] = stones[1] - n + 2
        max_move = max(c1, c2)
        if c1 == 0 or c2 == 0:
            return [min(max_move, 2), max_move]
        max_cnt = left = 0
        for right, sr in enumerate(stones):  # 滑动窗口， 遍历右端点所在的石子
            while sr - stones[left] + 1 > n:   # 窗口大小 大于 n
                left += 1
            max_cnt = max(max_cnt, right - left + 1)
        return [n - max_cnt, max_move]




if __name__ == '__main__':
    z = [7,4,9]
    so = Solution()
    print(so.numMovesStonesII(z))