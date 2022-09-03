class Solution:
    def getRow(self, ri: int) -> List[int]:
        
        res=[[1]]
        
        for i in range(1,ri+1):
            
            temp=[0]+res[-1]+[0]
            
            curr=[]
            
            for j in range(i+1):
                curr.append(temp[j]+temp[j+1])
            res.append(curr)
        return res[ri]
        