from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:
    cur_max, cur_min, sum = 0, 0, 0
    sub_max, sub_min = nums[0], nums[0]
    for i in nums:
        cur_max = max(i, cur_max + i)
        sub_max = max(sub_max, cur_max)
        cur_min = min(i, cur_min + i)
        sub_min = min(sub_min, cur_min)
        sum += i
    print(sub_max, sub_min)
    return max(sub_max, sum - sub_min) if sub_max >= 0 else sub_max



if __name__ == '__main__':
    ar = [-2, -2]
    print(maxSubarraySumCircular(ar))
