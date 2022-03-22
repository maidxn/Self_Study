import re

pattern = r'(?=([^aeiuoAEIOU])([aeiouAEIOU]{2,})([^aeiuoAEIOU]))'
string = input()
ans = re.findall(pattern, string)
if not ans:  # Just bool it to check empty or not :O
    print(-1)
else:
    print(*[i[1] for i in ans], sep='\n')
