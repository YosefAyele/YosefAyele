from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=Counter(nums[:k+1])
        if any(i>=2 for i in window.values()):
            return True
        for i in range(k+1,len(nums)):
            numin=nums[i]
            numout=nums[i-k-1]
            window[numin]+=1
            window[numout]-=1
            if window[numin]>=2:
                return True
        return False
            
            
            
        