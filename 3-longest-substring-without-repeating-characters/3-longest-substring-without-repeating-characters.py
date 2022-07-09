class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        window=""
        i=0
        j=0
        for l in s:
            while l in window:
                window=window[1:]
                i+=1
            window+=l
            j+=1
            if j-i>maxlength:
                maxlength=j-i
        return maxlength
                