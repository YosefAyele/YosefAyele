class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        res=[]
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
                
        sortedTuples=sorted(d.items(),reverse=True ,key= lambda item: item[1])
        
        for i in range(k):
            res.append(sortedTuples[i][0])
            
        return res
  