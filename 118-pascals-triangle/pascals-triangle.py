class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            row = [1]
            ans = 1
            for i in range(1, n + 1):
                ans = ans * (n - i + 1) // i   # use integer division directly
                row.append(ans)
            res.append(row)
        return res
