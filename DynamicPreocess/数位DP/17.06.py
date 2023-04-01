from functools import lru_cache


class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s = str(n)

        """
            数位dp:
            计数 ： n 以内 2 出现的个数
        """

        @lru_cache
        def f(i: int, cnt2: int, is_limit: bool, is_num) -> int:
            if i == len(s):
                return cnt2
            res = 0
            if not is_num:
                res += f(i + 1, cnt2, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                res += f(i + 1, cnt2 + (d == 2), is_limit and d == int(s[i]), True)
            return res

        return f(0, 0, True, False)


if __name__ == '__main__':
    z = 25
    so = Solution()
    print(so.numberOf2sInRange(z))
