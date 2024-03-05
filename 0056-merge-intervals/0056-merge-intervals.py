class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals, key=lambda x: x [0])
        temp = intervals[0]
        print(temp)
        for interval in intervals:
            if temp[0] > interval[1]:
                res.append(interval)
                temp = interval
            elif interval[0] > temp[1]:
                res.append(temp)
                temp = interval
            else:
                temp = [min(temp[0], interval[0]), max(temp[1], interval[1])]
                print("update")
                print(temp)
        print(res)
        res.append(temp)
        return res
        