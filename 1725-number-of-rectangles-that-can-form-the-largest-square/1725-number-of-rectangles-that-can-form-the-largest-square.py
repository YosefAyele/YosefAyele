class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
#         squares=0
        
#         for i in rectangles:
#             squares.append(min(i[0],i[1]))
            
#         return collections.Counter(squares)[max(squares)]
        count=0
        def recur(rect,i,maxval):
            
            global count
            
            if i==len(rect):
                return count
            
            minm=min(rect[i][0],rect[i][1])
            
            if minm>maxval:

                count=1
            
                maxval=minm
            elif minm==maxval:
                
                count+=1
            return recur(rect,i+1,maxval)
             
        
        
        return   recur(rectangles,0,0)