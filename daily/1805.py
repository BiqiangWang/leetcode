def numDifferentIntegers(word: str) -> int:
    get_int = ''.join([c if '0' <= c <= '9' else ' ' for c in word]).strip().split()
    print(get_int)
    ans = set(int(x) for x in get_int)
    print(set(int(x) for x in get_int))
    return len(ans)

# # answer 1
# def numDifferentIntegers(word: str) -> int:
#     nums = []
#     st = ""
#
#     def isInArray(a, arr) -> bool:
#         for i in arr:
#             if a == i:
#                 return True
#         return False
#
#     for char in word:
#         if not ('0' <= char <= '9') and st != "":
#             if not isInArray(int(st), nums):
#                 nums.append(int(st))
#             st = ''
#         if '0' <= char <= '9':
#             st += char
#     if st != '' and not isInArray(int(st), nums):
#         nums.append(int(st))
#     print(nums)
#     return len(nums)


if __name__ == '__main__':
    # z = "a123b34c34d8ef34"
    # z = "a1b01c001"
    z = '9'
    print(numDifferentIntegers(z))
