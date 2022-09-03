class Solution:
    def longestOnes(self, n: List[int], k: int) -> int:
        
        l=0
        
        for r in range(len(n)):
            
            if n[r]==0:
                k-=1
                
            if k<0:
                if n[l]==0:
                    k+=1
                l+=1
            
        return r-l+1
            
        