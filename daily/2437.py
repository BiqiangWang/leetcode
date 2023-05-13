class Solution:
    def countTime(self, time: str) -> int:
        m1 = 6 if time[3] == '?' else 1
        m2 = 10 if time[4] == '?' else 1
        res2 = m1 * m2

        res1 = 0
        a, b = time[0], time[1]
        if a == '?' and b == '?':
            res1 = 24
        elif a != '?' and b == '?':
            if 0 <= int(a) <= 1:
                res1 = 10
            else:
                res1 = 4
        elif a != '?' and b != '?':
            res1 = 1
        else:
            if int(b) >= 4:
                res1 = 2
            else:
                res1 = 3

        return res1 * res2


    def advanced(self, time: str) -> int:
        def f(s: str, m: int):
            cnt = 0
            for i in range(m):
                a = s[0] == '?' or (int(s[0]) == i // 10)
                b = s[1] == '?' or (int(s[1]) == i % 10)
                cnt += a and b
            return cnt

        return f(time[0:2], 24) * f(time[3:5], 60)

