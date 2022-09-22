class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l=len(stones)
        for i in range(l):
            stones[i]*=-1
        heapq.heapify(stones)
        
        while stones:
            
            y=-heapq.heappop(stones)
            if stones: 
                x= -heapq.heappop(stones)
            else:
                return y
            
            if x<y: heapq.heappush(stones,x-y)
        return 0
    
    