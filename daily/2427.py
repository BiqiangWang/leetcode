class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b:
            temp = a
            a = b
            b = temp
        while a % b != 0:
            temp = b
            b = a % b
            a = temp
        value = b  # 最大公约数
        ans = 0
        for i in range(1, value + 1):
            if value % i == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    z, v = 12, 6
    so = Solution()
    print(so.commonFactors(z, v))
