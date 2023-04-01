from typing import List


def minElements(nums: List[int], limit: int, goal: int) -> int:
    need = goal - sum(nums)
    if need == 0:
        return 0
    if abs(need) <= limit:
        return 1
    else:
        add_num = 1 if abs(need) % limit != 0 else 0
        return int(abs(need) / limit) + add_num


if __name__ == '__main__':
    z = [1, -1, 1]
    l = 3
    g = -4
    print(minElements(z, l, g))
