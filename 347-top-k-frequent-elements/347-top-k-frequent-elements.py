class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        res=[]
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
        
        maxheap=[[-freq,num] for num,freq in d.items()]
        
        heapq.heapify(maxheap)
        
        
        for _ in range(k):
            res.append(heapq.heappop(maxheap)[1])
        
        return res

  