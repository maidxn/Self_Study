from itertools import combinations_with_replacement

string, combinations = input().split()

all_combinations = list(combinations_with_replacement(string, int(combinations)))
remove_list = []
for each_combination in all_combinations:
    ans = ''
    new_one = sorted(each_combination)
    for each in new_one:
        ans += each
    remove_list.append(ans)
print(*sorted(remove_list), sep='\n')


