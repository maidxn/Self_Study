class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            val = nums[i] % N 
            nums[val - 1] += N
        res = []
        missing = 1
        print(nums)
        for num in nums:
            if num <= N:
                res.append(missing)
            missing += 1
        return res
            
        