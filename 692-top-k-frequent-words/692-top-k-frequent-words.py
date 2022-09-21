from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        
        
        sortedWord=sorted(count,key=lambda item: (-count[item],item))
 

        res=[]
        for i in range(k):
    
            res.append(sortedWord[i])
        return res