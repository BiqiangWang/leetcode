from typing import List


def advanced(nums: List[int]) -> bool:
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


def containsDuplicate(nums: List[int]) -> bool:
    d = dict()
    for i in nums:
        if i in d:
            return True
        d.setdefault(i, 1)
        print(d)
    return False


if __name__ == '__main__':
    v = [1, 2, 3, 1]
    print(containsDuplicate(v))
