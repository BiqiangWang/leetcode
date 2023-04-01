from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    for i in range(0, n-1):
        if i < 2:
            dp[i + 1] = nums[i]
        else:
            dp[i + 1] = max(dp[i - 1], dp[i - 2]) + nums[i]
    res1 = max(dp[n-1], dp[n-2])
    print(dp)
    dp = [0] * (n + 1)
    if n == 1:
        return nums[0]
    for i in range(1, n):
        if i < 2:
            dp[i + 1] = nums[i]
        else:
            dp[i + 1] = max(dp[i - 1], dp[i - 2]) + nums[i]
    res2 = max(dp[n], dp[n-1])
    return max(res1, res2)


if __name__ == '__main__':
    ar = [200,3,140,20,10]
    print(rob(ar))
