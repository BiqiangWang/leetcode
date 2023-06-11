from bisect import bisect
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str):
            c = ord('z') + 1
            cnt = 0
            for char in s:
                if ord(char) < c:
                    cnt = 1
                    c = ord(char)
                elif ord(char) == c:
                    cnt += 1
            return cnt

        arr = []
        for w in words:
            arr.append(f(w))
        n = len(arr)
        arr.sort()

        ans = []
        for q in queries:
            pos = bisect.bisect(arr, f(q))
            ans.append(n - pos)

        return ans





