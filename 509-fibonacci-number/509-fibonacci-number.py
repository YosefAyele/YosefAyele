class Solution:
    def fib(self, n: int) -> int:
        
        if n==0: return 0
            
        if n==2 or n==1:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)