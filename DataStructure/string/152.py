class Solution:
    def reverseWords(self, s: str) -> str:
        li = list(s)
        res = []
        c = ''
        for char in li:
            if char != ' ':
                c = c + char
            else:
                if c != '':
                    res.append(c)
                    c = ''
        if c != '':
            res.append(c)
        res.reverse()
        return " ".join(res)