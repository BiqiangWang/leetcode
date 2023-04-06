from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x, y = 0, 0
        x_edge, y_edge = [0, n], [0, n]
        case = 1
        ans = [[1] * n for _ in range(n)]
        for num in range(n * n):
            ans[x][y] += num
            if case == 1:
                if y < y_edge[1] - 1:
                    y += 1
                else:
                    x += 1
                    x_edge[0] = int(x_edge[0]) + 1
                    case = 2
            elif case == 2:
                if x < x_edge[1] - 1:
                    x += 1
                else:
                    y -= 1
                    y_edge[1] = int(y_edge[1]) - 1
                    case = 3
            elif case == 3:
                if y > y_edge[0]:
                    y -= 1
                else:
                    x -= 1
                    x_edge[1] = int(x_edge[1]) - 1
                    case = 4
            elif case == 4:
                if x > x_edge[0]:
                    x -= 1
                else:
                    y += 1
                    y_edge[0] = int(y_edge[0]) + 1
                    case = 1
        return ans


if __name__ == '__main__':
    z = 3
    so = Solution()
    print(so.generateMatrix(z))
