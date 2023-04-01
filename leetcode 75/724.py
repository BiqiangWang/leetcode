from typing import List


def pivotIndex(nums: List[int]) -> int:
    n = len(nums)
    left, right = 0, sum(nums[1:n])
    if left == right:
        return 0
    for pos in range(1, n):
        left += nums[pos - 1]
        right -= nums[pos]
        if left == right:
            return pos
    return -1


if __name__ == '__main__':
    z = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(z))
