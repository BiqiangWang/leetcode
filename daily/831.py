class Solution:
    def maskPII(self, s: str) -> str:
        if 'a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z':
            s = s.lower()
            arr = list(s)
            len_1 = len(arr)
            n = 0
            for i in range(len_1):
                if arr[i] == '@':
                    n = i
            print(n)
            if n > 1:
                return arr[0] + "*****" + "".join(arr[n - 1:len_1])
            else:
                return ''.join(arr)
        else:
            arr = list(s)
            len_1 = len(arr)
            n = 0
            for i in range(len_1):
                if arr[i].isdigit():
                    arr[n] = arr[i]
                    n += 1
            if n > 10:
                return '+' + ''.join(['*'] * (n-10)) + '-' + ''.join(['*'] * 3) + '-' + ''.join(['*'] * 3) + '-' + ''.join(arr[n - 4:n])
            else:
                return ''.join(['*'] * 3) + '-' + ''.join(['*'] * 3) + '-' + ''.join(arr[n - 4:n])


    def advanced(self, s: str) -> str:
        if s[0].isalpha():
            s = s.lower()
            return s[0] + '*****' + s[s.find('@') - 1:]
        s = ''.join(c for c in s if c.isdigit())
        cnt = len(s) - 10
        back = '***-***-' + s[-4:]
        return back if cnt == 0 else f'+{"*" * cnt}-{back}'

if __name__ == '__main__':
    z = "LeeeC@LeetCode.com"
    v = "86-(10)12345678"
    so = Solution()
    print(so.advanced(v))
