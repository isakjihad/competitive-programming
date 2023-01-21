class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in range(len(nums)):
            if nums[i]:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
        return nums
