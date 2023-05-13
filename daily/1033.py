from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        d = [a, b, c]
        d.sort()
        min_pos = d[0]
        mid = d[1]
        max_pos = d[2]

        min_res = 0
        max_res = 0
        if mid - min_pos > 1:
            max_res += mid - min_pos - 1
        if max_pos - mid > 1:
            max_res += max_pos - mid - 1

        if mid - min_pos > 1 and max_pos - mid > 1:
            if mid - min_pos == 2 or max_pos - mid == 2:
                min_res = 1
            else:
                min_res = 2
        elif mid - min_pos == 1 and max_pos - mid > 1:
            min_res = 1
        elif mid - min_pos > 1 and max_pos - mid == 1:
            min_res = 1

        return [min_res, max_res]

    def advanced(self, a: int, b: int, c: int) -> List[int]:
        min_pos, mid, max_pos = sorted((a, b, c))
        min_res, max_res = 0, 0

        if max_pos - min_pos > 2:
            max_res = max_pos - min_pos - 2
            min_res = 2 if max_pos - mid > 2 and mid - min_pos > 2 else 1

        return [min_res, max_res]
