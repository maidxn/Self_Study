for i in range(1, int(input())):
    print(int((i / 9) * pow(10, i)))
    # This problem is too strict now, why it doesn't accept str or for or something else
    # I can find 2 other ways like
    print(str(i) * i)
    # OR
    print(i * sum([pow(10, j) for j in range(i)]))
    # OR simply create a list to store elements 1, 22, 333,... to 999999 :)

