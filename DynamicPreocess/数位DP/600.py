from functools import lru_cache


class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n))[2:]

        """
            数位dp
            转换为二进制不存在连续 1 的个数
        """

        @lru_cache
        def f(i: int, pre1: bool, is_limit: bool) -> int:
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            res = f(i + 1, False, is_limit and up == 0)  # 当前位填0
            if not pre1 and up == 1:
                res += f(i + 1, True, is_limit)
            return res

        return f(0, False, True)


if __name__ == '__main__':
    z = 4
    so = Solution()
    print(so.findIntegers(z))
