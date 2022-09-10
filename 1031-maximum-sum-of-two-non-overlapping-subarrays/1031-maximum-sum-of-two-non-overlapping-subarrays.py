class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        def maxsum(fl,sl):
            
            initial=fl+sl
            sumF=sumS=0
            for i in range(initial):
                if i< fl:
                    sumF+=nums[i]
                else:
                    sumS+=nums[i]
            maxF=sumF
            res=sumF+sumS
            
            for i in range(initial,len(nums)):
                sumF=sumF+nums[i-sl]-nums[i-sl-fl]
                maxF=max(maxF,sumF)
                
                sumS=sumS+nums[i]-nums[i-sl]
                
                res=max(res,maxF+sumS)
            return res
        
        return max(maxsum(firstLen,secondLen),maxsum(secondLen,firstLen))
                    