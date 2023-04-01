from typing import List


def maxSubArray(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = nums[i] if dp[i] < 0 else dp[i] + nums[i]
    print(dp)
    return max(dp)

    # if n == 0:
    #     return 0
    # dp = [0] * (n)
    # dp[0] = nums[0]
    # for i in range(1, n):
    #     dp[i] = nums[i] if dp[i - 1] < 0 else dp[i - 1] + nums[i]
    # print(dp)
    # return max(dp[1: n+1])


if __name__ == '__main__':
    ar = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(ar))
