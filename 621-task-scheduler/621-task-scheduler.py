import collections 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q=collections.deque()
        count=collections.Counter(tasks)
        
        heap=[-count[i] for i in count]
        
        heapq.heapify(heap)
        time=0
        while heap or q:
            time+=1
            
            if heap: 
                x=1+heapq.heappop(heap)
                if x : q.append((x,time+n))

            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        
        return time