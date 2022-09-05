class NumMatrix:

    def __init__(self, mat: List[List[int]]):
        row,col= len(mat),len(mat[0])
        self.sums=[[0]*(col+1) for i in range(row+1)]
        self.mat=mat
        for r in range(row):
            prefix=0
            
            for c in range(col):
                prefix+=mat[r][c]
                self.sums[r+1][c+1]=prefix+self.sums[r][c+1]
            
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        sums=self.sums
        mat=self.mat
        return sums[r2+1][c2+1]-sums[r2+1][c1]-sums[r1][c2+1]+ sums[r1][c1 ]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)