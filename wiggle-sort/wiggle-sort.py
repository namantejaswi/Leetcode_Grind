class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        #we sort the array and then swap the numbers so the relative order is there
        #and also the intermiddiate number is greater than both left and right
    
    
        nums.sort()
        for i in range(1,len(nums)-1,2):
            
            nums[i],nums[i+1]=nums[i+1],nums[i]