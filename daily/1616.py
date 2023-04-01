from math import inf


class Solution:
    def isPalindrome(self, s):
        n = len(s)
        i, j = 0, n - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        for i in range(n):
            str1 = a[0:i] + b[i:n]
            str2 = b[0:i] + a[i:n]
            if self.isPalindrome(str1) or self.isPalindrome(str2):
                return True
        return False


class Advanced:
    def check(self, str_l, str_r, left, right):
        while left >= 0 and right < len(str_l):
            if str_l[left] == str_r[right]:
                left -= 1
                right += 1
            else:
                break
        return left, right

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        i, j = int((n - 1) / 2), int(n / 2)
        i, j = min(self.check(a, a, i, j), self.check(b, b, i, j))
        i, j = min(self.check(a, b, i, j), self.check(b, a, i, j))
        return i == -1


if __name__ == '__main__':
    z, v = "ulacfd", "jizalu"
    so = Advanced()
    print(so.checkPalindromeFormation(z, v))
