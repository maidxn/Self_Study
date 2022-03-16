def CreateArray(size):
    return [number for number in range(size + 1)]


firstArray = CreateArray(int(input()))
secondArray = CreateArray(int(input()))
thirdArray = CreateArray(int(input()))
theSum = int(input())

# ans = []
# for i in firstArray:
#     for j in secondArray:
#         for k in thirdArray:
#             if i + j + k != theSum:
#                 ans.append([i, j, k])
#
# print(ans)

# Another way to solve the problem most effective is
print([[i, j, k] for i in firstArray for j in secondArray for k in thirdArray if i + j + k != theSum])
