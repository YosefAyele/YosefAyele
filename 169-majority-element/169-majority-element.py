from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numswithfreq=Counter(nums)
        print(numswithfreq)
        for i in numswithfreq:
            
            if numswithfreq[i]>=len(nums)/2:
                return i
        
        