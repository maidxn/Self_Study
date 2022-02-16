import math

string = input()
rows = math.floor(math.sqrt(len(string)))
columns = math.ceil(math.sqrt(len(string)))

# This is my way, it's a little long and ummhhh... :> DUMB
substring = []
start = 0
end = columns
while end < len(string):
    substring.append(string[start:end])
    start = end
    end += columns
substring.append(string[start:])

ans = [""] * columns
for each in substring:
    for char_index in range(len(each)):
        ans[char_index] += each[char_index]

print(*ans, sep=" ")


# The second way is shorter and cooler ;;-;;
# Okay, it likes this ARRAY[start:end:step]
# the code here is start by each column in the array right? so it is 1, 2, ... to columnS
# then just jump to the (column_ + columnS)th position at the string.
# And done. If that postition is not in range, it just stops, and doesn't raise INDEX ERRO
# SUPPPER COOLLLLLLLL :>
# Ref here: https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences
for column in range(columns):
    print(string[column::columns], end=" ")
