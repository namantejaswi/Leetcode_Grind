class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        lptr = 0 
        rptr = len(height)-1
        
        mx = 0 
        
        while rptr>lptr:
            
            area = (rptr-lptr)*min(height[lptr],height[rptr])

            mx = max (mx, area)
            
            #we move inwards from the lesser height in case we find a taller line which helps stroring more vertical water horizontally we are maxed out only way is to see if we can get more vertical estate, if heights are equal we can move inward in either direction
            
            
            if height[lptr]>height[rptr]:rptr-=1
                
            else:   lptr+=1
                
                
        return mx
            
            