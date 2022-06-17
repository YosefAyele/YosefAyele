class Solution:
    def isPowerOfThree(self, n):
        if n==1:
            return True
        elif n<1:
            return False
        else:
            m=Solution.isPowerOfThree(self, n/3)
            return m