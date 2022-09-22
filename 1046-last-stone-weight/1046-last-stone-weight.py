class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l=len(stones)
        stones.sort()
        
        if l==1: return stones[0]
    
        while len(stones)>=2:
            y,x=stones.pop(),stones.pop()
            
            if x<y:
                stones.append(y-x)
                stones.sort()
        if stones: 
            return stones[0] 
        else: return 0