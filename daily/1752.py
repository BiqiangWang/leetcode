# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def check(array):
    length = len(array)
    pos = 0
    for i in range(0, len(array)):
        if i > 0:
            if array[i - 1] > array[i]:
                pos = i
                break
    print(pos)
    for i in range(0, len(array) - 1):
        index = (pos + i) % length
        next_index = (pos + i + 1) % length
        print(index)
        print(next_index)
        if array[index] > array[next_index]:
            print(False)
            return False
    print(True)
    return True


def ad_check(nums):
    length = len(nums)
    flag = 0
    if length == 0:
        return True
    for i in range(0, length):
        now = nums[i]
        nex = nums[(i + 1) % length]
        print(now, nex)
        if now > nex:
            flag += 1
        if flag > 1:
            print(False)
            return False
    print(True)
    return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # nums = [3, 4, 5, 1, 2]
    arr = [2, 1, 3, 4]
    # arr = [1, 2, 3]
    ad_check(arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
