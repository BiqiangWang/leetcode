class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i, char in enumerate(s):
            if char == ' ':
                s[i] = '%20'
        ans = ''.join(s)
        return ans


if __name__ == '__main__':
    z = "We are happy."
    so = Solution()
    print(so.replaceSpace(z))
