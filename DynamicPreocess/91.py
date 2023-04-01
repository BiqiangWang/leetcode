def correct(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    if s[0] == '0':
        return 0
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(1, n):
        if int(s[i]) != 0:
            dp[i + 1] += dp[i]
        if int(s[i - 1]) == 1 or (int(s[i - 1]) == 2 and int(s[i]) <= 6):
            dp[i + 1] += dp[i - 1]
    print(dp)
    return dp[n]

# bug
def numDecodings(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    if s[0] == '0':
        return 0
    dp, last = [1] * n, int(s[0])
    for i in range(1, n):
        if last == 0:
            if int(s[i]) == 0:
                return 0
            else:
                dp[i] = dp[i - 1] + 1
        if (last == 1 and int(s[i]) != 0) or (int(last) == 2 and 0 < int(s[i]) <= 6):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
        if int(s[i]) == 0 and i - 2 >= 0:
            if int(s[i - 2]) == 1 or (int(s[i - 2]) == 2 and int(s[i - 1]) <= 2):
                dp[i] -= 1
        last = int(s[i])
    return dp[n - 1]


if __name__ == '__main__':
    z = "122"
    print(numDecodings(z))
