from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s) - 1
        while l < r:
            char = s[l]
            s[l] = s[r]
            s[r] = char
            l += 1
            r -= 1

    def advanced(self, s: List[str]) -> None:
        s[::] = [s[i] for i in range(len(s) - 1, -1, -1)]    # s[::] 和 s[:] 类似，都是指从头到尾遍历的数组
