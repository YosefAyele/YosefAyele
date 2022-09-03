class Solution:
    def reverseWords(self, s: str) -> str:
        
        sl=s.split()
        
        for i,word in enumerate(sl):
            
            sl[i]=word[::-1]
            
        return " ".join(sl)