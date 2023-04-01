from typing import List


class Solution:
    def check_flush(self, suit):
        val = suit[0]
        for i in suit:
            if i != val:
                return False
        return True

    def checkTKorPair(self, rank):
        d = dict()
        for i in rank:
            if i not in d:
                d.setdefault(i, 1)
            else:
                d[i] += 1
                if d[i] == 3:
                    return 3
        for item in d.items():
            if item[1] == 2:
                return 2
        return 1

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if self.check_flush(suits):
            return "Flush"
        checkPoint = self.checkTKorPair(ranks)
        if checkPoint == 3:
            return "Three of a Kind"
        elif checkPoint == 2:
            return "Pair"
        else:
            return "High Card"


if __name__ == '__main__':
    z, x = [4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]
    solu = Solution()
    print(solu.bestHand(z, x))
