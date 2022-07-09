class Solution:
    def isHappy(self, n: int) -> bool:
        sums=[]
        def ishappy(n):
            if n==1:
                return True
            summ=0
            while n:
                summ+=(n%10)**2
                n=n//10
            if summ in sums:
                return False
            sums.append(summ)
            return ishappy(summ)
        return ishappy(n)
            