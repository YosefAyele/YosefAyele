class Solution:
    def maxScore(self, cpts: List[int], k: int) -> int:
        n=len(cpts)
        
        r=n-k
        total=sum(cpts[r:])
        
        res=total
        for l in range(k):
            
            total=total+cpts[l]-cpts[r]
            res=max(res,total)
            r+=1
        
        return res
            
            
        