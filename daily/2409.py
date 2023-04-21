class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive = max(arriveAlice, arriveBob)
        leave = min(leaveAlice, leaveBob)
        days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        arr_day = sum(days[:int(arrive[:2]) - 1]) + int(arrive[3:])
        lea_day = sum(days[:int(leave[:2]) - 1]) + int(leave[3:])
        return max(lea_day - arr_day + 1, 0)



if __name__ == '__main__':
    a, b, c, d = "08-15", "08-18", "08-16", "08-19"
    so = Solution()
    print(so.countDaysTogether(a, b, c, d))
