class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0        
        tempsum = float('-inf')
        currentsum = 0
        allnegative = False

        if(max(nums)<0):
            return max(nums)


        while(i<len(nums)):
            currentsum = currentsum + nums[i]
            if(currentsum<0):
                currentsum = 0
            if(currentsum>tempsum):
                tempsum = currentsum
            i=i+1
        return tempsum
