from itertools import combinations

string, max_len = input().split()
for each_len in range(1, int(max_len) + 1):
    ans_arr = list(combinations(string, each_len))
    ans = []
    for each_arr in ans_arr:
        each_arr = sorted(each_arr)
        each_arr = ''.join(each_arr)
        ans.append(each_arr)
    ans = sorted(ans)
    print(*ans, sep='\n')

