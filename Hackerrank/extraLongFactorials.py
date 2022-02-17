number = int(input())
factorial = 1

# Yeah, a simple loop
for i in range(1, number + 1):
    factorial *= i
print(factorial)

# And now, recursion :)


def FindFactorial(num):
    if num == 1:
        return 1
    return num * FindFactorial(num - 1)
    # I forgot how to do this in recursion way ;;-;;


print(FindFactorial(int(input())))
