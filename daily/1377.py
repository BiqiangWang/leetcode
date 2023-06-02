from functools import cache
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        used = [0] * (n + 1)  # 标记节点是否被访问过
        matrix = [[0] * (n + 1) for _ in range(n + 1)]
        for edge in edges:
            matrix[edge[0]][edge[1]] = 1
            matrix[edge[1]][edge[0]] = 1

        def f(pos: int, deep: int, use_list: List[int], probability: float):
            ans = 0
            use_list[pos] = 1
            if deep == t:
                return probability if pos == target else 0
            cnt, temp_list = 0, []
            for i in range(n + 1):
                if matrix[pos][i] == 1 and used[i] == 0:
                    cnt += 1
                    temp_list.append(i)
            if not temp_list:
                return probability if pos == target else 0
            for i in temp_list:
                ans += f(i, deep + 1, use_list, probability * (1 / cnt))
            return ans

        return f(1, 0, used, 1)

    """
        优化思路： 1. matrix邻接矩阵其实不需要完整的n * n ，实际上只需要n * 2 的大小，通过这一优化可以将空间复杂度降为 O(n）
                2. 保留精度。在过程中进行除法操作可能会导致精度降低，由于都是分子为1的分数，因此可以先将分母都乘起来，最后取倒数
    """

    def advanced(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        used = [0] * (n + 1)  # 标记节点是否被访问过
        matrix = [[] for _ in range(n + 1)]
        for x, y in edges:
            matrix[x].append(y)
            matrix[y].append(x)

        def f(pos: int, deep: int, use_list: List[int], probability: float):
            ans = 0
            use_list[pos] = 1
            if deep == t:
                return probability if pos == target else 0
            cnt, temp_list = 0, []
            for i in matrix[pos]:
                if used[i] == 0:
                    cnt += 1
                    temp_list.append(i)
            if not temp_list:
                return probability if pos == target else 0
            for i in temp_list:
                ans += f(i, deep + 1, use_list, probability * cnt)
            return ans

        res = f(1, 0, used, 1)
        return 1 / res if res != 0 else 0


if __name__ == '__main__':
    z, x, c, v = 7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 20, 6
    so = Solution()
    print(so.advanced(z, x, c, v))
