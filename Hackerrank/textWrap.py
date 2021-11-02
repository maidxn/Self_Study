import textwrap


string = input()
width = int(input())
arr = textwrap.wrap(string, width)
new = "\n".join(arr)
print(new)
# print(*textwrap.wrap(string, width), sep='\n')
