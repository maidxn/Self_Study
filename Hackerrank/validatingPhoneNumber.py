import re

#My way
numberOfTest = int(input())
for each in range(numberOfTest):
    phoneNumber = input()
    if len(phoneNumber) == 10 and re.search("^7|^8|^9", phoneNumber) and (not re.search("[A-Z]", phoneNumber)):
        print("YES")
    else:
        print("NO")

#The smarter way to do
numberOfTest = int(input())
for each in range(numberOfTest):
    phoneNumber = input()
    if len(phoneNumber) == 10 and re.search("^[789]\d{9}", phoneNumber):
        print("YES")
    else:
        print("NO")

#^[789] means starts with 7 or 8 or 9, \d means if there is a digit 0-9. And {9} means exactly 9 times
#Much more easier right???