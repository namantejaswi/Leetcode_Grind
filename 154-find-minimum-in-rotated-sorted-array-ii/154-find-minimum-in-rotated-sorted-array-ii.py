class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        
        #if the array is sorted then the we look for the first elment which is smaller than start
        
        low=0
        high=len(nums)-1
        pos=0
        
        if len(nums)==1:    
            return nums[0]
        
        while(low<high):
            
            mid=(low+high)//2
            
            #print("low",low,"high",high)
            #print("mid",mid,"nums[mid]",nums[mid])
    
            
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                pos=low
            
            elif nums[mid]<=nums[high]:
                #print("setting pos to",mid)
                high=mid
                
            else:
                low=mid+1
                pos=low
                
                
        return nums[pos]