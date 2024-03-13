class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxValue = 0
        index = 0
        N = len(nums)
        while index < N:
            if nums[index] == 1: 
                count += 1
            else:
                maxValue = max(count, maxValue)
                count = 0
            index += 1
        maxValue = max(count, maxValue)
        return maxValue