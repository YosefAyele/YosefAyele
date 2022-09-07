class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        
        sumMap={}
        presum=0
        for i in range(len(nums)):
            
            presum+=nums[i]
            if presum==k: res+=1
            
            if presum-k in sumMap:
                res+=sumMap[presum-k]
                
            if presum not in sumMap:
                sumMap[presum]=1
            else:
                sumMap[presum]+=1
            
    

        return res