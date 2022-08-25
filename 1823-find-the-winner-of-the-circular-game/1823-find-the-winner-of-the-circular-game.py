class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        Q=[i for i in range(1,n+1)]
        r=-1
        
        while len(Q)>1:
            r=(r+k)%len(Q)
            Q.pop(r)
            r-=1
            
        return Q[0]
        
            
            