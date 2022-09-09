class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        res=0
        
        l,r=0,0
        
        while r<len(prices):
            
            while r<len(prices) and prices[l]-prices[r]==r-l:
                res+=r-l+1
                r+=1
            l=r
                
        return res
        