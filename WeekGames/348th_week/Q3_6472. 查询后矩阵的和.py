from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        check_raw = [False] * n
        check_col = [False] * n
        empty, total, ans = n, 0, 0
        for t, i, v in queries[::-1]:
            if t == 1:
                if check_col[i]:
                    continue
                check_col[i] = True
                empty -= 1
                total += v
            else:
                if check_raw[i]:
                    continue
                check_raw[i] = True
                ans += v * empty + total
        for i in range(n):
            if not check_raw[i]:
                ans += total
        return ans

