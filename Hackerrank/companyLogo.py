from collections import Counter


string = Counter(sorted(input()))
print(*["{} {}".format(i[0], i[1]) for i in string.most_common()[:3]], sep='\n')

# The format is very strange to me ;;-;;



