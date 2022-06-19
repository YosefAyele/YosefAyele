class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        else:
            return Solution.isPowerOfFour(self,n/4)
        