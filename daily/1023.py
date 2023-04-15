from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(queries)
        ans = [True] * n
        for i in range(n):
            x, y = 0, 0
            while x < len(queries[i]) and y < len(pattern):
                if queries[i][x] == pattern[y]:
                    x += 1
                    y += 1
                else:
                    if queries[i][x].isupper():
                        ans[i] = False
                        break
                    x += 1
            if y == len(pattern):
                while x < len(queries[i]):
                    if queries[i][x].isupper():
                        ans[i] = False
                        break
                    x += 1
            if x == len(queries[i]) and y < len(pattern):
                ans[i] = False

        return ans


if __name__ == '__main__':
    z, v = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], 'FB'
    so = Solution()
    print(so.camelMatch(z, v))
