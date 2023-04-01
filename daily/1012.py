from functools import lru_cache

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)
        """
            本着正难则反的原则，本题采用反向做法
        """

        @lru_cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            """
            f(i,mask,isLimit,isNum) 表示构造从高到低第i位及其之后数位的合法方案数
            :param i:
            :param mask: 表示前面选过的数字集合，换句话说，第i位要选的数字不能在mask中。
            :param is_limit: 表示当前是否受到了n的约束。
                                若为真，则第i位填入的数字至多为s[i]，否则可以是9。
                                如果在受到约束的情况下填了s[i]，那么后续填入的数字仍会受到n的约束。
            :param is_num: 表示i前面的数位是否填了数字。
                                若为假，则当前位可以跳过（不填数字），或者要填入的数字至少为1；
                                若为真，则要填入的数字可以从0开始。
            :return:
            """
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, mask, False, False)
            low = 0 if is_num else 1  # 若前面没有填数字，则需要从1开始（因为第一位不能为0）
            up = int(s[i]) if is_limit else 9  # 若前面的数字都填的和n的一样
            for d in range(low, up + 1):
                if (mask >> d & 1) == 0:  # 说明d不在mask中
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res

        return n - f(0, 0, True, False)


if __name__ == '__main__':
    z = 1000
    so = Solution()
    print(so.numDupDigitsAtMostN(z))
