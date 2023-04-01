def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m, n, t = len(s1), len(s2), len(s3)
    if n + m != t:
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(0, m + 1):
        for j in range(0, n + 1):
            if i > 0:
                dp[i][j] = dp[i-1][j] and s1[i - 1] == s3[i + j - 1]
            if j > 0:
                dp[i][j] |= dp[i][j-1] and s2[j - 1] == s3[i + j - 1]
    print(dp)
    return dp[m][n]


if __name__ == '__main__':
    z1, z2, z3 = "aabcc", "dbbca", "aadbbcbcac"
    print(isInterleave(z1, z2, z3))
