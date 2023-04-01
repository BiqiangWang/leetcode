from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    nu = [2, 7, 11, 15]
    t = 9
    print(twoSum(nu, t))
