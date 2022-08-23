class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        currSum=0
        Total=sum(nums)
        for i in range(len(nums)):
            
            currSum+=nums[i]

            if currSum-nums[i]==Total-currSum:
                return i
        return -1
