import cmath

user_input = input()
x, y = '', ''
pos = 0
flag = False
for each in user_input:
    if each == '+':
        flag = True
        continue
    elif each == '-' and pos != 0:
        flag = True
        y += each
        continue
    if flag:
        y += each
    else:
        x += each
    pos += 1

print(*cmath.polar(complex(float(x), float(y[:-1]))), sep='\n')
# or just simply take all the input, Python understands what you really want :)
print(*cmath.polar(complex(input())), sep='\n')
# It's smarter than me now :)
