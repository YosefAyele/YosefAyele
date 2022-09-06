class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mapp={0:-1}
        
        summ=0
        
        for i in range(len(nums)):
            summ+=nums[i]
            
            if summ%k not in mapp:
                mapp[summ%k]=i
            elif i-mapp[summ%k]>1:
                return True
            
        return False
            
                
                
        
        
        
        
        
        
        
        
        
        
            