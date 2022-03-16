import numpy

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = numpy.array(arr)

# Or
# And it's faster :)
arr = numpy.array([input().split() for i in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))

