class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]>height[j]:
                h=height[j]
                a=h*(j-i)
                j-=1
            else:
                h=height[i]
                a=h*(j-i)
                i+=1
            maxm=max(maxm,a)
        return maxm
            
            
                
        