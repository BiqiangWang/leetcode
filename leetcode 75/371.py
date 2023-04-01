class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = bin(a), bin(b)
        print(len(x), len(y))


if __name__ == '__main__':
    z, v = 1, 2
    so = Solution()
    so.getSum(z, v)