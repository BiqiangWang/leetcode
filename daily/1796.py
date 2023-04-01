def secondHighest(s: str) -> int:
    high, sec = -1, -1
    for char in s:
        if char.isdigit():
            num = int(char)
            if num > high:
                sec = high
                high = num
            elif sec < num < high:
                sec = num
        # if 'a' <= char <= 'z':
        #     continue
        # else:
        #     if int(char) > sec:
        #         if int(char) > high:
        #             sec = high
        #             high = int(char)
        #         elif sec < int(char) < high:
        #             sec = int(char)
    print(sec)
    return sec


if __name__ == '__main__':
    st = 'sjhtz8344'
    secondHighest(st)
