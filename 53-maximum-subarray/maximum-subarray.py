class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs = 0  # current sum
        ms = float('-inf')  # max sum (like Integer.MIN_VALUE in Java)
        
        for element in nums:
            cs = cs + element
            if cs > ms:
                ms = cs
            if cs < 0:
                cs = 0
        return ms
