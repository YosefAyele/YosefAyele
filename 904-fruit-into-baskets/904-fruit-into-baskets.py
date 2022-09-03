class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits)==1: return 1
        
        i=0
        
        res=0
        
        counts=collections.Counter()
        
        for j in range(len(fruits)):
            
            counts[fruits[j]]+=1
            
            while len(counts)>2:
                
                counts[fruits[i]]-=1
                
                if counts[fruits[i]]==0:
                    counts.pop(fruits[i])
                i+=1
                
            res=max(res,j-i+1)
            
        return res
                
                
            