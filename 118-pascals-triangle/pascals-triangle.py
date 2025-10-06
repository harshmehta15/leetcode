import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        list2=[]
        for i in range(numRows):
            list2.append(self.generaterow(i))
        
        return list2

        
    def generaterow(self,n):

        list1=[]
        for i in range(n+1):
            element = (math.factorial(n)//(math.factorial(n-i)*math.factorial(i)))
            list1.append(element)
        
        return list1
