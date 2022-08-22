class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        check=[]
        r=0
        for i in range(len(pushed)):
            
            check.append(pushed[i])
            
            while check and  check[-1]==popped[r]:
                check.pop()
                r+=1
                
        return len(check)==0
                
                