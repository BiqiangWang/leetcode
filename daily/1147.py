class Solution:
    def longestDecomposition(self, text: str) -> int:
        if text == "":
            return 0
        for i in range(len(text) // 2 + 1):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:-i])
        return 1


if __name__ == '__main__':
    z = "ghiabcdefhelloadamhelloabcdefghi"
    so = Solution()
    print(so.longestDecomposition(z))