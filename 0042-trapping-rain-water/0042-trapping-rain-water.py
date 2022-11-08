class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        
        length=len(height)
        
        left=[0]*length
        right=[0]*length
        
        mx_l,mx_r=0,0
        
        water=0
        
        
        for i in range(length):
            
            if height[i]>mx_l:
                mx_l=height[i]
                
            left[i]=mx_l

            
        for j in range(length):
            
            if height[length-1-j]>mx_r:
                mx_r=height[length-j-1]
                
            right[length-j-1]=mx_r
        
        

        for k in range(length):
            
            water+=min(left[k],right[k])-height[k]
            
        return(water)