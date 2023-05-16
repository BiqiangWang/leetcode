from typing import List


class Solution:
    def get_next(self, s: str) -> List[int]:
        n = len(s)
        ne = [0] * n
        j, k = 0, -1
        ne[0] = -1
        while j < n - 1:
            if k == -1 or s[k] == s[j]:
                k += 1
                j += 1
                ne[j] = k
            else:
                k = ne[k]
        return ne

    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        ne = self.get_next(needle)
        i, j = 0, 0
        while i < n:
            if haystack[i] != needle[j]:
                j = ne[j]
                if j == -1:
                    j = 0
                    i += 1
            else:
                j += 1
                i += 1
                if j == m:
                    return i - j
        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        b = len(haystack)
        if a == 0:
            return 0
        next = self.getnext(a, needle)
        p = -1
        for j in range(b):
            while p >= 0 and needle[p + 1] != haystack[j]:
                p = next[p]
            if needle[p + 1] == haystack[j]:
                p += 1
            if p == a - 1:
                return j - a + 1
        return -1

    def getnext(self, a, needle):
        next = ['' for i in range(a)]
        k = -1
        next[0] = k
        for i in range(1, len(needle)):
            while (k > -1 and needle[k + 1] != needle[i]):
                k = next[k]
            if needle[k + 1] == needle[i]:
                k += 1
            next[i] = k
        return next


if __name__ == '__main__':
    z, x = "mississippi", "issip"
    so = Solution()
    print(so.strStr(z, x))
