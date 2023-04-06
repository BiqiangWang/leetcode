import math
class Solution:
    def baseNeg2(self, n: int) -> str:
        """
            有误，无法处理 n = 5 的情况

            当

        """
        ind = 0
        count = n
        ans = ''
        while count > 1:
            ind += 1
            count = math.ceil(count / 2)

        if ind % 2 == 1:
            if pow(2, ind) > n:
                start_pos = ind - 1
            else:
                start_pos = ind + 1
        else:
            start_pos = ind

        num = 0
        for index in range(start_pos, -1, -1):
            if index % 2 == 0:
                if num < n:
                    ans += '1'
                    num += pow(2, index)
                else:
                    ans += '0'
            else:
                if num > n:
                    ans += '1'
                    num -= pow(2, index)
                else:
                    ans += '0'

        return ans

    def advanced(self, n: int) -> str:
        k = 1
        ans = []
        while n:
            if n % 2:
                ans.append('1')
                n -= k
            else:
                ans.append('0')
            n //= 2
            k *= -1
        return ''.join(ans[::-1]) or '0'


if __name__ == '__main__':
    z = 2
    so = Solution()
    print(so.advanced(z))
