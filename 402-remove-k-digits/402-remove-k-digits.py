class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        smin=[]
        for i in range(len(num)):
            while k and smin and int(num[i])<int(smin[-1]):
                smin.pop()
                k-=1
            smin.append(num[i])
        if k:
            return "".join(smin[:-k]).lstrip("0") or "0"
        else:
            return "".join(smin).lstrip("0") or "0"
      