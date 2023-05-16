class Solution:
    def get_next(self, s: str) -> List[int]:
        n = len(s)
        j, k = 0, -1
        ne = [0] * (n + 1)
        ne[0] = k
        while j < n:
            if k == -1 or s[k] == s[j]:
                k += 1
                j += 1
                ne[j] = k
            else:
                k = ne[k]
        return ne

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False
        ne = self.get_next(s)
        print(ne)
        if ne[-1] != 0 and n % (n - ne[-1]) == 0:
            return True
        return False

    def f1(self, s: str) -> bool:
        ss = s + s
        return True if s in ss[1:len(ss) - 1] else False

    def f2(self, s: str) -> bool:
        return s in (s + s)[1:-1]
