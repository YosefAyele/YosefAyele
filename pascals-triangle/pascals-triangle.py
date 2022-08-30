class Solution:
    def generate(self, num: int) -> List[List[int]]:
        
        output=[[1]]
        
        for i in range(1,num):
            temp=[0]+output[-1]+[0]
            curr=[]
            for j in range(i+1):
                curr.append(temp[j]+temp[j+1])
            
            output.append(curr)
        return output
                
            
        
        