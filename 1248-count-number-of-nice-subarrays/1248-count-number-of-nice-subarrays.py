class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        
        l=0
        low=-1
        for r in range(len(nums)):
            
            k-=nums[r]%2
            
            if nums[l]%2==0:
                l+=1
            if k<0:
                low=l
            while k<0:
                l+=1
                k+=nums[l]%2
            if k==0:
                res+=l-low
        
        return res
            
            
            
            