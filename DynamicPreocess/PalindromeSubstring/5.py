# time out, visit leetcode.com to see the right answer
def function(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


def longestPalindrome(s: str) -> str:
    start, end = 0, 0
    n = len(s)
    for i in range(n):
        left1, right1 = function(s, i, i)
        left2, right2 = function(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    print(s[start: end+1])


if __name__ == '__main__':
    str = 'babad'
    longestPalindrome(str)
