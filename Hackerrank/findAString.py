import re


string = input()
substring = input()
print(len(list(re.finditer(r'(?={})'.format(substring), string))))



