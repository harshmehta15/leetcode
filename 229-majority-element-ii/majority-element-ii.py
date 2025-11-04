class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1 = count2 = 0
        var1 = var2 = None
        returnarray =[]
        for i in range(len(nums)):
            if(count1 ==0 and nums[i]!=var2):
                count1 = 1
                var1 = nums[i]
            elif(count2 ==0 and nums[i]!=var1):
                count2 = 1
                var2 = nums[i]
            elif(nums[i]==var1):
                count1+=1
            elif(nums[i]==var2):
                count2+=1
            else:
                count1-=1
                count2-=1
        
        if(nums.count(var1)>math.floor(len(nums)/3)):
            returnarray.append(var1)
        if(nums.count(var2)>(math.floor(len(nums)/3))):
            returnarray.append(var2)
        
        return returnarray


        