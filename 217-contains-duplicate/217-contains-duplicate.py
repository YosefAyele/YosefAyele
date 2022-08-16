class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for j in d:
            if d[j]>1:
                return True
        return False
        
            
            
        