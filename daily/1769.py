# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def minOperations(boxes: str) -> List[int]:
    # arr = list(boxes)
    n = len(boxes)
    left, right, op = int(boxes[0]), 0, 0
    # ans = [0] * n
    for i in range(1, n):
        if boxes[i] == '1':
            right += 1
            op += i
    ans = [op]
    for i in range(1, n):
        op += + left - right
        if boxes[i] == '1':
            left += 1
            right -= 1
        ans.append(op)
    print(ans)
    return ans

    # time out
    # flag = [0] * n
    # for i in range(0, n):
    #     if int(arr[i]) == 1:
    #         flag[i] = 1
    #     for j in range(0, i + 1):
    #         if int(arr[j]) == 1:
    #             ans[i] += abs(i - j)
    #         if int(arr[i]) == 1:
    #             ans[j] += abs(i - j)
    # print(ans)
    # return ans

    # time out
    ans = []
    for i in range(0, n):
        res = 0
        for j in range(0, n):
            res += abs(i - j) if boxes[j] == '1' else 0
        ans.append(res)
    # print(ans)
    # return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = '110'
    minOperations(s)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
