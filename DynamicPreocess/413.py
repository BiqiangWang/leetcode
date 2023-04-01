from typing import List


def numberOfArithmeticSlices(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0
    ans, val = 0, 0
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            val += 1
            ans += val
        else:
            val = 0
    return ans


if __name__ == '__main__':
    z = [1, 2, 3, 4]
    print(numberOfArithmeticSlices(z))
