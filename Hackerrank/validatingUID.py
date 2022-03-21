def ValidatingUID(string):
    upper = list(filter(lambda x: x.isupper(), string))
    digits = list(filter(lambda x: x.isnumeric(), string))
    return (len(set(string)) == 10 == len(string)) and len(upper) >= 2 and len(digits) >= 3


for each in range(int(input())):
    print('Valid' if ValidatingUID(input()) else 'Invalid')
# No using regex but still elegant (I think so :>)

# And here is the solution using regex
import re

no_repeats = r"(?!.*(.).*\1)"
two_or_more_upper = r"(?=(?:.*[A-Z]){2,})"
three_or_more_digits = r"(?=(?:.*\d){3,})"
ten_alphanumerics = r"[a-zA-Z0-9]{10}"
filters = no_repeats, two_or_more_upper, three_or_more_digits, ten_alphanumerics

for uid in [input() for _ in range(int(input()))]:
    if all([re.match(f, uid) for f in filters]):
        print("Valid")
    else:
        print("Invalid")
# I don't know why but looking at regex make me fear :<
