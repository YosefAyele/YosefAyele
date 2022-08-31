class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
#         commons=[strs[0]]
        
#         for i in range(1,len(strs)):
#             currcomn=""
#             run=min(len(commons[-1]),len(strs[i]))
#             for j in range(run):
#                 if strs[i][j]!=commons[-1][j]:
#                     commons[-1]=currcomn
#                     break
#                 else:
#                     currcomn+=strs[i][j]
#             commons[-1]=currcomn
        # return commons[-1]
        
        def divide(strs,i,j):
            
            if i==j:
                return strs[i]
            else:
                mid=(i+j)//2
                l=divide(strs,i,mid)
                r=divide(strs,mid+1,j)
                run=min(len(l),len(r))

                for i in range(run):
                    if l[i]!=r[i]:
                        return l[:i]
                return l[:run]
        return divide(strs,0,len(strs)-1)
            
            
    
        
        