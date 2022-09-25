class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=len(nums)
        i=0
        summ=0
        flag=False
        for j in range(len(nums)):
            
            summ+=nums[j]
            
            while summ>=target:
                res=min(res,j-i+1)
                flag=True
                summ-=nums[i]
                i+=1
                
        return res if flag else 0
            
            
            