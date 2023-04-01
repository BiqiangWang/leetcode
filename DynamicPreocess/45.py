from typing import List


# def jump(nums: List[int]) -> int:
#     n = len(nums)
#     ans = []
#
#     def reachNext(start, end, layer: int):
#         if end >= n - 1:
#             ans.append(layer)
#             return
#         head = tail = start + 1
#         for i in range(start, end + 1):
#             print(start, end, i)
#             a = i + 1
#             b = i + nums[i]
#             head = max(head, a)
#             tail = max(tail, b)
#         reachNext(head, tail, layer + 1)
#
#     reachNext(0, 0, 0)
#     print(ans[0])
#     return ans[0]

# timeout
def jump(nums: List[int]) -> int:
    n = len(nums)
    dp = [float("inf")] * n
    dp[0] = 0
    print(dp)
    for i in range(n):
        for j in range(i, min(i + nums[i] + 1, n)):
            dp[j] = min(dp[j], dp[i] + 1)
    print(dp)
    return dp[n - 1]


if __name__ == '__main__':
    ar = [2, 3, 1, 1, 4]
    print(jump(ar))
