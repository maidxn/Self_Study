left = int(input())
right = int(input())
maximum = 0
for first in range(left, right):
    for second in range(first, right + 1): #Becareful with the range okay?
        maximum = first ^ second if maximum < first ^ second else maximum
print(maximum)
