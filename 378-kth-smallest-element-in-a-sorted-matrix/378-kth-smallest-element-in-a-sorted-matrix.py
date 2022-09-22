class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap=[]
        heapq.heapify(heap)
        
        for arr in matrix:
            for num in arr:
                heapq.heappush(heap,num)
        
        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
    