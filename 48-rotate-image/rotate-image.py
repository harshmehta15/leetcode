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

        if(n%2!=0):
            left = math.floor(n/2)
        else:
            left = (n//2)

        for i in range(0,n):
            for j in range(0,left):
                self.swapMatrix(i,j,i,n-j-1,matrix)

    def swapMatrix(self,i,j,x,y,matrix):
        temp = matrix[i][j]
        matrix[i][j] = matrix[x][y]
        matrix[x][y] = temp
    
    def swapInternal(self,i,j,matrix):

        temp= matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp