class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        left, right, mid = 0, len(nums) - 1, len(nums) // 2
        print(mid)
        while left < right:
            # print("left, right", left, right)
            # print(nums[left:right+1])
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1
            mid = (right + left) // 2
            # print("update", mid)
            # print(left, right)
        print("last")
        print(left, right)
        if target <= nums[left]:
            return left
        return left + 1
   
        