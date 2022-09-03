class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res=0
#         window=""
        
#         l=0
        
#         for r in range(len(s)):
            
#             while s[r] in window:
#                 window=window[1:]
#                 l+=1
#             res=max(res,r-l+1)
#             window+=s[r]
#         return res
            
        chars=set()
        
        l=0
        
        for r in range(len(s)):
            
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
                
            chars.add(s[r])
            res=max(res,r-l+1)
            
        return res
        
        
        
        