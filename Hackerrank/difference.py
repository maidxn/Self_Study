sizeA = int(input())
arrA = set(map(int, input().split()))
sizeB = int(input())
arrB = set(map(int, input().split()))
print(len(arrA.difference(arrB)))