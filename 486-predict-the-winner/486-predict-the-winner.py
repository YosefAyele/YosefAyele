class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        if len(nums)%2==0: return True
        
        def helper(nums,l,r):
            if l==r:
                return nums[l]
            a=nums[l]-helper(nums,l+1,r)
            b=nums[r]-helper(nums,l,r-1)
            
            return max(a,b)
        
        return helper(nums,0,len(nums)-1)>=0