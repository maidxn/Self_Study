returnDay, returnMonth, returnYear = map(int, input().split())
dueDay, dueMonth, dueYear = map(int, input().split())

fine = 0

if returnYear == dueYear:
    if returnMonth > dueMonth:
        fine = 500 * (returnMonth - dueMonth)
    elif returnMonth == dueMonth and returnDay > dueDay:
        fine = 15 * (returnDay - dueDay)
elif returnYear > dueYear:
    fine = 10000

print(fine)
