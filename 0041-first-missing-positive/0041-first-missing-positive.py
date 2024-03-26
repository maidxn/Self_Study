class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        N = len(nums) 


        for index in range(N):
            if nums[index] < 0 or nums[index] > N:
                nums[index] = 0
        value = nums[0]

                
        for index in range(N):
            if nums[index] > 0: 
                update_index = nums[index] % N - 1
                nums[update_index] += N

        if value == nums[0]:
            return 1 

        for index in range(N):
            if nums[index] // N == 0: # =)))
                return index + 1 
        return N