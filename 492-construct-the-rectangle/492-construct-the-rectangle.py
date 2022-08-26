class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width=int(sqrt(area))
        
        def recur(w):
            if area%w==0:
                return [int(area/w),w]
            return recur(w-1)
        return recur(width)
        