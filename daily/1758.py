# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def reverse(t, i):
    if t[i] == '1':
        t[i] = '0'
    elif t[i] == '0':
        t[i] = '1'
    return t


def isSame(a, b):
    if a == b:
        return True
    return False


def minOperations(s: str) -> int:
    res1 = 0  # 记录010101类型
    n = len(s)
    # l = list(s)
    # if l[0] == '1':
    #     reverse(l, 0)
    #     res1 += 1
    # pre = '0'
    # for i in range(1, n):
    #     if isSame(l[i], pre):
    #         reverse(l, i)
    #         res1 += 1
    #     pre = l[i]

    should = '0'
    for i in s:
        if i != should:
            res1 += 1
        should = '1' if should == '0' else '0'

    res2 = n - res1
    print(min(res1, res2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st = "0100"
    minOperations(st)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
