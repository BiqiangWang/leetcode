from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    d = dict()
    for i in nums1:
        if i not in d:
            d.setdefault(i, 1)
        else:
            d[i] += 1
    ans = []
    for i in nums2:
        if i in d:
            ans.append(i)
            d[i] -= 1
            if d[i] == 0:
                d.pop(i)
    return ans


if __name__ == '__main__':
    hashtable(1,1)
    # p, l = [1, 2, 2, 1], [2, 2, 2]
    # print(intersect(p, l))
