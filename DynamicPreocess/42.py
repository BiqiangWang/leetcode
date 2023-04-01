from typing import List


def easy(height: List[int]) -> int:
    stack = list()
    ans = 0
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            left = stack[-1]
            currWidth = i - left - 1
            currHeight = min(height[left], height[i]) - height[top]
            ans += currWidth * currHeight
        stack.append(i)
    return ans


def trap(height: List[int]) -> int:
    n = len(height)
    leftMax, rightMax = [height[0]] * n, [height[n - 1]] * n
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], height[i])
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], height[i])
    print(leftMax, rightMax)
    rain = 0
    for i in range(0, n):
        if height[i] < leftMax[i] and height[i] < rightMax[i]:
            rain += min(leftMax[i], rightMax[i]) - height[i]
    return rain


if __name__ == '__main__':
    z = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(easy(z))
