class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        max_to_the_left =[0 for i in range(len(height))]
        
        max_to_the_right =[0 for j in range(len(height))]
        
    
        mx_l=height[0]
        mx_r=height[-1]
        
        for i in range(1,len(height)):
            
            max_to_the_left[i] = mx_l
            mx_l = max(mx_l,height[i])
            
        for j in range(len(height)-2,-1,-1):
            
            max_to_the_right[j] = mx_r
            mx_r = max(mx_r,height[j])
            
        total=0
        for h in range(len(height)):
            
            
            total += max(0,min(max_to_the_left[h],max_to_the_right[h])-height[h])
            
        return total