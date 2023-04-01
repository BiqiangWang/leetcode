from typing import List


def getMaxLen(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    plus, minus = 0, 0
    ans = 0
    for i in nums:
        if i > 0:
            plus += 1
            ans = max(ans, plus)
            if minus != 0:
                minus += 1
        elif i < 0:
            if minus > 0:
                last_plus = plus
                plus = minus + 1
                minus = last_plus + 1
            elif minus == 0:
                minus = plus + 1
                plus = 0
            ans = max(ans, plus)
        else:
            plus, minus = 0, 0
        print(plus, minus)
    return ans


if __name__ == '__main__':
    # z = [1, -2, -3, 4]
    z = [-1]
    # z = [5,-20,-20,-39,-5,0,0,0,36,-32,0,-7,-10,-7,21,20,-12,-34,26,2]
    print(getMaxLen(z))


