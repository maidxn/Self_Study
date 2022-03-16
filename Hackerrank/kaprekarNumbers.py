def CheckIfKaprekar(number):
    squares = str(number ** 2)
    number = str(number)
    totalDigits = len(number)
    right = squares[-totalDigits:]
    left = squares[:-totalDigits]
    left = 0 if left == '' else int(left)
    right = 0 if right == '' else int(right)
    return left + right


def KaprekarNumber(lower, higher):
    count = 0
    for number in range(lower, higher + 1):
        if number == CheckIfKaprekar(number):
            count += 1
            print(number, end=" ")
    if not count:
        print("INVALID RANGE")


start = int(input())
end = int(input())
KaprekarNumber(start, end)
