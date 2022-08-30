class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        commons=[strs[0]]
        
        for i in range(1,len(strs)):
            currcomn=""
            run=min(len(commons[-1]),len(strs[i]))
            for j in range(run):
                if strs[i][j]!=commons[-1][j]:
                    commons[-1]=currcomn
                    break
                else:
                    currcomn+=strs[i][j]
            commons[-1]=currcomn
        return commons[-1]
        