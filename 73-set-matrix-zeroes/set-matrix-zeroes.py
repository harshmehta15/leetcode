class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        rowref = [1 for i in range(rows)]
        colref = [1 for j in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j]==0):
                    rowref[i]=0
                    colref[j]=0
        
        for i in range(rows):
            for j in range(cols):
                if(rowref[i]==0 or colref[j]==0):
                    matrix[i][j]=0


        
        