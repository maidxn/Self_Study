athletes, attributes = map(int, input().split())
dictionary = {}
for each in range(athletes):
    dictionary[each] = list(map(int, input().split()))
sortedPos = int(input())
arr = list(zip(*dictionary.values()))
print(arr[sortedPos])
sortedDic = {}
index = 0
for each in arr[sortedPos]:
    sortedDic[index] = each
    index += 1
ans = dict(sorted(sortedDic.items(), key=lambda item: item[1]))
for key in ans.keys():
    print(*dictionary[key], sep=' ')
# So first I took the specific values to asign 0, 1,... to N, then sort
# Then find the indices then back to the dictionary from the start ;;-;;

# And here is the solution
N, M = map(int, input().split())
# Use normal array instead of dictionary like the way I did
rows = [list(map(int, input().split())) for i in range(N)]
i = int(input())
# Then we can sort here, using the lambda, and specify a row we want :)
# It's so elegant :>
rows = sorted(rows, key=lambda x: x[i])
for i in rows:
    print(*i)
