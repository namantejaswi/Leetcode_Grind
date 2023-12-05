class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        #We visually see that we can count the amount of water for each point in a linear pass, visually it is intutive but mathematically 
        
        #a points water contributing ability is limited by the lower height on either side 
        
        #each index will contribute water of the amount min( max height to the left from current point, max height to the right)-height[i]
        
        
        
        max_to_left = [0]*len(height)
        max_to_right = [0]*len(height)
        
        
        mx_l=height[0]
        for i in range(1,len(height)):
            mx_l=max(height[i-1],mx_l)
            max_to_left[i] = mx_l
            
            
        mx_r=height[-1]
        for i in range(len(height)-2,-1,-1):

            mx_r = max(height[i+1],mx_r)
            max_to_right[i] = mx_r
        
        #print(max_to_left,max_to_right)
         
        water = 0    
        
        for i in range(len(height)):
            
            contribution =  max(0,min(max_to_left[i],max_to_right[i])-height[i])
            water+=contribution
            
        return water
            
            
            
            