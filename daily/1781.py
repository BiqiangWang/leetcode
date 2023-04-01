from collections import Counter


def dynamicProcess(s):
    ans, n = 0, len(s)
    for i in range(n):
        d = dict()
        cnt = Counter()
        for j in range(i, n):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d.setdefault(s[j], 1)
            ans += max(d.values()) - min(d.values())
    return ans


def beautySum(s: str) -> int:
    n = len(s)

    def beauty(st: str):
        if len(st) < 3:
            return 0
        d = dict()
        for char in st:
            if char not in d:
                d.setdefault(char, 1)
            else:
                d[char] += 1
        values = d.values()
        large = max(values)
        small = min(values)
        print(st, large, small)
        return large - small

    ans = 0
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            ans += beauty(s[i:j])
    return ans


if __name__ == '__main__':
    z = "aabcb"
    print(beautySum(z))
