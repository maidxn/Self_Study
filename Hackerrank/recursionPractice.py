# Print sum 1 to n number

def CountSum(num):
    if num == 1:
        return 1
    return num + CountSum(num - 1)


# Find the -th Fibonacci number

def FindFibonacci(num):
    if num <= 2:
        return 1
    return FindFibonacci(num - 1) + FindFibonacci(num - 2)


# Print all elements in one array

def PrintElements(a, pos):
    if pos >= len(a):
        return
    print("***", a[pos], "***")
    PrintElements(a, pos + 1)


arr = [1, 2, 3, 4, 5, 6]
PrintElements(arr, 0)
