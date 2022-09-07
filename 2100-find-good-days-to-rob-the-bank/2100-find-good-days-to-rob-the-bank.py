class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        res=[]
        
        
        inc=[0]
        
        for i in range(len(security)-2,-1,-1):
            if security[i+1]>=security[i]:
                inc.append(inc[-1]+1)
            else: inc.append(0)
        
        inc[:]=inc[::-1]
        dec=0
        if dec>=time and inc[0]>=time: res.append(0)
        for i in range(1,len(security)):
            if security[i]<=security[i-1]:
                dec+=1
            else:
                dec=0
                
            if dec>=time and inc[i]>=time:
                res.append(i)
        return res
        
        