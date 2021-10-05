numberOfElements = int(input())
array = [int(i) for i in input().split()]

array.sort()
count = 1
maxLen = 1
pre = 0
flag = True
# print(array)
for index in range(1, len(array)):
    # print("Count = ", count)
    # print("Max = ", maxLen)
    # print("Array[i]", array[index], index)
    if index == len(array) - 1:
        # print("TRUUUUE")
        if array[index] == array[index - 1]:
            count += 1
            # print("Count here", count)
        else:
            break
    else:
        if array[index] - array[index - 1] <= 1 and array[index] - array[pre] <= 1:
            count += 1
            # print("A case")
        else:
            pre = index
            maxLen = max(count, maxLen)
            count = 1
            # print("B case")

#     # if index == len(array) - 1 and array[index] - array[index - 1] <= 1:
#     #     count += 1
#     #     continue
#     # print("ITEM", array[index])
#     # print("PRE", array[pre])
#     # print("INDEX", index)
#     if array[index] - array[pre] <= 1 and array[index + 1] - array[index] <= 1:
#         count += 1
#     else:
#         flag = False
#         if array[index + 1] - array[index] > 1:
#             pre = index + 1
#         else:
#             pre += 1
#         if count > maxLen:
#             maxLen = count
#         count = 1
#     # print("COUNT", count)
# ans = count if flag else maxLen
# print("COUNT VS MAX", count, maxLen)
print(max(count, maxLen))
