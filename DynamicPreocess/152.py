from typing import List


def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    cur_max = nums[0]
    cur_min = nums[0]
    ans = nums[0]
    for i in nums[1: n]:
        last_max = cur_max
        cur_max = max(cur_min * i, max(cur_max * i, i))
        cur_min = min(cur_min * i, min(last_max * i, i))
        ans = max(ans, max(cur_max, cur_min))
    return ans


# def maxProduct(nums: List[int]) -> int:
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
#     cur_max = nums[0] if nums[0] != 0 else 1
#     cur_min = nums[0] if nums[0] != 0 else 1
#     ans = nums[0]
#     for i in range(1, n):
#         if nums[i] > 0:
#             if cur_max > 0:
#                 cur_max = cur_max * nums[i]
#                 ans = max(ans, cur_max)
#             elif cur_max < 0:
#                 cur_max = nums[i]
#                 ans = max(ans, cur_max)
#             if cur_min > 0:
#                 cur_min = nums[i]
#             elif cur_min < 0:
#                 cur_min = cur_min * nums[i]
#         elif nums[i] < 0:
#             last_max = cur_max
#             if cur_min > 0:
#                 cur_max = nums[i]
#                 ans = max(ans, cur_max)
#             elif cur_min < 0:
#                 cur_max = cur_min * nums[i]
#                 ans = max(ans, cur_max)
#             if last_max > 0:
#                 cur_min = last_max * nums[i]
#             elif last_max < 0:
#                 cur_min = nums[i]
#         elif nums[i] == 0:
#             ans = max(ans, 0)
#             cur_max, cur_min = 1, 1
#     return ans


if __name__ == '__main__':
    z = [0, 2]
    # z = [2, 3, -2, 4]
    print(maxProduct(z))
