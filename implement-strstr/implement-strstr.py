class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl=len(needle)
        hl=len(haystack)
        if nl>hl:
            return -1
        l=r=0
        
        while r<hl:
            if r-l+1==nl:
                if haystack[l:r+1]==needle:
                    return l
                l+=1
            r+=1
        return -1
        