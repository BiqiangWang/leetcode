from functools import lru_cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == "": return str2
        if str2 == "": return str1
        if str1[-1] == str2[-1]:
            return self.shortestCommonSupersequence(str1[:-1], str2[:-1]) + str1[-1]
        ans1 = self.shortestCommonSupersequence(str1[:-1], str2)
        ans2 = self.shortestCommonSupersequence(str1, str2[:-1])
        if len(ans1) < len(ans2):
            return ans1 + str1[-1]
        return ans2 + str2[-1]

    def advancedonce(self, str1: str, str2: str) -> str:

        @lru_cache
        def f(i: int, j: int) -> str:
            if i < 0: return str2[:j + 1]
            if j < 0: return str1[:i + 1]
            if str1[i] == str2[j]:
                return f(i - 1, j - 1) + str1[i]
            ans1 = f(i - 1, j)
            ans2 = f(i, j - 1)
            if len(ans1) < len(ans2):
                return ans1 + str1[i]
            return ans2 + str2[j]

        return f(len(str1) - 1, len(str2) - 1)

    def advancedOnceAgain(self, str1: str, str2: str) -> str:

        @lru_cache
        def f(i: int, j: int) -> int:
            if i < 0: return j + 1
            if j < 0: return i + 1
            if str1[i] == str2[j]:
                return f(i - 1, j - 1) + 1
            return min(f(i - 1, j), f(i, j - 1)) + 1

        def make_ans(i: int, j: int) -> str:
            if i < 0: return str2[:j + 1]
            if j < 0: return str1[:i + 1]
            if str1[i] == str2[j]:
                return make_ans(i - 1, j - 1) + str1[i]
            if f(i, j) == f(i - 1, j) + 1:
                return make_ans(i - 1, j) + str1[i]
            return make_ans(i, j - 1) + str2[j]

        return make_ans(len(str1) - 1, len(str2) - 1)


if __name__ == '__main__':
    z, v = 'abcd', 'cab'
    so = Solution()
    print(so.advancedOnceAgain(z, v))
