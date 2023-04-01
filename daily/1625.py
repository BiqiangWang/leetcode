class Solution:
    def adda(self, s: str, a: int):
        for i, num in enumerate(s):
            if i % 2 == 1:
                pre = s[0:i]
                num = (int(num) + a) % 10
                after = s[i + 1:len(s)]
                s = pre + str(num) + after
        return s

    def move(self, s: str, b: int):
        temp = s[0:b]
        s = s[b: len(s)]
        s += temp
        return s

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        min_str = s
        if b % 2 == 1:
            move_num = len(s)
        else:
            move_num = int(len(s) / 2)
        for i in range(move_num):
            s = self.move(s, b)
            min_str = min(min_str, s)
            for j in range(10):
                s = self.adda(s, a)
                min_str = min(min_str, s)
                for k in range(move_num):
                    s = self.move(s, b)
                    min_str = min(min_str, s)
                    for t in range(10):
                        s = self.adda(s, a)
                        min_str = min(min_str, s)
        return min_str

class Advanced:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        n = len(s)
        s = list(s)
        for _ in range(n):
            s = s[-b:] + s[:-b]
            for j in range(10):
                for k in range(1, n, 2):
                    s[k] = str((int(s[k]) + a) % 10)
                if b % 2 == 1:
                    for p in range(10):
                        for k in range(0, n, 2):
                            s[k] = str((int(s[k]) + a) % 10)
                        t = ''.join(s)
                        if ans > t:
                            ans = t
                else:
                    t = ''.join(s)
                    if ans > t:
                        ans = t
        return ans


if __name__ == '__main__':
    z, v, m = "5525", 9, 2
    so = Advanced()
    print(so.findLexSmallestString(z, v, m))
