class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        output=d[s[0]]
        for i in range(1,len(s)):
            if d[s[i]]>d[s[i-1]]:
                output=output-2*d[s[i-1]]+d[s[i]]
            else:
                output+=d[s[i]]
        return output
            
            