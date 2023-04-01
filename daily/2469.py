from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kai = celsius + 273.15
        hua = celsius * 1.8 + 32
        return [round(kai, 5), round(hua, 5)]


if __name__ == '__main__':
    z = 36.50
    so = Solution()
    so.convertTemperature(z)
