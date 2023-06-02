from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(x: int):  # 检查数组能否满足x甜蜜度
            cnt, pre = 0, -x
            for cur in price:
                if cur - pre >= x:
                    pre = cur
                    cnt += 1
            return cnt >= k

        price.sort()
        l, r = 0, price[-1] - price[0]
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l

