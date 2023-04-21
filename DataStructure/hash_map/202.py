class Solution:
    def isHappy(self, n: int) -> bool:
        d = dict()
        while n not in d:
            if n == 1:
                return True
            d[n] = 1
            ne = 0
            while n > 0:
                ne += pow(n % 10, 2)
                n = n // 10
            n = ne

        return False


