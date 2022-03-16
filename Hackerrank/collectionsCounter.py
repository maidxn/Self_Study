from collections import Counter


def FindTheShoesAndPrice(counter, index, value):
    if index in counter.keys() and counter[index] > 0:
        counter[index] -= 1
        return value
    return 0


numberOfShoes = int(input())
shoes = [int(i) for i in input().split()]
numberOfCustomers = int(input())
money = 0
counter = Counter(shoes)
for customer in range(numberOfCustomers):
    size, price = map(int, input().split())
    money += FindTheShoesAndPrice(counter, size, price)
print(money)
