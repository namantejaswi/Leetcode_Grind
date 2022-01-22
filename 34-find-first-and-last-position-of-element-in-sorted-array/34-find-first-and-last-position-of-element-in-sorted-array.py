class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        #we first use binary search to find the element
        #then we use binary search to find the start and then to find the end
        
        
        
        
        def leftsearch(nums,target):
            
            low=0
            high=len(nums)-1
            pos=-1
            
            while(low<=high):
                
                mid = (low+high)//2
                
                if nums[mid]==target:
                    
                    #we need to find leftmost so we shift interval toward left
                    
                    high=mid-1
                    pos=mid
                    
                    
                elif nums[mid]<target:
                    low=mid+1
                    
                elif nums[mid]>target:
                    high=mid-1
                    
            return pos
        
        
        
        def rightsearch(nums,target):
            
            low=0
            high=len(nums)-1
            pos=-1
            
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                #we need right most so we update low to mid+1
                
                    low=mid+1
                    pos=mid
                
                
                if nums[mid]>target:
                    high=mid-1
                
                if nums[mid]<target:
                    low=mid+1
                
            return pos
        
        
        
        l=leftsearch(nums,target)
        r=rightsearch(nums,target)
        
        return [l,r]
        
        
        
            
                
                
                
                
                
                
                
            
            
            
                    
                    
        
                    
                    
                    
                    
                    