class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        mn=min(nums)
        mx=max(nums)
        
        mnidx=nums.index(mn)
        mxidx=nums.index(mx)
        
        right=max(mnidx,mxidx)
        left=min(mnidx,mxidx)
        
        return min(right+1,len(nums)-right+left+1,len(nums)-left)
        