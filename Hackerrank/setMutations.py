sizeSet = int(input())
arrayA = set(map(int, input().split()))
operations = int(input())
for each in range(operations):
    name, sizeB = input().split()
    arrayB = set(map(int, input().split()))
    if 'intersection' in name:
        arrayA.intersection_update(arrayB)
    elif 'symmetric' in name:  # the command symmetric and difference both have 'difference' so watch out the order
        arrayA.symmetric_difference_update(arrayB)
    elif 'difference' in name:
        arrayA.difference_update(arrayB)
    else:
        arrayA.update(arrayB)
print(sum(arrayA))

# Or just use the getattr()

for each in range(operations):
    name, size = input().split()
    arrayB = set(map(int, input().split()))
    getattr(arrayA, name)(arrayB)
print(sum(arrayA))
