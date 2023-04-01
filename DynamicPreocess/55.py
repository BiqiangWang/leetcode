from typing import List


def canJump(nums: List[int]) -> bool:
    n = len(nums)
    k = 0
    for i in range(0, n):
        if i > k:
            return False
        k = max(k, i + nums[i])
    return True


#  time out 2
# def canJump(nums: List[int]) -> bool:
#     n = len(nums)
#     if nums[0] == 0:
#         if n == 1:
#             return True
#         else:
#             return False
#     dp = [False] * (n + 1)
#     dp[0] = True
#
#     def updateState(start, end):
#         print(start, end)
#         if end >= n - 1:
#             dp[n - 1] = True
#             return
#         if start == end and nums[start] == 0:
#             return
#         next_end = end
#         for i in range(start, end + 1):
#             if i < n:
#                 dp[i] = True
#                 if i + nums[i] > end:
#                     next_end = max(next_end, i + nums[i])
#         updateState(start + 1, next_end)
#
#     updateState(0, 0)
#     return dp[n - 1]

# # timeout
# def canJump(nums: List[int]) -> bool:
#     n = len(nums)
#     dp = [False] * (n + 1)
#     dp[0] = True
#     for i in range(0, n):
#         if dp[i]:
#             for val in range(1, nums[i] + 1):
#                 if i + val < n:
#                     dp[i + val] = True
#     return dp[n-1]


if __name__ == '__main__':
    ar = [2, 3, 1, 1, 4]
    # ar = [1, 2, 3]
    print(canJump(ar))
