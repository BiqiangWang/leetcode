# This is a sample Python script.
from itertools import accumulate

import numpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def largestSumOfAverages(nums, k):
    n = len(nums)
    prefix_array = [0]
    summary = 0
    for i in range(0, n):
        summary += nums[i]
        prefix_array.append(summary)
    # print(prefix_array)
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = prefix_array[i] / i
    for j in range(2, k + 1):  # 分组数：2-k
        for i in range(j, n + 1):  # 前i项： j-n ，不能比分组数还少
            for t in range(j - 1, i):
                dp[i][j] = max(dp[i][j], dp[t][j - 1] + (prefix_array[i] - prefix_array[t]) / (i - t))
    print(dp[n][k])
    return dp[n][k]

    # prefix_array = list(accumulate(nums, initial=0))  # 前缀和数组
    # print(prefix_array)
    # dp = [[0.0] * (k + 1) for _ in range(n + 1)]   # dp[i][j]表示前i项分成j组的最大前缀和
    # for i in range(1, n + 1):
    #     dp[i][1] = prefix_array[i] / i
    # for j in range(2, k + 1):   # 遍历分组情况，从分2组到分k组
    #     for i in range(j, n + 1):    # 遍历总数情况，分别计算前i项
    #         for t in range(j - 1, i):    # 遍历新增分组位置 新增分组位置代表的最大前缀和为：前t-1项分j-1组的最大平均和 + 新分组的最大平均和
    #             dp[i][j] = max(dp[i][j], dp[t][j - 1] + (prefix_array[i] - prefix_array[t]) / (i - t))
    # print(dp)
    # return dp[n][k]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # array = [9, 1, 2, 3, 9]
    # key = 3
    array = [1, 2, 3, 4, 5, 6, 7]
    key = 4
    print(largestSumOfAverages(array, key))
