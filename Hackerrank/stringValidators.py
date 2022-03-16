string = input()
alnum, alpha, digit, lower, upper = False, False, False, False, False

for char in string:
    if char.isalnum():
        alnum = True
    if char.isalpha():
        alpha = True
    if char.isdigit():
        digit = True
    if char.islower():
        lower = True
    if char.isupper():
        upper = True
print(alnum, alpha, digit, lower, upper, sep='\n')

# ORR
# the built-in any() check if any element is TRUE
string = input()
print(any(c.isalnum() for c in string))
print(any(c.isalpha() for c in string))
print(any(c.isdigit() for c in string))
print(any(c.islower() for c in string))
print(any(c.isupper() for c in string))

