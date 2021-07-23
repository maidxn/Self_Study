def permutationEquation(array):
    length = len(array)
    for i in range(1, length + 1):
        pos = 0
        for index in array:
            pos += 1
            if i == index:
                break
        count = 0
        for index in array:
            count += 1
            if index == pos:
                print(count)
                break


size = int(input())
listOfNumbers = [int(i) for i in input().split()]
permutationEquation(listOfNumbers)
