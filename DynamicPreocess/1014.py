from typing import List


def maxScoreSightseeingPair(values: List[int]) -> int:
    n = len(values)
    ans = 0
    cur, index = values[0], 0
    for i in range(1, n):
        ans = max(ans, values[i] + cur + index - i)
        if cur + index < values[i] + i:
            cur = values[i]
            index = i
        print(cur, index)
    return ans


if __name__ == '__main__':
    v = [8, 1, 5, 2, 6]
    print(maxScoreSightseeingPair(v))
