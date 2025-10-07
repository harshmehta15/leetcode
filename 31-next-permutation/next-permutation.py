class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        i = len(nums)-1
        while i>0:
            if(nums[i]>nums[i-1]):
                index = i-1
                break
            i-=1
        
        if(index == -1):
            return nums.reverse()
        
        j = len(nums)-1
        while j > index:
            if(nums[j]>nums[index]):
                temp = nums[j]
                nums[j] = nums[index]
                nums[index] = temp
                break
            j-=1
        
        nums[index+1:]=reversed(nums[index+1:])
        return nums

        


        
            
        