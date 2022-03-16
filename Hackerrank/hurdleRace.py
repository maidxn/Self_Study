numberOfHurdles, maxHeight = map(int, input().split())
hurdles = [int(i) for i in input().split()]

theTallest = max(hurdles)
ans = theTallest - maxHeight if theTallest - maxHeight > 0 else 0
print(ans)
