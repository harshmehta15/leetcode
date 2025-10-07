class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1

        while(mid<=high):
            if(nums[mid]==0):
                self.swapNums(mid,low,nums)
                low = low+1
                mid = mid +1
            elif(nums[mid]==1):
                mid = mid+1
            else:
                self.swapNums(mid,high,nums)
                high= high-1


    def swapNums(self,a,b,nums):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
        