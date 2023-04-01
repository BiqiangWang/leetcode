def countSubstrings(s: str) -> int:
    n = len(s)
    ans = n
    for i in range(n):
        left, right = i-1, i+1
        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            ans += 1
            left -= 1
            right += 1
        left, right = i, i+1
        while left >= 0 and right < n:
            if s[left] != s[right]:
                break
            ans += 1
            left -= 1
            right += 1
    print(ans)


if __name__ == '__main__':
    ss = 'fdsklf'
    countSubstrings(ss)
