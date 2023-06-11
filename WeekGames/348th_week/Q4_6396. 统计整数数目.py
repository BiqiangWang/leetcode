import string
from functools import cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7

        def f(s: string):

            @cache
            def dp(i: int, summary: int, is_limit: bool) -> int:
                if summary > max_sum:
                    return 0
                if i == len(s):
                    return summary >= min_sum
                res = 0
                up = int(s[i]) if is_limit else 9
                for k in range(up + 1):
                    res += dp(i + 1, summary + k, is_limit and k == up)
                return res % MOD

            return dp(0, 0, True)

        t = 0
        for c in num1:
            t += int(c)
        ans = f(num2) - f(num1) + (min_sum <= t <= max_sum)
        return ans % MOD

