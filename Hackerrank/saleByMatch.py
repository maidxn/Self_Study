def sockMerchant(n, arr):
    max_item = max(arr)
    ans = [0] * max_item
    for item in arr:
        ans[item - 1] += 1
    pairs = 0
    for item in ans:
        pairs += item // 2
    return pairs


size = int(input())
socks = [int(i) for i in input().split()]
print(sockMerchant(size, socks))
