from collections import deque

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds=deque()
        res=0
        odds.append(-1)
        
        for i in range(len(nums)):
            
            if nums[i]%2: odds.append(i)
            if len(odds)>k+1: odds.popleft()
            if len(odds)==k+1: res=res+odds[1]-odds[0]
                
        return res
        