string = input()
# low, up, odd, even = [], [], [], []
# for char in string:
#     if 97 <= ord(char) <= 122:  # Can replace with islower, isupper, ...
#         low.append(char)
#     elif 65 <= ord(char) <= 90:
#         up.append(char)
#     else:
#         number = int(char)
#         if number % 2 == 0:
#             even.append(char)
#         else:
#             odd.append(char)
#
#
# arr = [low, up, odd, even]
# ans = ''
# for each in arr:
#     temp = ''.join(sorted(each))
#     ans += temp
# print(ans)

# OR

l = sorted(list(filter(lambda x: x.islower(), string)))
u = sorted(list(filter(lambda x: x.isupper(), string)))
o = sorted(list(filter(lambda x: x.isdigit() and int(x) % 2 != 0, string)))
e = sorted(list(filter(lambda x: x.isdigit() and int(x) % 2 == 0, string)))
print(''.join(l + u + o + e))

# Much more shorter :)

