def birthdayCakeCandles(candles):
    tallest = max(candles)
    count = 0
    for candle in candles:
        if candle == tallest:
            count += 1
    return count


size = int(input())
arr = [int(i) for i in input().split()]
print(birthdayCakeCandles(arr))

