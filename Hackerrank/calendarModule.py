import calendar

month, day, year = map(int, input().split())
weekday = calendar.weekday(year, month, day)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
# If else is too longggggg
print(days[weekday])

