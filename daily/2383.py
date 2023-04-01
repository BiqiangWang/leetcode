from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        n = len(energy)
        all_need_energy = 1
        dvalue, before = 0, 0
        for i in range(n):
            all_need_energy += energy[i]
            dvalue = max(dvalue, experience[i] - before)
            before += experience[i]
        add_energy, add_experience = (max(0, all_need_energy - initialEnergy)), max(0, dvalue + 1 - initialExperience)
        print(add_energy, add_experience)
        return add_energy + add_experience


if __name__ == '__main__':
    a, b, z1, z2 = 5, 3, [1, 4, 3, 2], [2, 6, 3, 1]
    so = Solution()
    print(so.minNumberOfHours(a, b, z1, z2))
