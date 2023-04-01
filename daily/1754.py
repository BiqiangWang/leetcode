class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        merge = ""
        i = j = 0
        while i < m and j < n:
            if word1[i] > word2[j]:
                merge += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                merge += word2[j]
                j += 1
            else:
                k = 1
                while i + k < m and j + k < n and word1[i + k] == word2[j + k]:
                    k += 1
                if i + k == m:
                    merge += word2[j:j + k]
                    j += k
                elif j + k == n:
                    merge += word1[i:i + k]
                    i += k
                else:
                    if word1[i + k] > word2[j + k]:
                        if word1[i + k] > word1[i + k - 1]:
                            merge += word1[i:i + k]
                            i += k
                        else:
                            merge += word1[i:i + k]
                            merge += word2[j:j + k]
                            i += k
                            j += k
                    else:
                        if word2[j + k] > word2[j + k - 1]:
                            merge += word2[j:j + k]
                            j += k
                        else:
                            merge += word1[i:i + k]
                            merge += word2[j:j + k]
                            i += k
                            j += k
            print(i, j, merge)
        if i < m:
            merge += word1[i:m]
        elif j < n:
            merge += word2[j:n]
        return merge


class Advanced:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ""
        while len(word1) or len(word2):
            if word1 > word2:
                merge += word1[0]
                word1 = word1[1:len(word1)]
            else:
                merge += word2[0]
                word2 = word2[1:len(word2)]
        return merge


if __name__ == '__main__':
    z, v = "wwwwwwwwwddwddwwdwwwwwwwwwwwwwwwdddddddddddddwwddddddwddw", "wwwwwwwwwddwwdwwwwwwwwwwwwwwwddwdddddddddddddwwddddddwddw"
    so = Advanced()
    print(so.largestMerge(z, v))
