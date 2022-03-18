number = int(input())
spaces = len(str(bin(number))[2:]) + 1
for each in range(1, number + 1):
    print("{padd}{de}{pado}{oct}{padh}{hex}{pad}{bi}".format(de=each, padd=' '*(spaces - len(str(each))),
                                                oct=str(oct(each))[2:], pado=' '*(spaces + 1 - len(str(oct(each))[2:])),
                                                hex=str(hex(each))[2:].upper(), padh=' '*(spaces + 1 - len(str(hex(each))[2:])),
                                                bi=str(bin(each))[2:], pad=' '*(spaces + 1 - len(str(bin(each))[2:]))))

