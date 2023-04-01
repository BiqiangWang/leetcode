from functools import lru_cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache
        def f(i: int, limit: int) -> int:
            if i == n - 1:
                return 5 - limit
            ans = 0
            for k in range(limit, 5):
                ans += f(i + 1, k)
            return ans

        return f(0, 0)

    def dp(self, n: int) -> int:
        dp = [1] * 5
        for i in range(1, n):
            for j in range(1, 5):
                dp[j] += dp[j-1]

        print(dp)
        return sum(dp)


if __name__ == '__main__':
    z = 3
    so = Solution()
    print(so.dp(z))
