from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowel = ['a', 'e', 'i', 'o', 'u']
        vowel_arr = [0] * (n + 1)
        for i, w in enumerate(words):
            vowel_arr[i + 1] = vowel_arr[i] + 1 if w[0] in vowel and w[-1] in vowel else vowel_arr[i]
        return [vowel_arr[r + 1] - vowel_arr[l] for l, r in queries]
