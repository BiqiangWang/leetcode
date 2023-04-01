from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * (n+1)
    if n == 1:
        return nums[0]
    for i in range(0, n):
        if i < 2:
            dp[i+1] = nums[i]
        else:
            dp[i+1] = max(dp[i-1], dp[i-2]) + nums[i]
    return max(dp[n], dp[n-1])


if __name__ == '__main__':
    ar = [1]
    print(rob(ar))
