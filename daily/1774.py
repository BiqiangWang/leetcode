from typing import List


def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
    x = min(baseCosts)
    if x > target:
        return x
    dp = [False] * (target + 1)
    ans = 2 * target - x
    for i in baseCosts:
        if i <= target:
            dp[i] = True
        else:
            ans = min(ans, i)

    """
    首先明确：不需要提供具体方案，因此只需关注价格是否能够达到
    大致思路为：记录小于target的所有价格方案的可能性，和一个大于target的最小价格
    
    将所有的小料遍历两遍，遍历当前所有可能的价格方案
    若有价格为i的方案满足 i+当前小料价格c > 目标价格target， 则更新大于target的 最优解
    若当前价格方案暂不存在，则尝试通过 i-c寻找更小的解决方案， 因为若dp[i-c]存在， 则选取前小料c时， dp[i]也存在
    通过不断更新各种价格方案可能性，最终得到所有组合的价格可能性
    """
    for c in toppingCosts:
        for count in range(2):
            for i in range(target, 0, -1):
                if dp[i] and i + c > target:
                    ans = min(ans, i + c)
                if i - c > 0 and not dp[i]:
                    dp[i] = dp[i - c]

    # 从target开始向前遍历ans-target个， 若没有这些方案，则选择大于target 的ans
    for i in range(ans - target + 1):
        if dp[target - i]:
            return target - i
    return ans


# def closestCost(baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
#     toppingCosts.extend(toppingCosts)
#     val = [baseCosts[0]]
#
#     def choseTopp(top, money):
#         print(top, money, val)
#         if not top:
#             if abs(money) < abs(target - val[0]):
#                 val.clear()
#                 val.append(target - money)
#             return
#         if money >= 0:
#             arr = top.copy()
#             a = arr[0]
#             arr.pop()
#             choseTopp(arr, money - a)
#             choseTopp(arr, money)
#
#     for i in baseCosts:
#         t = toppingCosts.copy()
#         choseTopp(t, target - i)
#
#     return baseCosts[0] if not val else val[0]


if __name__ == '__main__':
    base, topp, tar = [2, 3], [4, 5, 100], 18
    # base, topp, tar = [10], [1], 1
    print(closestCost(base, topp, tar))

