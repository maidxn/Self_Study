from itertools import permutations

string, length = input().split()
length = int(length)
print(*sorted([''.join(i) for i in permutations(string, length)]), sep='\n')


