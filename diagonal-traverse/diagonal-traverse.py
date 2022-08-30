class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        sums=dict()
        output=[]
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                
                if i+j not in sums:
                    sums[i+j]=[mat[i][j]]
                else:
                    sums[i+j].append(mat[i][j])
        # print(sums)
        
        for k in sums:
            if k%2==0:
                output.extend(sums[k][::-1])
            else:
                output.extend(sums[k])
        return output