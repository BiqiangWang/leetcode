def reference(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = 1
    p2 = p3 = p5 = 1

    for i in range(2, n + 1):
        n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
        dp[i] = min(n2, n3, n5)
        if dp[i] == n2:
            p2 += 1
        elif dp[i] == n3:
            p3 += 1
        else:
            p5 += 1
    return dp[n]


# timeout
def nthUglyNumber(n: int) -> int:
    arr = [1, 2, 3, 5]
    two, three, five = [2], [3], [5]

    def my_insert(number):
        for t in range(0, len(arr)):
            if number < arr[t]:
                arr.insert(t, number)
                return
        arr.append(number)

    def find_min(a1, b1, c1):
        if a1 < min(b1, c1):
            return 0
        elif b1 < min(a1, c1):
            return 1
        else:
            return 2

    def add_in(num, arr1, arr2):
        for k in arr1:
            if num > k:
                my_insert(num * k)
        for k in arr2:
            if num > k:
                my_insert(num * k)
        for k1 in arr1:
            for k2 in arr2:
                if num > k1 and num > k2:
                    my_insert(num * k1 * k2)

    while len(arr) < n + 10 or min(two[len(two) - 1], min(three[len(three) - 1], five[len(five) - 1])) < arr[n - 1]:
        a, b, c = two[len(two) - 1], three[len(three) - 1], five[len(five) - 1]
        i = find_min(a, b, c)
        print(a, b, c, i)
        if i == 0:
            add_in(a, three, five)
            val = a * 2
            my_insert(val)
            two.append(val)
        elif i == 1:
            add_in(b, two, five)
            val = b * 3
            my_insert(val)
            three.append(val)
        else:
            add_in(c, two, three)
            val = c * 5
            my_insert(val)
            five.append(val)
    print(arr)
    return arr[n - 1]


if __name__ == '__main__':
    print(nthUglyNumber(500))
