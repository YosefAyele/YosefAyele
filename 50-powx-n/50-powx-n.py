class Solution:
    def myPow(self, x: float, n: int) -> float:
        def Pow(b,e):
            if e==0: return 1
            if b==0: return 0
            
            res=Pow(b*b,e//2)
            
            return b*res if e%2 else res
        output=Pow(x,abs(n))
        
        return output if n>=0 else 1/output
        