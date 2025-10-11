class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(len(matrix)):

            if (target == matrix[i][0] or target ==matrix[i][cols-1]):
                return True

            if(target>matrix[i][0] and target <matrix[i][cols-1]):
                for num in matrix[i]:
                    if(num == target):
                        return True
        
        return False

        