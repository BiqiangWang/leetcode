from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
            思路清晰： 先建图 再染色， 但染色过程有误
                问题在于：在遍历过程中对目标点进行染色存在一定的问题，例如无法准确识别出目标顶点染色1号的情况
                        实际上，对于这类染色问题，应当从自身染色出发，一步步迭代进行，具体参见 advanced 函数
        :param n:
        :param paths:
        :return:
        """
        ans = [1] * n
        map = [[] for _ in range(n)]
        for u, v in paths:
            map[u - 1].append(v - 1)
            map[v - 1].append(u - 1)
        for i in range(n):
            for j in range(len(map[i])):
                if map[i][j] > i:
                    ans[map[i][j]] = max(ans[map[i][j]], ans[i] + 1)

        return ans

    def advanced(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)
        color = [0] * n
        for i, nodes in enumerate(g):
            color[i] = (set(range(1, 5)) - {color[j] for j in nodes}).pop()

    def Bitwise(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)
        color = [0] * n
        for i, nodes in enumerate(g):
            mask = 1
            for j in g[i]:
                mask |= 1 << color[j]
            mask = ~mask
            color[i] = (mask & -mask).bit_length() - 1
        return color


if __name__ == '__main__':
    z, c = 4, [[1, 2], [3, 4]]
    print(1 << 0)
    so = Solution()
    print(so.Bitwise(z, c))
