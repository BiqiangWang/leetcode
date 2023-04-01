# This is a sample Python script.
from typing import List


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    def abs(num):
        if num < 0:
            return -num
        return num
    min_dis = float('inf')
    res = -1
    for i, point in enumerate(points):
        if point[0] == x or point[1] == y:
            dis = abs(x - point[0]) + abs(y - point[1])
            if dis < min_dis:
                min_dis = dis
                res = i
    return res




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x, y = 3, 4
    p = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    print(nearestValidPoint(x, y, p))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
