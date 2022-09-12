class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_ind={}
        
        for i in range(len(nums)):
            if nums[i] in val_ind:
                return i,val_ind[nums[i]]
            else:
                val_ind[target-nums[i]]=i