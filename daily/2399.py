from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = dict()
        for i, char in enumerate(s):
            if char not in d:
                d.setdefault(char, i)
            else:
                if i - d[char] - 1 != distance[ord(char) - ord("a")]:
                    return False
        return True


if __name__ == '__main__':
    z, v = 'abaccb', [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    so = Solution()
    print(so.checkDistances(z, v))
