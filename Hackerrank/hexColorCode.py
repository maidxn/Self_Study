import re

numberOfLines = int(input())
for each in range(numberOfLines):
    line = input()
    #  Can omit two lines of code for look cooler :vvvv
    # if len(line) != 0 and line[0] == "#":
    #     continue
    #(?<! ) => Matches if the current position in the string is not preceded by a match for .... This is called a negative lookbehind assertion. Similar to positive lookbehind assertions, the contained pattern must only match strings of some fixed length. Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.
    ans = re.findall("(?<!^)(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})", line)
    for i in ans:
        print(i)

