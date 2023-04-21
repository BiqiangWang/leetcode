from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cnt = [0] * n
        for start, end in trips:
            def dfs(x: int, fa: int):
                if x == end:
                    cnt[x] += 1
                    return True
                for y in g[x]:
                    if y != fa and dfs(y, x):
                        cnt[x] += 1
                        return True
                return False

            dfs(start, -1)

        def dfs(x: int, fa: int):
            not_halve = price[x] * cnt[x]
            halve = not_halve // 2
            for y in g[x]:
                if y != fa:
                    nh, h = dfs(y, x)
                    not_halve += min(nh, h)
                    halve += nh
            return not_halve, halve

        return min(dfs(0, -1))





