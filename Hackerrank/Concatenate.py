import numpy

row_1, row_2, column = input().split()
arr_1, arr_2 = [], []
for i in range(int(row_1)):
    arr_1.append(input().split())
for i in range(int(row_2)):
    arr_2.append(input().split())

arr_1 = numpy.array(arr_1, dtype=int)
arr_2 = numpy.array(arr_2, dtype=int)

# Remember one thing is you have to put all the arrays you
# are going to concatenating to (), then put in
# numpy.concatenate( ) <= 2 ()
print(numpy.concatenate((arr_1, arr_2)))



