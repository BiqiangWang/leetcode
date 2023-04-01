from typing import List


def generateParenthesis(n: int) -> List[str]:
    ans = []

    def function(st, left, right):
        if len(st) == 2 * n:
            ans.append(''.join(st))
            return
        if left < n:
            st.append('(')
            function(st, left + 1, right)
            st.pop()
        if right < left:
            st.append(')')
            function(st, left, right + 1)
            st.pop()

    function([], 0, 0)
    return ans


if __name__ == '__main__':
    r = 3
    print(generateParenthesis(r))
