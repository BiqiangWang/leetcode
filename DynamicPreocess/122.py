from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0
    in_price = prices[0]
    ans = 0
    res = 0
    for i in range(1, n):
        if prices[i] >= in_price:
            ans = max(ans, prices[i] - in_price)
        else:
            in_price = prices[i]
        if ans != 0 and prices[i] < prices[i - 1]:
            res += ans
            ans = 0
            in_price = prices[i]
    if ans != 0:
        res += ans
    return res


if __name__ == '__main__':
    v = [7, 1, 5, 3, 6, 4]
    print(maxProfit(v))
