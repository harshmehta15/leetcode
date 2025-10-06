class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        list2 = []
        for i in range(numRows):
            list2.append(self.generaterow(i))
        return list2

    def generaterow(self,n):
        list1 = []
        list1.append(1)
        ans = 1
        for i in range(1,n+1):
            ans = (ans * (n-i+1))/i
            list1.append(int(ans))
        return list1
    