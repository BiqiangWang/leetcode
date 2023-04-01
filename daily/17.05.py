from typing import List
import numpy as np


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        n = len(array)
        count = np.zeros([n + 1], dtype=np.dtype)
        for i in range(1, n + 1):
            if 'A' <= array[i - 1] <= 'Z' or 'a' <= array[i - 1] <= 'z':
                count[i] = count[i - 1] + 1
            else:
                count[i] = count[i - 1] - 1
        map = dict()
        map.setdefault(0, 0)
        print(count)
        mlen, start, end = 0, -1, -1
        for i in range(1, n + 1):
            if count[i] not in map:
                map.setdefault(count[i], i)
            else:
                if i - map[count[i]] > mlen:
                    mlen = i - map[count[i]]
                    start = map[count[i]]
                    end = i
        return array[start:end]


if __name__ == '__main__':
    z = ["42", "10", "O", "t", "y", "p", "g", "B", "96", "H", "5", "v", "P", "52", "25", "96", "b", "L", "Y", "z", "d",
         "52", "3", "v", "71", "J", "A", "0", "v", "51", "E", "k", "H", "96", "21", "W", "59", "I", "V", "s", "59", "w",
         "X", "33", "29", "H", "32", "51", "f", "i", "58", "56", "66", "90", "F", "10", "93", "53", "85", "28", "78",
         "d", "67", "81", "T", "K", "S", "l", "L", "Z", "j", "5", "R", "b", "44", "R", "h", "B", "30", "63", "z", "75",
         "60", "m", "61", "a", "5", "S", "Z", "D", "2", "A", "W", "k", "84", "44", "96", "96", "y", "M"]
    so = Solution()
    print(so.findLongestSubarray(z))
