sizeA = int(input())
arrayA = set(map(int, input().split()))
sizeB = int(input())
arrayB = set(map(int, input().split()))

print(len(arrayA.intersection(arrayB)))


