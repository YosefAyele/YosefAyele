class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        res=0
        
        l,r=0,0
        
        while r<len(prices):
            
            while r<len(prices) and prices[l]-prices[r]==r-l:
                r+=1
            
            while l<r:
                res+=r-l
                l+=1
                
        return res
        