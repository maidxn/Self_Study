# def Find_Polynomial(array):
#     power = list(range(len(array) - 1, -1, -1))
#     ans = 0
#     for x, hat in zip(array, power):
#         ans += pow(x, power)
#
#
# number, answer = map(int, input().split())
# polynomial = [int(i) for i in input().split()]
# if Find_Polynomial(polynomial) == answer:
#     print("True")
# else:
#     print("False")

#Note here is if want to eval() somethings, the input_1 in the 16th lines, must be the same with the input
#in polynomial. Get it!
x, answer = map(int, input().split())
polynomial = input()
if eval(polynomial) == answer:
    print("True")
else:
    print("False")
