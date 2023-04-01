from collections import defaultdict, Counter
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ds = dict()
        for i in range(len(items1)):
            ds.setdefault(items1[i][0], items1[i][1])
        for i in range(len(items2)):
            if items2[i][0] not in ds:
                ds.setdefault(items2[i][0], items2[i][1])
            else:
                ds[items2[i][0]] += items2[i][1]

        return sorted([a, b] for a, b in ds.items())

    def trydo(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map = Counter()
        for a, b in items1:
            map[a] += b
        for a, b in items2:
            map[a] += b
        print(map, sorted([k, v] for k, v in map.items()))


if __name__ == '__main__':
    z1, z2 = [[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]
    so = Solution()
    so.mergeSimilarItems(z1, z2)
    so.trydo(z1, z2)
