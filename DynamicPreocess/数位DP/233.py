from functools import lru_cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)

        """
            计数： n 以内 1 出现的个数
        """

        @lru_cache
        def f(i: int, cnt1: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return cnt1
            res = 0
            if not is_num:
                res += f(i + 1, cnt1, False, False)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                res += f(i + 1, cnt1 + (d == 1), is_limit and d == up, True)
            return res

        return f(0, 0, True, False)


if __name__ == '__main__':
    z = 13
    so = Solution()
    print(so.countDigitOne(z))
