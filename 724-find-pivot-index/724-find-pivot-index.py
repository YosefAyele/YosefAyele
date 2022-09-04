class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        currSum=0
        Total=sum(nums)
        for i in range(len(nums)):
            
            if 2*currSum == Total - nums[i]: return i
            
            currSum+=nums[i]
            
        return -1
