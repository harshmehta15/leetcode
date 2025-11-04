class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        countvar = 0
        var = None
        for i in range(len(nums)):

            if(count==0):
                var = nums[i]
                count = 1
            elif(nums[i]==var):
                count +=1
            else:
                count -=1
        
        if( nums.count(var)> len(nums)/2):
            return var

            


        