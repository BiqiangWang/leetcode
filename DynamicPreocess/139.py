from typing import List


# def advanced(s: str, wordDict: List[str]) -> bool:
#     dp = [False] * (len(s) + 1)
#     dp[0] = True
#     for i in range(len(s)):
#         if dp[i]:
#             for


def wordBreak(s: str, wordDict: List[str]) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(0, n):
        if dp[i]:
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict:
                    dp[j] = True
    return dp[n]


if __name__ == '__main__':
    ss = "applepenapple"
    d = ["apple", "pen"]
    print(wordBreak(ss, d))
