class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        squares=[]
        
        for i in rectangles:
            squares.append(min(i[0],i[1]))
            
        return collections.Counter(squares)[max(squares)]
        
       