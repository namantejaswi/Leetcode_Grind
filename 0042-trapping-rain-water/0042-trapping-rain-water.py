class Solution:
    def trap(self, height: List[int]) -> int:
        
        #we try to calculate the water trapped by each index
        #water trapped by each index is limited by the largest element to the left and right , min(max_to_the_left,max_to the_right)-h
        
        max_to_left = [0 for i in range(len(height))]
        max_to_right = [0 for j in range(len(height))]
        
        mx_l = height[0]
        mx_r = height[-1]
        
        
        for i in range(1,len(height)):
        
            max_to_left[i] = mx_l
            mx_l = max(mx_l,height[i])
            
            
        for j in range(len(height)-2,-1,-1):
            max_to_right[j] = mx_r
            mx_r = max(mx_r, height[j])
        
        total = 0
        
        for h in range(len(height)):
            
            total += max(min(max_to_left[h],max_to_right[h])-height[h], 0)
            
        return total
            