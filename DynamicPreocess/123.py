from typing import List


def maxProfit(prices: List[int]) -> int:
    buy1, buy2, sell1, sell2 = -prices[0], -prices[0], 0, 0
    for pr in prices:
        buy1 = max(buy1, -pr)
        sell1 = max(sell1, buy1 + pr)
        buy2 = max(buy2, sell1 - pr)
        sell2 = max(sell2, buy2 + pr)
    return sell2


if __name__ == '__main__':
    v = [3, 3, 5, 0, 0, 3, 1, 4]
    print(maxProfit(v))
