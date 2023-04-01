class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        arr_1, arr_2 = list(s), list(t)
        len1, len2 = len(arr_1), len(arr_2)
        ans = 0
        for i in range(len1):
            for j in range(len2):
                flag, val = 0, 0
                x, y = i, j
                while flag < 2 and x + val < len1 and y + val < len2:
                    if arr_1[x + val] != arr_2[y + val]:
                        flag += 1
                    val += 1
                    if flag == 1:
                        ans += 1
        return ans

    def advanced(self, s: str, t: str) -> int:
        ans, n, m = 0, len(s), len(t)
        for d in range(1 - m, n):  # d=i-j, j=i-d
            i = max(d, 0)
            k0 = k1 = i - 1  # k0为上上一个不同， k1为上一个不同
            while i < n and i - d < m:
                if s[i] != t[i - d]:
                    k0 = k1
                    k1 = i
                ans += k1 - k0
                i += 1
        return ans


if __name__ == '__main__':
    z, v = "ab", "bb"
    so = Solution()
    print(so.advanced(z, v))
