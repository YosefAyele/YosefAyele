class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res=0
        mapp={}
        summ=0
        
        for i in range(len(nums)):
            
            summ+=nums[i]
            
            if summ==k: res+=1  
                
            if summ-k in mapp:
                res+=mapp[summ-k]
    
            mapp[summ]=mapp.get(summ,0)+1
            
        return res

        
                