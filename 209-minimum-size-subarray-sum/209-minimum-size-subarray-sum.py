class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if target>sum(nums): return 0
        
        currsum=0
        r=l=0
        res=len(nums)
        while r<len(nums):
            
            currsum+=nums[r]
            
            while currsum>=target:
                res=min(res,r-l+1)
                currsum-=nums[l]
                l+=1
            
            r+=1
                
        
        return res