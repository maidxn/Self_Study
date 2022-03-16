dictionary = {}


def CountCharacters(string, index):
    global dictionary
    for each in string:
        if each not in dictionary.keys():
            dictionary[each] = [1, 0] if index == 0 else [0, 1]
        else:
            dictionary[each][index] += 1


string_1 = input()
string_2 = input()

CountCharacters(string_1, 0)
CountCharacters(string_2, 1)

deletions = 0
for key in dictionary.keys():
    if dictionary[key][0] == 0:
        deletions += dictionary[key][1]
    elif dictionary[key][1] == 0:
        deletions += dictionary[key][0]
    else:
        deletions += abs(dictionary[key][0] - dictionary[key][1])

print(deletions)

# ;;-;; I'm sick today, so tired
