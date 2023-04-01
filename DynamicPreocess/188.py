from typing import List


def maxProfit(k: int, prices: List[int]) -> int:
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)
    for pr in prices:
        for i in range(1, k + 1):
            buy[i] = max(buy[i], sell[i - 1] - pr)
            sell[i] = max(sell[i], buy[i] + pr)
    return sell[k]


if __name__ == '__main__':
    z, v = 2, [2, 4, 1]
    print(maxProfit(z, v))