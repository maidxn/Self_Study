class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        
        left, right, mid = 0, len(nums) - 1, len(nums) // 2
        while left < right:
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1
            mid = (right + left) // 2
        if target <= nums[left]:
            return left
        return left + 1
   
        