class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        max_to_the_left = [0]*len(height)
        max_to_the_right = [0]*len(height)
        
        
        mx_l=height[0]
        mx_r=height[-1]
        
        
        for i in range(1,len(height)):
            
            mx_l = max(height[i],mx_l)
            
            max_to_the_left[i]=mx_l
            
        for i in range(len(height)-2,-1,-1):
        
            mx_r = max(height[i],mx_r)
            
            max_to_the_right[i] =mx_r
            
        #print(max_to_the_left,max_to_the_right)    
        #Now water stored by each index of height h will be
        # min(mx_to_the_left,mx_to the right)-h
        
        total=0
        
        
        for i in range(len(height)):
            
            total+= max(0,min(max_to_the_left[i], max_to_the_right[i])-height[i])
        
        return total