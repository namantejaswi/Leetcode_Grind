class Solution:
    def trap(self, height: List[int]) -> int:
        
        size=len(height)        
                        
        left=[0]*size
        right=[0]*size
    
        max_left_height=0
        max_right_height=0
        trapped_water=0
        
        for i in range(size):
       
            if(height[i]>max_left_height):
                
                max_left_height=height[i]
                
            left[i]=max_left_height
            
        for j in range(size):
            
            if(height[size-1-j]>max_right_height):
            
                max_right_height=height[size-1-j]
                
            right[size-j-1]=max_right_height
        
        for k in range(size):
            
            trapped_water+=min(left[k],right[k])-height[k]
            
        return(trapped_water)