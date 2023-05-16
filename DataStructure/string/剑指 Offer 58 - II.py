class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s = list(s)
        s[:n] = list(reversed(s[:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        return ''.join(s)
    