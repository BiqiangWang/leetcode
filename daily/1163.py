from functools import cache


class Solution:

    def lastSubstring(self, s: str) -> str:
        """
            用递归复杂度太高
        :param s:
        :return:
        """

        @cache
        def dfs(i: int) -> str:
            if i == len(s):
                return ''
            res = ''
            for j in range(i, len(s)):
                substr = s[i: j + 1]
                res = max(res, substr, dfs(j + 1))
            return res

        return dfs(0)

    def advanced(self, s: str) -> str:
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] > s[j + k]:
                j += k + 1
                k = 0
            else:
                i += k + 1
                k = 0
                if i >= j:
                    j = i + 1

        return s[i:]
