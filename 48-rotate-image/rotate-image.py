class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i): 
                if(i!=j):               
                    self.swapInternal(i,j,matrix)

        for i in range(0,n):
            matrix[i].reverse()
            

    def swapMatrix(self,i,j,x,y,matrix):
        temp = matrix[i][j]
        matrix[i][j] = matrix[x][y]
        matrix[x][y] = temp
    
    def swapInternal(self,i,j,matrix):

        temp= matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp