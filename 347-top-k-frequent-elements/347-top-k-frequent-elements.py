from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=len(nums)
        ctr=Counter(nums)
        
        bucket=[[] for i in range(l+1)]
        for num in ctr:
            bucket[ctr[num]].append(num)
        
        res=[]
        
        for i in range(l,-1,-1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    if len(res)==k: return res
            
            
            
