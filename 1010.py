from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = dict()
        for t in time:
            c = t % 60
            if c not in d:
                d.setdefault(c, 1)
            else:
                d[c] += 1
        d = sorted(d.items(), key=lambda x: x[0])
        ans = 0
        l, r = 0, len(d) - 1
        if d[l][0] == 0:
            ans += int(d[l][1] * (d[l][1] - 1) / 2)
            l += 1
        while l < r:
            if d[l][0] + d[r][0] < 60:
                l += 1
            elif d[l][0] + d[r][0] > 60:
                r -= 1
            else:
                if d[l][0] == d[r][0]:
                    ans += int(d[l][1] * (d[l][1] - 1) / 2)
                else:
                    ans += d[l][1] * d[r][1]
                l += 1
                r -= 1
        return ans


if __name__ == '__main__':
    z = time = [30, 20, 150, 100, 40]
    so = Solution()
    print(so.numPairsDivisibleBy60(z))
