class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res=0
        window=""

        for r in range(len(s)):
            res=max(res,len(window))
            while s[r] in window:
                window=window[1:]
            window+=s[r]
        res=max(res,len(window))
        return res
                
            
            