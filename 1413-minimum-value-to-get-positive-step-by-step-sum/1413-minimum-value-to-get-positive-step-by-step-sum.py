class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        minPre=nums[0]
        pre=[nums[0]]
        
        for i in range(1,len(nums)):
            
            minPre=min(minPre,pre[-1]+nums[i])
            pre.append(pre[-1]+nums[i])
            
        return 1-minPre if minPre<1 else 1