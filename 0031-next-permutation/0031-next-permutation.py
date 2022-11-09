class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)<=1:    return nums
        #find rightmost element smaller than its next element i.e a valley
        
        idx=None
        rgt=None
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx=i
                break
            
        else:   return nums.reverse()
        
        #find rightmost smallest elment in the right of valley greater than valley
        
        for j in range(len(nums)-1,idx,-1):
            if nums[j]>nums[idx]:
                rgt=j
                break
                
        #print(idx,rgt)
        nums[idx],nums[rgt]=nums[rgt],nums[idx]
        
        #Reverse the elements to the right of right of orignal valley  index
        
        
        nums[idx+1:]=reversed(nums[idx+1:])
        return nums