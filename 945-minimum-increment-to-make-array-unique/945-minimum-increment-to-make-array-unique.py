
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        curr=-1
        output=0
        
        for i in nums:
            curr=max(curr+1,i)
            output+=curr-i
            
        return output
