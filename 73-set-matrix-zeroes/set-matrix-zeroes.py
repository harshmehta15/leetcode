class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):

                if(matrix[i][j]==0):
                    self.makerow(i,matrix)
                    self.makecol(j,matrix)
        
        for i in range(rows):
            for j in range(cols):

                if(matrix[i][j]=='a'):
                    matrix[i][j]=0
        
    def makerow(self,n,matrix):
        for i in range(len(matrix[n])):
            if(matrix[n][i]!=0):
                matrix[n][i]='a'

    def makecol(self,n,matrix):
        for i in range(len(matrix)):
            if(matrix[i][n]!=0):
                matrix[i][n]='a'  
        
        