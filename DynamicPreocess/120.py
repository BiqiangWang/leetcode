from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    if len(triangle) == 0:
        return triangle[0][0]
    last_layer = triangle[0]
    for layer in triangle[1:]:
        n = len(layer)
        for i in range(0, n):
            if i == 0:
                layer[0] += last_layer[0]
            elif i == n - 1:
                layer[n - 1] += last_layer[n - 2]
            else:
                layer[i] += min(last_layer[i - 1], last_layer[i])
        last_layer = layer
    print(triangle)
    return min(triangle[len(triangle) - 1])


if __name__ == '__main__':
    # z = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    z = [[]]
    print(minimumTotal(z))
