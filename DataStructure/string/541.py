class Solution:
    """
        这道题对python3有非常变态的要求！！！

        python3规定不能直接对str中的某一项进行直接修改，只能通过多次字符串拼接来实现部分翻转

    """

    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s