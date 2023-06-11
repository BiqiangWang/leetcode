from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        record = []
        for i in range(n):
            a = '-'.join(str(k) for k in grid[i][0:n])
            record.append(a)
        cnt = Counter(record)
        c = []
        for j in range(n):
            c.append([grid[0][j]])
        for j in range(n):
            for i in range(1, n):
                c[j].append(grid[i][j])
        ans = 0
        for arr in c:
            a = '-'.join(str(k) for k in arr)
            if a in cnt:
                ans += cnt[a]
        return ans

    
