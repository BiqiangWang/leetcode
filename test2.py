class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        flag, count, pos = -1, 0, 0
        ans = 0
        while pos < n:
            check = ord(word[pos]) - ord('a')
            if check > flag:
                count += 1
                flag = check
            elif check <= flag:
                ans += (3 - count)
                count = 1
                flag = check
            pos += 1
        if count > 0:
            ans += (3 - count)
        return ans


if __name__ == '__main__':
    z = 'aaa'
    so = Solution()
    print(so.addMinimum(z))
