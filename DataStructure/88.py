from typing import List


def back(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j = m - 1, n - 1
    while i >= 0 or j >= 0:
        if j == 0:
            break
        elif i == 0:
            nums1[:j + 1] = nums2[:j + 1]
            break
        else:
            if nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    n1_copy = nums1.copy()

    def insert(pos, number):
        for v in range(m + n - 1, pos, -1):
            nums1[v] = nums1[v - 1]
        nums1[pos] = number

    i, j = 0, 0
    while i < m or j < n:
        if j == n:
            break
        elif i == m:
            for t in range(j, n):
                nums1[i + t] = nums2[t]
            break
        else:
            if n1_copy[i] <= nums2[j]:
                i += 1
            else:
                insert(i + j, nums2[j])
                j += 1
    print(nums1)


if __name__ == '__main__':
    a, b = [4, 5, 6, 0, 0, 0], [1, 2, 3]
    merge(a, 3, b, 3)
