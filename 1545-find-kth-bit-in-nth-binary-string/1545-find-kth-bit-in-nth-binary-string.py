class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(i):
            if i==1:
                return "0"
            s=helper(i-1)
            transtable=s.maketrans("01","10","")
            s=s.translate(transtable)
            return helper(i-1)+"1"+s[::-1]
        return helper(n)[k-1]
        