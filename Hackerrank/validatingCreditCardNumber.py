import re

pattern = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'
for i in range(int(input())):
    string = input()
    # Need to replace '-' because the string split by that
    print("Valid" if re.match(pattern, string) and not re.search(r'([\d])\1\1\1', string.replace('-', '')) else "Invalid")
