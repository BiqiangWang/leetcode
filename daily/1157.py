from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.t = dict(list)
        for j in range(len(arr)):
            self.t[arr[j]].append(j)  # 按顺序遍历数组，每个元素的下标数组就自然是有序，可以直接二分
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        print(self.arr)


if __name__ == '__main__':
    z = [1, 1, 2, 2, 1, 1]
    obj = MajorityChecker(z)
    print(obj.query(0, 5, 4))

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
