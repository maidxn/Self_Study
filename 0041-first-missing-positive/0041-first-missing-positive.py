class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        N = len(nums) 
        
        for index in range(N):
            if nums[index] < 0 or nums[index] > N:
                nums[index] = 0
        check = nums[0]
        
        for index in range(N):
            if nums[index] > 0:
                nums[nums[index]%N - 1] += N
     
        if nums[0] == check: return 1
        
        for index in range(N):
            if nums[index] // N == 0:
                return index + 1

        return N