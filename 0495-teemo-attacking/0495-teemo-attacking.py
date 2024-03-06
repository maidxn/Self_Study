class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        prev = timeSeries[0]
        for index in range(1, len(timeSeries)):
            if prev + duration - 1 < timeSeries[index]:
                res += duration
            else:
                res += timeSeries[index] - prev
            prev = timeSeries[index]
        return res + duration