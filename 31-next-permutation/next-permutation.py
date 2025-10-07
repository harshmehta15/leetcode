class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        index = 0

        while(i>=0): 

            if(nums[i]>nums[i-1]):
                index = i-1
                break
            if(i==1):
                return nums.reverse()
            i-=1

        i = len(nums)-1
        while(i>index):
            if(nums[i]>nums[index]):
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                break
            i-=1
        i = len(nums)-1
        nums[index+1:] = reversed(nums[index+1:])
        return nums
        
            
        