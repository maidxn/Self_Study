size = int(input())
array = input().split()

if all([item[0] != '-' for item in array]) and any(len(item) == 1 or item == item[::-1] for item in array):
    print("True")
else:
    print("False")
