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
        # quên gòi :"> hết biết làm gòi
        # cíuuuuu
        # tới đây gòi sao nữa :<<<< à =))) lâu quá gòi, hơn gòi, lẻ 3 ngày nưa 
        for index in range(N):
            if nums[index] // N == 0: # =)))
                return index + 1 
        return N
        # tới đây gòi hổng biết làm anh iu :< chỉ đi :<<<
        # thì nhớ làm như zị à :>> à hiểu gòi
        # ơ???? đúng gòi mà baaaaa
        # ủa sai chỗ nàooooooooooooo
