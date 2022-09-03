class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
         
        currsum=0
        r=l=0
        res=len(nums)+1
        while r<len(nums):
            
            currsum+=nums[r]
            
            while currsum>=target:
                res=min(res,r-l+1)
                currsum-=nums[l]
                l+=1
            
            r+=1
                
        
        return res if res<len(nums)+1 else 0