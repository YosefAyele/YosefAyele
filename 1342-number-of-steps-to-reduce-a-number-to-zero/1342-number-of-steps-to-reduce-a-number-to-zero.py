class Solution:
    def numberOfSteps(self, num: int) -> int:
        ctr=0
        while num>0:
            num=num//2 if num%2==0 else num-1
            ctr+=1
        return ctr
            