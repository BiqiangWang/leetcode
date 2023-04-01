from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = sorted(zip(scores, ages))
        dp = [0] * len(arr)
        for i, (score, age) in enumerate(arr):
            for j in range(i):
                if arr[j][1] <= age:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += score
        return max(dp)


if __name__ == '__main__':
    z, v = [1, 3, 5, 10, 15], [1, 2, 3, 4, 5]
    so = Solution()
    print(so.bestTeamScore(z, v))
