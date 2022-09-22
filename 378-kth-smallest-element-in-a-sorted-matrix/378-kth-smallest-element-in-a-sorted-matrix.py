class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap=[]
        heapq.heapify(heap)
        
        for arr in matrix:
            for num in arr:
                heapq.heappush(heap,-num)
                
                if len(heap)>k:
                    heapq.heappop(heap)
        return -heapq.heappop(heap)
    