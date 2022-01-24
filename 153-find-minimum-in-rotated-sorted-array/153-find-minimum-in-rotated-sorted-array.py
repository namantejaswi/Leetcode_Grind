class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        
        #if the array is sorted then the we look for the first elment which is smaller than start
        
        low=0
        high=len(nums)-1
        pos=0
        
        if len(nums)==1:    
            return nums[0]
        if len(nums)<3:
            return min(nums)
        
        
        while(low<=high):
            
            mid=(low+high)//2
            
            print("low",low,"high",high)
            print("mid",mid,"nums[mid]",nums[mid])
            #unique elements mid cant be same as start
            
            if nums[mid]<nums[0]:
                print("setting pos to",mid)
                pos=mid
                high=mid-1
                
            if nums[mid]>=nums[0]:
                low=mid+1
                
                
        return nums[pos]