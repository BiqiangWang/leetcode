def advanced(a: int, b: int, c: int) -> int:
    score = 0
    if a > b:
        val = a
        a = b
        b = val
    if a <= c < b:
        val = b
        b = c
        c = val
    elif c < a:
        val = c
        c = b
        b = a
        a = val
    while a > 0:
        a -= 1
        score += 1
        if c > b:
            c -= 1
        else:
            b -= 1
    while b > 0:
        b -= 1
        c -= 1
        score += 1
    return score



def maximumScore(a: int, b: int, c: int) -> int:
    score = 0
    mi = min(a, b, c)
    ma = max(a, b, c)
    mo = 0
    min_flag = 1
    max_flag = 1
    for i in [a, b, c]:
        if i == mi:
            if min_flag == 0:
                mo = i
            min_flag = 0
        elif i == ma:
            if max_flag == 0:
                mo = i
            max_flag = 0
        else:
            mo = i
    while mi > 0:
        mi -= 1
        score += 1
        if ma > mo:
            ma -= 1
        else:
            mo -= 1
    while mo > 0:
        mo -= 1
        ma -= 1
        score += 1
    return score


if __name__ == '__main__':
    z, x, v = 6, 4, 2
    print(advanced(z, x, v))
