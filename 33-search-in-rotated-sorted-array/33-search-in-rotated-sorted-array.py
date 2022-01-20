class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Finding pivot using linear scan defeats the purpose as in the worst
        #case we are taking 0(n) time to fin the pivot only we can use binary
        #search to find the peak to find the pivot in log(n). 
        
        #To the left and right of pivot we will have uniformly increasing
        #array using this we can solve in single pass
        
        
        left=0
        right=len(nums)-1
        
        while(left<=right):
            
            mid=(left+right)//2      
            if nums[mid]==target:   
                return mid
            
            elif nums[mid]>=nums[left]:    #i.e left half is increasing
        
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                    
                else:
                    left=mid+1
            
            else:
                if target<=nums[right] and target>nums[mid]:
                    left=mid+1
                else:
                    right=mid -1
                    
        return -1
                