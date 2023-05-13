from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict()
        n = len(names)
        for i in range(n):
            d[heights[i]] = names[i]
        s = sorted(d.items(), key=lambda item: item[0], reverse=True)
        res = []
        for item in s:
            res.append(item[1])
        return res


    def advanced(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]