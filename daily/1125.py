from functools import lru_cache
from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sid = {s: i for i, s in enumerate(req_skills)}
        n = len(people)
        mask = [0] * n
        for i, skills in enumerate(people):
            for s in skills:
                mask[i] |= 1 << sid[s]  # 位运算

        # dfs(i,j) 表示从前 i 个集合中选择一些集合，并集等于 j，需要选择的最小集合
        @lru_cache
        def dfs(i: int, j: int) -> int:
            if j == 0:
                return 0  # 背包已装满
            if i < 0:
                return (1 << n) - 1  # 无法装满背包，返回全集
            res = dfs(i - 1, j)
            res2 = dfs(i - 1, j & ~mask[i]) | (1 << i)
            return res if res.bit_count() < res2.bit_count() else res2  # python 3.10 新特性： bit_count() 用于计算对应二进制数中1的个数

        res = dfs(n - 1, (1 << len(req_skills)) - 1)
        return [i for i in range(n) if (res >> i) & 1]  # 所有在 res 中的下标


if __name__ == '__main__':
    z, v = ["java", "nodejs", "reactjs"], [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    so = Solution()
    print(so.smallestSufficientTeam(z, v))
