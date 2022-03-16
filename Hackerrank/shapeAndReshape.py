import numpy

print(numpy.array(input().split(), int).reshape(3, 3))
# One line :) Really :>>
# Actually we don't need to use map(int, list) to asign elements' type,
# in numpy can just define dtype = int
