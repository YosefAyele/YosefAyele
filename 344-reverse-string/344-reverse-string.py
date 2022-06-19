class Solution:
    def reverseString(self, s: List[str]) -> None:
        def solve(i,j):
            if i>j:
                return
            s[i], s[j] = s[j], s[i]
            
            solve(i+1, j-1)
            
        solve(0,len(s)-1)
            