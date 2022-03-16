import re

s = input()
k = input()

matches = list(re.finditer(r'(?={})'.format(k), s))
# There is something called LOOKAHEAD :)
# https://www.geeksforgeeks.org/python-regex-lookahead/
# New thing V Get :>>>>
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')

